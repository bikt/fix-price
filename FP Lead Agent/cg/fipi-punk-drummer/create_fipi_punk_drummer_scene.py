import math
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parent
BLEND_PATH = ROOT / "fipi_punk_drummer.blend"
PNG_PATH = ROOT / "fipi_punk_drummer_render_2042x1674.png"
WEBP_PATH = ROOT / "fipi_punk_drummer_render_2042x1674.webp"


def hex_color(value, alpha=1.0):
    value = value.strip("#")
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4)) + (alpha,)


def make_mat(name, color, roughness=0.55, metallic=0.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
    return mat


def assign_mat(obj, mat):
    obj.data.materials.append(mat)
    return obj


def smooth(obj, bevel=None, subdiv=None):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except AttributeError:
        pass
    if bevel:
        mod = obj.modifiers.new("soft bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 8
        mod.affect = "EDGES"
        obj.modifiers.new("weighted highlights", "WEIGHTED_NORMAL")
    if subdiv:
        mod = obj.modifiers.new("gentle subdivision", "SUBSURF")
        mod.levels = subdiv
        mod.render_levels = subdiv
    return obj


def uv_sphere(name, loc, scale, mat, segments=64, rings=32, rotation=(0, 0, 0), subdiv=None):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=segments,
        ring_count=rings,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    assign_mat(obj, mat)
    return smooth(obj, subdiv=subdiv)


def cylinder(name, loc, radius, depth, mat, vertices=64, rotation=(0, 0, 0), bevel=None):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=depth,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    assign_mat(obj, mat)
    return smooth(obj, bevel=bevel)


def cube(name, loc, scale, mat, rotation=(0, 0, 0), bevel=0.02):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    assign_mat(obj, mat)
    return smooth(obj, bevel=bevel)


def torus(name, loc, major_radius, minor_radius, mat, rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_torus_add(
        major_radius=major_radius,
        minor_radius=minor_radius,
        major_segments=96,
        minor_segments=16,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    assign_mat(obj, mat)
    return smooth(obj)


def cylinder_between(name, start, end, radius, mat, vertices=24):
    start = Vector(start)
    end = Vector(end)
    direction = end - start
    mid = start + direction * 0.5
    length = direction.length
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    assign_mat(obj, mat)
    return smooth(obj)


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_arc_curve(name, points, mat, bevel_depth=0.018):
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 24
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 4
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, coords in zip(spline.points, points):
        point.co = (coords[0], coords[1], coords[2], 1)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    assign_mat(obj, mat)
    return obj


def add_text(name, text, loc, size, mat, rotation=(math.radians(90), 0, 0), align="CENTER"):
    bpy.ops.object.text_add(location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.body = text
    obj.data.align_x = align
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.extrude = 0.012
    assign_mat(obj, mat)
    return obj


def create_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    mats = {
        "body": make_mat("Fipi warm turquoise body", hex_color("00A9B7"), 0.62),
        "body_light": make_mat("Fipi lighter teal face and belly", hex_color("B7F3E4"), 0.65),
        "spine": make_mat("Fipi deep blue green soft spines", hex_color("087D91"), 0.68),
        "spine_dark": make_mat("Fipi shadow blue spine bases", hex_color("07577D"), 0.72),
        "eye": make_mat("soft white eyes", hex_color("F8FFFA"), 0.45),
        "pupil": make_mat("black pupils and nose", hex_color("101214"), 0.35),
        "smile": make_mat("friendly charcoal smile", hex_color("202426"), 0.45),
        "mohawk": make_mat("small punk red mohawk", hex_color("E53145"), 0.5),
        "vest": make_mat("matte tiny black punk vest", hex_color("17191C"), 0.7),
        "stud": make_mat("brushed silver studs", hex_color("D7DEE2"), 0.28, metallic=0.75),
        "drum_red": make_mat("Fix Price red drum shells", hex_color("E5262D"), 0.42),
        "drum_white": make_mat("warm white drum heads", hex_color("F4F5EC"), 0.55),
        "chrome": make_mat("chrome hardware", hex_color("B9C3CA"), 0.22, metallic=0.85),
        "cymbal": make_mat("brushed gold cymbals", hex_color("D7A73A"), 0.35, metallic=0.65),
        "wood": make_mat("natural wood drumsticks", hex_color("D6A15D"), 0.5),
        "floor": make_mat("neutral dark studio floor", hex_color("35383B"), 0.75),
        "wall": make_mat("cool neutral studio wall", hex_color("596168"), 0.8),
        "panel_a": make_mat("teal acoustic panels", hex_color("146F7C"), 0.76),
        "panel_b": make_mat("red acoustic panels", hex_color("9D2530"), 0.78),
        "light": make_mat("soft practical lamp glass", hex_color("FFF1B7"), 0.25),
    }

    # Studio envelope.
    cube("studio floor, visible grounding plane", (0, 0.35, -0.04), (5.4, 4.6, 0.04), mats["floor"], bevel=0.01)
    cube("rear studio wall", (0, 2.35, 1.85), (5.4, 0.06, 1.95), mats["wall"], bevel=0.01)
    for i, x in enumerate([-3.6, -2.85, 2.85, 3.6]):
        cube(
            f"side acoustic panel {i+1}",
            (x, 2.26, 2.0),
            (0.22, 0.08, 1.15),
            mats["panel_a"] if i % 2 == 0 else mats["panel_b"],
            bevel=0.045,
        )
    for i, x in enumerate([-1.7, -0.85, 0.85, 1.7]):
        cube(
            f"rear vertical acoustic slab {i+1}",
            (x, 2.24, 2.2),
            (0.25, 0.07, 1.28),
            mats["panel_b"] if i % 2 == 0 else mats["panel_a"],
            bevel=0.035,
        )
    cube("low rear riser shadow block", (0, 2.05, 0.42), (3.6, 0.24, 0.42), mats["floor"], bevel=0.045)

    # Fipi: rounded readable mascot body.
    uv_sphere("Fipi rounded turquoise body", (0, 0.1, 1.35), (0.78, 0.58, 0.92), mats["body"], subdiv=1)
    uv_sphere("Fipi open lighter belly patch", (0, -0.43, 1.36), (0.43, 0.08, 0.53), mats["body_light"])
    uv_sphere("Fipi large friendly head", (0, -0.02, 2.24), (0.76, 0.61, 0.67), mats["body"], subdiv=1)
    uv_sphere("Fipi light oval face patch", (0, -0.56, 2.24), (0.50, 0.09, 0.43), mats["body_light"])
    uv_sphere("Fipi soft muzzle", (0, -0.68, 2.12), (0.28, 0.13, 0.20), mats["body_light"])
    uv_sphere("Fipi round black nose", (0, -0.80, 2.22), (0.13, 0.10, 0.12), mats["pupil"])

    for side in [-1, 1]:
        uv_sphere(f"Fipi small rounded ear {side}", (side * 0.56, -0.04, 2.55), (0.18, 0.10, 0.22), mats["body"])
        uv_sphere(f"Fipi pale inner ear {side}", (side * 0.58, -0.12, 2.55), (0.105, 0.035, 0.13), mats["body_light"])
        uv_sphere(f"Fipi white eye {side}", (side * 0.23, -0.61, 2.42), (0.13, 0.035, 0.17), mats["eye"])
        uv_sphere(f"Fipi black pupil with gentle catchlight {side}", (side * 0.25, -0.645, 2.41), (0.055, 0.018, 0.078), mats["pupil"])
        uv_sphere(f"Fipi tiny eye highlight {side}", (side * 0.225, -0.66, 2.455), (0.018, 0.006, 0.024), mats["eye"])

    add_arc_curve(
        "Fipi friendly smile curve",
        [(-0.18, -0.82, 2.03), (-0.09, -0.845, 1.985), (0, -0.855, 1.98), (0.09, -0.845, 1.985), (0.18, -0.82, 2.03)],
        mats["smile"],
        bevel_depth=0.012,
    )

    # Brand-like soft hedgehog silhouette: big rounded capsules, not aggressive spikes.
    spine_specs = [
        ((-0.74, 0.28, 1.35), (-0.55, 0.35, -0.10), (0.16, 0.16, 0.48)),
        ((0.74, 0.28, 1.35), (0.55, 0.35, -0.10), (0.16, 0.16, 0.48)),
        ((-0.85, 0.30, 1.78), (-0.68, 0.30, 0.05), (0.17, 0.17, 0.56)),
        ((0.85, 0.30, 1.78), (0.68, 0.30, 0.05), (0.17, 0.17, 0.56)),
        ((-0.82, 0.27, 2.20), (-0.62, 0.23, 0.22), (0.17, 0.17, 0.52)),
        ((0.82, 0.27, 2.20), (0.62, 0.23, 0.22), (0.17, 0.17, 0.52)),
        ((-0.58, 0.24, 2.64), (-0.42, 0.16, 0.55), (0.16, 0.16, 0.47)),
        ((0.58, 0.24, 2.64), (0.42, 0.16, 0.55), (0.16, 0.16, 0.47)),
        ((0, 0.24, 2.78), (0, 0.16, 0.78), (0.18, 0.18, 0.50)),
        ((-0.32, 0.34, 1.08), (-0.20, 0.52, -0.36), (0.14, 0.14, 0.42)),
        ((0.32, 0.34, 1.08), (0.20, 0.52, -0.36), (0.14, 0.14, 0.42)),
    ]
    for idx, (loc, direction, scale) in enumerate(spine_specs, 1):
        rot = Vector(direction).to_track_quat("Z", "Y").to_euler()
        uv_sphere(f"Fipi oversized soft spine capsule {idx:02}", loc, scale, mats["spine"] if idx % 3 else mats["spine_dark"], rotation=rot)

    # Punk accents are intentionally small: they read after the mascot, not before it.
    for idx, (z, y, height) in enumerate([(2.84, -0.20, 0.20), (2.98, -0.02, 0.24), (2.82, 0.18, 0.18)], 1):
        rot = Vector((0, -0.12, 1)).to_track_quat("Z", "Y").to_euler()
        uv_sphere(f"small red rounded mohawk tuft {idx}", (0, y, z), (0.055, 0.075, height), mats["mohawk"], segments=32, rings=16, rotation=rot)

    # Tiny open vest and studs, kept below the face.
    cube("left open black vest panel", (-0.28, -0.51, 1.42), (0.18, 0.035, 0.46), mats["vest"], rotation=(0, 0, math.radians(-8)), bevel=0.025)
    cube("right open black vest panel", (0.28, -0.51, 1.42), (0.18, 0.035, 0.46), mats["vest"], rotation=(0, 0, math.radians(8)), bevel=0.025)
    for side in [-1, 1]:
        for j, z in enumerate([1.18, 1.36, 1.54, 1.72]):
            uv_sphere(f"silver vest stud {side} {j}", (side * 0.34, -0.56, z), (0.027, 0.012, 0.027), mats["stud"], segments=24, rings=12)

    # Arms, hands and drumsticks.
    for side in [-1, 1]:
        cylinder_between(f"Fipi upper arm {side}", (side * 0.52, -0.23, 1.68), (side * 0.82, -0.62, 1.47), 0.095, mats["body"])
        cylinder_between(f"Fipi forearm {side}", (side * 0.82, -0.62, 1.47), (side * 0.58, -1.02, 1.28), 0.085, mats["body"])
        uv_sphere(f"Fipi mitten hand {side}", (side * 0.56, -1.04, 1.27), (0.12, 0.10, 0.11), mats["body_light"])
    cylinder_between("left wooden drumstick crossing snare", (-0.66, -1.04, 1.31), (-1.22, -1.48, 1.08), 0.022, mats["wood"], vertices=18)
    cylinder_between("right wooden drumstick raised toward cymbal", (0.57, -1.04, 1.31), (1.26, -1.44, 1.86), 0.022, mats["wood"], vertices=18)
    uv_sphere("left drumstick round tip", (-1.22, -1.48, 1.08), (0.055, 0.055, 0.055), mats["wood"], segments=24, rings=12)
    uv_sphere("right drumstick round tip", (1.26, -1.44, 1.86), (0.055, 0.055, 0.055), mats["wood"], segments=24, rings=12)

    # Drum kit in front: dimensional bass, snare, toms, cymbals and stands.
    cylinder("bass drum red shell", (0, -1.22, 0.62), 0.62, 0.58, mats["drum_red"], rotation=(math.radians(90), 0, 0), bevel=0.02)
    cylinder("bass drum front warm white head", (0, -1.53, 0.62), 0.565, 0.035, mats["drum_white"], rotation=(math.radians(90), 0, 0), bevel=0.01)
    torus("bass drum chrome rim", (0, -1.56, 0.62), 0.575, 0.025, mats["chrome"], rotation=(math.radians(90), 0, 0))
    torus("bass drum rear chrome rim", (0, -0.91, 0.62), 0.575, 0.018, mats["chrome"], rotation=(math.radians(90), 0, 0))
    add_text("small bass drum FIPI mark", "FIPI", (0, -1.595, 0.68), 0.20, mats["spine"], rotation=(math.radians(90), 0, 0))

    cylinder("snare red shell", (-0.92, -1.25, 1.02), 0.34, 0.20, mats["drum_red"], bevel=0.015)
    cylinder("snare white head", (-0.92, -1.25, 1.14), 0.345, 0.025, mats["drum_white"], bevel=0.01)
    torus("snare chrome rim", (-0.92, -1.25, 1.155), 0.345, 0.018, mats["chrome"])
    cylinder_between("snare stand pole", (-0.92, -1.25, 0.18), (-0.92, -1.25, 0.92), 0.025, mats["chrome"])

    for name, x, z, rotz in [("left rack tom", -0.36, 1.35, -9), ("right rack tom", 0.44, 1.35, 10)]:
        cylinder(f"{name} red shell", (x, -1.15, z), 0.31, 0.28, mats["drum_red"], rotation=(math.radians(82), 0, math.radians(rotz)), bevel=0.015)
        cylinder(f"{name} white head", (x, -1.33, z + 0.03), 0.31, 0.025, mats["drum_white"], rotation=(math.radians(82), 0, math.radians(rotz)), bevel=0.01)
        torus(f"{name} chrome rim", (x, -1.35, z + 0.035), 0.31, 0.017, mats["chrome"], rotation=(math.radians(82), 0, math.radians(rotz)))

    cylinder("floor tom red shell", (1.12, -0.88, 0.94), 0.38, 0.52, mats["drum_red"], bevel=0.02)
    cylinder("floor tom white head", (1.12, -0.88, 1.215), 0.385, 0.025, mats["drum_white"], bevel=0.01)
    torus("floor tom chrome rim", (1.12, -0.88, 1.23), 0.385, 0.018, mats["chrome"])

    for x in [-1.45, 1.72]:
        cylinder_between(f"cymbal stand pole {x}", (x, -1.15, 0.12), (x, -1.15, 1.73), 0.024, mats["chrome"])
        cylinder_between(f"cymbal stand tripod a {x}", (x, -1.15, 0.16), (x - 0.32, -1.45, 0.04), 0.018, mats["chrome"])
        cylinder_between(f"cymbal stand tripod b {x}", (x, -1.15, 0.16), (x + 0.34, -1.38, 0.04), 0.018, mats["chrome"])
        cylinder_between(f"cymbal stand tripod c {x}", (x, -1.15, 0.16), (x, -0.76, 0.04), 0.018, mats["chrome"])
    cylinder("left crash cymbal", (-1.45, -1.15, 1.76), 0.46, 0.035, mats["cymbal"], vertices=96, rotation=(math.radians(84), math.radians(-12), 0), bevel=0.005)
    cylinder("right ride cymbal", (1.72, -0.82, 1.82), 0.42, 0.035, mats["cymbal"], vertices=96, rotation=(math.radians(78), math.radians(10), 0), bevel=0.005)
    uv_sphere("left cymbal dome", (-1.45, -1.18, 1.78), (0.14, 0.14, 0.035), mats["cymbal"], segments=32, rings=12)
    uv_sphere("right cymbal dome", (1.72, -0.85, 1.84), (0.13, 0.13, 0.035), mats["cymbal"], segments=32, rings=12)

    # Floor light accents and soft glow bulbs.
    for idx, x in enumerate([-2.55, 2.55], 1):
        cylinder_between(f"studio lamp stand {idx}", (x, 1.75, 0.08), (x, 1.75, 1.58), 0.025, mats["chrome"])
        uv_sphere(f"warm studio lamp bulb {idx}", (x, 1.72, 1.72), (0.16, 0.16, 0.16), mats["light"], segments=32, rings=16)

    # Lighting.
    bpy.ops.object.light_add(type="AREA", location=(0, -3.8, 4.5))
    key = bpy.context.object
    key.name = "large softbox key light"
    key.data.energy = 620
    key.data.size = 4.0
    look_at(key, (0, -0.6, 1.7))

    bpy.ops.object.light_add(type="POINT", location=(-2.7, -1.1, 2.4))
    left = bpy.context.object
    left.name = "cool teal rim light"
    left.data.energy = 160
    left.data.color = (0.24, 0.95, 1.0)

    bpy.ops.object.light_add(type="POINT", location=(2.5, -1.0, 2.5))
    right = bpy.context.object
    right.name = "warm punk red side light"
    right.data.energy = 90
    right.data.color = (1.0, 0.25, 0.28)

    # Camera: frontal 3/4, composed for the requested Figma frame.
    bpy.ops.object.camera_add(location=(3.35, -6.15, 3.0))
    camera = bpy.context.object
    camera.name = "Camera - Fipi punk drummer 3/4"
    look_at(camera, (0, -0.75, 1.50))
    camera.data.lens = 42
    camera.data.dof.use_dof = True
    camera.data.dof.focus_object = bpy.data.objects["Fipi large friendly head"]
    camera.data.dof.aperture_fstop = 8
    bpy.context.scene.camera = camera

    # Render settings.
    scene = bpy.context.scene
    scene.render.resolution_x = 2042
    scene.render.resolution_y = 1674
    scene.render.film_transparent = False
    scene.render.filepath = str(PNG_PATH)
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.eevee.taa_render_samples = 96
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
        scene.eevee.use_gtao = True
        scene.eevee.gtao_distance = 3
        scene.eevee.gtao_factor = 1.3
    except Exception:
        try:
            scene.render.engine = "BLENDER_EEVEE"
        except Exception:
            scene.render.engine = "CYCLES"
            scene.cycles.samples = 72

    try:
        scene.view_settings.view_transform = "AgX"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0
        scene.view_settings.gamma = 1
    except Exception:
        pass

    # Organize naming for inspection.
    for obj in bpy.context.scene.objects:
        obj.select_set(False)


def main():
    create_scene()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    bpy.ops.render.render(write_still=True)

    # Blender builds differ on WebP support; save one when the format is available.
    try:
        bpy.context.scene.render.image_settings.file_format = "WEBP"
        bpy.context.scene.render.filepath = str(WEBP_PATH)
        bpy.ops.render.render(write_still=True)
    except Exception as exc:
        print(f"WEBP export skipped: {exc}")

    print(f"BLEND={BLEND_PATH}")
    print(f"PNG={PNG_PATH}")
    print(f"WEBP={WEBP_PATH if WEBP_PATH.exists() else 'not generated'}")


if __name__ == "__main__":
    main()
