import math
import os
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parent
PREVIEW_DIR = ROOT / "previews"
PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

BLEND_PATH = ROOT / "fipi_blockout.blend"
FRONT_PATH = PREVIEW_DIR / "fipi_blockout_front.png"
COMPARISON_PATH = PREVIEW_DIR / "fipi_blockout_reference_comparison.png"

REFERENCE_PATH = Path(
    r"C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\reference\fipi_master_reference.png"
)


def clean_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for block in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.images,
        bpy.data.curves,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for item in list(block):
            if item.users == 0:
                block.remove(item)


def mat(name, color, roughness=0.72, metallic=0.0, specular=0.25):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Alpha"].default_value = color[3]
        if "Specular IOR Level" in bsdf.inputs:
            bsdf.inputs["Specular IOR Level"].default_value = specular
        elif "Specular" in bsdf.inputs:
            bsdf.inputs["Specular"].default_value = specular
    return material


def assign(obj, material):
    obj.data.materials.append(material)
    return obj


def shade(obj, subdiv=1):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    try:
        bpy.ops.object.shade_smooth()
    except RuntimeError:
        pass
    obj.select_set(False)
    if subdiv:
        mod = obj.modifiers.new("blockout_smoothing_subdivision", "SUBSURF")
        mod.levels = subdiv
        mod.render_levels = subdiv
    return obj


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_uv_ellipsoid(name, loc, scale, material, segments=64, rings=32, subdiv=1):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    assign(obj, material)
    return shade(obj, subdiv=subdiv)


def add_capsule(name, start, end, radius, material, subdiv=1):
    start = Vector(start)
    end = Vector(end)
    mid = (start + end) * 0.5
    length = (end - start).length
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=radius, depth=length, location=mid)
    cyl = bpy.context.object
    cyl.name = f"{name}_soft_limb"
    cyl.rotation_euler = (end - start).to_track_quat("Z", "Y").to_euler()
    assign(cyl, material)
    shade(cyl, subdiv=subdiv)
    add_uv_ellipsoid(f"{name}_rounded_shoulder_end", start, (radius, radius, radius), material, 32, 16, subdiv)
    add_uv_ellipsoid(f"{name}_rounded_wrist_end", end, (radius, radius, radius), material, 32, 16, subdiv)
    return cyl


def create_spine_mesh(name, length=0.92, width=0.15, depth=0.13, rings=18, segments=24):
    verts = []
    faces = []
    for i in range(rings + 1):
        v = i / rings
        y = (v - 0.5) * length
        # Rounded plush strand: fuller than a spike, slimmer than a petal.
        profile = math.sin(math.pi * v) ** 0.42
        taper = 1.0 - 0.34 * max(0.0, v - 0.45)
        r_x = width * profile * taper
        r_z = depth * profile * (1.05 - 0.25 * v)
        for j in range(segments):
            a = 2.0 * math.pi * j / segments
            verts.append((math.cos(a) * r_x, y, math.sin(a) * r_z))
    for i in range(rings):
        for j in range(segments):
            a = i * segments + j
            b = i * segments + (j + 1) % segments
            c = (i + 1) * segments + (j + 1) % segments
            d = (i + 1) * segments + j
            faces.append((a, b, c, d))
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    return mesh


def add_spine(name, loc, rot, scale, material):
    mesh = create_spine_mesh(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = loc
    obj.rotation_euler = rot
    obj.scale = scale
    assign(obj, material)
    shade(obj, subdiv=1)
    return obj


def add_curve_arc(name, points, bevel_depth, material, resolution=5):
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 16
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = resolution
    spline = curve.splines.new("BEZIER")
    spline.bezier_points.add(len(points) - 1)
    for point, co in zip(spline.bezier_points, points):
        point.co = Vector(co)
        point.handle_left_type = "AUTO"
        point.handle_right_type = "AUTO"
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def build_character(materials):
    green = materials["body_green"]
    belly = materials["belly_light_green"]
    blue = materials["spines_blue"]
    white = materials["eyes_white"]
    black = materials["eyes_black"]
    highlight = materials["eye_highlights"]
    mouth_dark = materials["mouth_dark"]
    tongue = materials["tongue_pink"]
    inner_ear = materials["inner_ear_green"]
    brow = materials["brow_blue_green"]

    # Unified mascot mass: body and face overlap deeply so the top reads as one soft character volume.
    add_uv_ellipsoid("body_unified_soft_torso_green", (0, 0, 1.46), (0.92, 0.66, 1.22), green, subdiv=2)
    add_uv_ellipsoid("upper_face_broad_blended_green", (0, -0.045, 2.43), (0.94, 0.64, 0.66), green, subdiv=2)
    add_uv_ellipsoid("soft_head_to_body_blend_volume", (0, -0.02, 2.08), (0.86, 0.58, 0.45), green, subdiv=2)

    # Belly patch only on torso. It is a raised oval volume, not a face mask.
    add_uv_ellipsoid("torso_only_raised_oval_belly_patch", (0, -0.69, 1.45), (0.58, 0.075, 0.73), belly, 64, 24, 1)

    # Ears with inner bowl indication.
    for side, sx in (("left", -1), ("right", 1)):
        ear = add_uv_ellipsoid(f"{side}_large_round_green_ear", (sx * 0.9, -0.03, 2.65), (0.26, 0.18, 0.32), green, 48, 20, 1)
        ear.rotation_euler[1] = math.radians(0)
        inner = add_uv_ellipsoid(f"{side}_recessed_inner_ear_bowl", (sx * 0.93, -0.16, 2.65), (0.15, 0.045, 0.21), inner_ear, 32, 14, 1)
        inner.rotation_euler[2] = math.radians(sx * 6)

    # Face: large oval eyes, close glossy nose, open dimensional smile.
    for side, sx in (("left", -1), ("right", 1)):
        eye = add_uv_ellipsoid(f"{side}_large_vertical_white_eye", (sx * 0.31, -0.675, 2.55), (0.18, 0.044, 0.255), white, 48, 20, 1)
        eye.rotation_euler[2] = 0
        pupil = add_uv_ellipsoid(f"{side}_large_black_pupil_inside_eye", (sx * 0.315, -0.718, 2.52), (0.092, 0.02, 0.145), black, 32, 16, 1)
        pupil.rotation_euler[2] = 0
        add_uv_ellipsoid(f"{side}_eye_white_catchlight", (sx * 0.36, -0.736, 2.61), (0.032, 0.009, 0.045), highlight, 24, 10, 0)
        add_curve_arc(
            f"{side}_short_soft_bluegreen_brow",
            [(sx * 0.2, -0.73, 2.84), (sx * 0.33, -0.755, 2.9), (sx * 0.48, -0.73, 2.88)],
            0.014,
            brow,
        )

    add_uv_ellipsoid("small_glossy_black_round_nose", (0, -0.748, 2.38), (0.12, 0.082, 0.105), black, 48, 20, 1)
    add_curve_arc("subtle_dark_muzzle_split_below_nose", [(0, -0.793, 2.32), (0, -0.805, 2.25)], 0.004, mouth_dark, 2)
    add_uv_ellipsoid("open_happy_smile_dark_mouth_cavity", (0, -0.79, 2.18), (0.255, 0.028, 0.14), mouth_dark, 48, 14, 1)
    add_uv_ellipsoid("visible_soft_tongue_inside_open_smile", (0.025, -0.812, 2.095), (0.145, 0.016, 0.048), tongue, 32, 12, 0)

    # Raised arms and readable hands/fingers.
    arm_data = [
        ("left", -1, (-0.7, -0.02, 1.98), (-1.22, -0.31, 2.8)),
        ("right", 1, (0.7, -0.02, 1.98), (1.22, -0.31, 2.8)),
    ]
    for side, sx, shoulder, wrist in arm_data:
        add_capsule(f"{side}_raised_tapered_arm", shoulder, wrist, 0.14, green, 1)
        palm = add_uv_ellipsoid(f"{side}_rounded_open_palm", wrist, (0.18, 0.09, 0.19), green, 32, 16, 1)
        palm.rotation_euler[2] = math.radians(sx * 18)
        fan_angles = [-0.2, -0.06, 0.08, 0.22]
        for i, offset in enumerate(fan_angles):
            finger_base = Vector(wrist) + Vector((sx * 0.035, -0.035, offset * 0.62))
            finger_tip = finger_base + Vector((sx * (0.13 + abs(offset) * 0.08), -0.055, 0.12 + offset * 0.35))
            add_capsule(f"{side}_soft_fanned_finger_{i+1}", finger_base, finger_tip, 0.045, green, 0)
        thumb_base = Vector(wrist) + Vector((sx * -0.04, -0.035, -0.03))
        thumb_tip = thumb_base + Vector((sx * -0.14, -0.055, 0.055))
        add_capsule(f"{side}_rounded_opposable_thumb", thumb_base, thumb_tip, 0.048, green, 0)

    # Short sturdy legs, wide feet, toe bumps.
    for side, sx in (("left", -1), ("right", 1)):
        add_capsule(f"{side}_short_sturdy_leg", (sx * 0.38, -0.03, 0.66), (sx * 0.45, -0.06, 0.22), 0.18, green, 1)
        foot = add_uv_ellipsoid(f"{side}_wide_soft_foot", (sx * 0.48, -0.24, 0.18), (0.32, 0.25, 0.13), green, 40, 14, 1)
        foot.rotation_euler[2] = math.radians(sx * 3)
        for i, toe_x in enumerate([-0.12, 0.0, 0.12]):
            add_uv_ellipsoid(
                f"{side}_rounded_front_toe_{i+1}",
                (sx * (0.48 + toe_x), -0.43, 0.24),
                (0.075, 0.055, 0.055),
                green,
                24,
                10,
                0,
            )

    # Blue plush spine masses: crown crest, side rows, and rear/back continuation.
    crown_specs = [
        (-0.62, 0.1, 2.9, -35, 18, 0.68),
        (-0.48, 0.16, 3.02, -27, 14, 0.78),
        (-0.32, 0.2, 3.1, -18, 10, 0.86),
        (-0.14, 0.23, 3.14, -7, 4, 0.9),
        (0.05, 0.24, 3.15, 3, -2, 0.9),
        (0.24, 0.21, 3.11, 14, -7, 0.86),
        (0.42, 0.16, 3.02, 25, -12, 0.76),
        (0.58, 0.09, 2.9, 35, -18, 0.66),
    ]
    for idx, (x, y, z, rz, rx, s) in enumerate(crown_specs, 1):
        add_spine(
            f"crown_soft_blue_spine_lobe_{idx}",
            (x, y, z),
            (math.radians(78 + rx), 0, math.radians(rz)),
            (0.95 * s, 1.0 * s, 0.95 * s),
            blue,
        )

    side_specs = []
    for row, z in enumerate([2.72, 2.46, 2.2, 1.92, 1.64, 1.36]):
        width = 0.78 + 0.035 * row
        for sx in (-1, 1):
            side_specs.append((sx * width, 0.32 + 0.03 * row, z, sx, row))
    for idx, (x, y, z, sx, row) in enumerate(side_specs, 1):
        add_spine(
            f"side_back_soft_blue_spine_mass_{idx}",
            (x, y, z),
            (math.radians(80), math.radians(sx * 14), math.radians(sx * (58 + row * 3))),
            (0.58 - row * 0.018, 0.7 - row * 0.018, 0.62),
            blue,
        )

    for idx, z in enumerate([2.84, 2.62, 2.38, 2.12, 1.86, 1.6, 1.35, 1.14], 1):
        add_spine(
            f"visible_center_back_blue_spine_stack_{idx}",
            (0, 0.51, z),
            (math.radians(95), 0, 0),
            (0.5 - idx * 0.012, 0.68 - idx * 0.012, 0.55),
            blue,
        )

    # Non-rendering guide labels as empty object names only: useful for FP review inside blend.
    empty = bpy.data.objects.new("SCOPE_NOTE_blockout_only_no_rig_no_final_textures", None)
    bpy.context.collection.objects.link(empty)


def setup_lighting_and_camera():
    bpy.ops.object.light_add(type="AREA", location=(-3.0, -4.0, 6.0))
    key = bpy.context.object
    key.name = "large_softbox_key_light"
    key.data.energy = 480
    key.data.size = 4.5

    bpy.ops.object.light_add(type="POINT", location=(2.8, 1.7, 3.0))
    fill = bpy.context.object
    fill.name = "small_back_rim_for_spine_readability"
    fill.data.energy = 80

    bpy.ops.object.camera_add(location=(0, -8.6, 2.05), rotation=(math.radians(78), 0, 0))
    cam = bpy.context.object
    cam.name = "front_review_camera"
    cam.data.lens = 43
    cam.data.sensor_width = 32
    look_at(cam, (0, -0.15, 1.8))
    bpy.context.scene.camera = cam

    world = bpy.context.scene.world or bpy.data.worlds.new("World")
    bpy.context.scene.world = world
    world.color = (1, 1, 1)


def render_front():
    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    if hasattr(bpy.context.scene, "eevee"):
        bpy.context.scene.eevee.taa_render_samples = 64
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 1800
    bpy.context.scene.render.film_transparent = False
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.render.filepath = str(FRONT_PATH)
    bpy.ops.render.render(write_still=True)


def make_comparison():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    def image_plane(name, image_path, center_x, max_w=4.3, max_h=5.35):
        image = bpy.data.images.load(str(image_path))
        aspect = image.size[0] / image.size[1]
        if aspect >= max_w / max_h:
            width = max_w
            height = max_w / aspect
        else:
            height = max_h
            width = max_h * aspect
        bpy.ops.mesh.primitive_plane_add(size=1, location=(center_x, 0, 0))
        plane = bpy.context.object
        plane.name = name
        plane.rotation_euler[0] = math.radians(90)
        plane.dimensions = (width, height, 1)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        material = bpy.data.materials.new(f"{name}_image_material")
        material.use_nodes = True
        nodes = material.node_tree.nodes
        bsdf = nodes.get("Principled BSDF")
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = image
        if bsdf:
            material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Base Color"])
            bsdf.inputs["Roughness"].default_value = 0.55
        plane.data.materials.append(material)
        return plane

    image_plane("comparison_left_canonical_reference_image", REFERENCE_PATH, -2.55)
    image_plane("comparison_right_blockout_preview_image", FRONT_PATH, 2.55)

    font_curve = bpy.ops.object.text_add
    font_curve(location=(-2.55, 0, 2.95), rotation=(math.radians(90), 0, 0))
    left_text = bpy.context.object
    left_text.name = "comparison_label_canonical_reference"
    left_text.data.body = "Canonical reference"
    left_text.data.align_x = "CENTER"
    left_text.data.size = 0.18
    font_curve(location=(2.55, 0, 2.95), rotation=(math.radians(90), 0, 0))
    right_text = bpy.context.object
    right_text.name = "comparison_label_manual_blockout"
    right_text.data.body = "Manual sculpt blockout"
    right_text.data.align_x = "CENTER"
    right_text.data.size = 0.18

    bpy.ops.object.light_add(type="AREA", location=(0, -2.5, 4))
    light = bpy.context.object
    light.data.energy = 260
    light.data.size = 6
    bpy.ops.object.camera_add(location=(0, -7.0, 0.25))
    cam = bpy.context.object
    cam.name = "comparison_render_camera"
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 6.35
    look_at(cam, (0, 0, 0.15))
    bpy.context.scene.camera = cam
    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.render.resolution_x = 1800
    bpy.context.scene.render.resolution_y = 1250
    bpy.context.scene.render.filepath = str(COMPARISON_PATH)
    bpy.context.scene.world.color = (0.95, 0.965, 0.98)
    bpy.ops.render.render(write_still=True)


def write_handoff():
    handoff = ROOT / "BLOCKOUT_HANDOFF.md"
    handoff.write_text(
        "\n".join(
            [
                "Status:",
                "Manual sculpt blockout revision v2 created from reference pack after FP Lead rejection of v1. This is not a final render, rig, animation, UV, or full material pass.",
                "",
                f"Preview saved: {FRONT_PATH}",
                f"Comparison saved: {COMPARISON_PATH}",
                f"Blend saved: {BLEND_PATH}",
                f"Handoff saved: {handoff}",
                "",
                "What matches:",
                "- v2 reduces the separate head-ball feeling by lowering and blending the upper face volume into the torso.",
                "- Green face remains fully green; light belly patch is restricted to the torso only.",
                "- Cheek spots/cheek patches from v1 were removed.",
                "- Eyes were rebuilt as larger upright white ovals with black pupils and catchlights.",
                "- Nose was reduced; mouth was simplified toward an open happy smile with dark cavity and tongue.",
                "- Blue spine masses are smaller, denser, and closer to soft strands than the v1 petal shapes.",
                "- Raised arms include palms, separate thumb shapes, and softer fanned fingers.",
                "- Short sturdy legs, wide feet, and toe bumps are present.",
                "- Materials are simple color guides only, matching the reference swatches for readability.",
                "",
                "What does not match yet:",
                "- Scripted Blender primitives still cannot fully recover the canonical facial identity; a human Blender sculpt-mode pass is needed.",
                "- The open smile, eye curvature, and muzzle softness need hand sculpting to match the reference character expression.",
                "- Head/body merge is improved but still needs organic sculpt cleanup.",
                "- Spines are denser than v1 but remain separate blockout strands and need manual sculpt/retopo for true plush needle forms.",
                "- Hands are softer than v1 but still primitive; finger fan/palm silhouette needs artist pass.",
                "- No final topology, UVs, rig, facial controls, or PBR plush material pass has been attempted.",
                "",
                "Verdict:",
                "- not ready, needs blockout revision",
                "",
                "Decision needed from FP Lead:",
                "- approve blockout direction / revise blockout",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return handoff


def main():
    clean_scene()
    materials = {
        "body_green": mat("body_green_blockout_74CD26", (0.455, 0.804, 0.149, 1), 0.84, specular=0.18),
        "belly_light_green": mat("belly_light_green_blockout_D5E95B", (0.835, 0.914, 0.357, 1), 0.86, specular=0.16),
        "spines_blue": mat("spines_blue_blockout_0054C4", (0.0, 0.329, 0.769, 1), 0.78, specular=0.22),
        "eyes_white": mat("eyes_white_blockout", (0.97, 0.965, 0.93, 1), 0.28, specular=0.45),
        "eyes_black": mat("glossy_black_nose_pupils_blockout", (0.006, 0.007, 0.007, 1), 0.18, specular=0.7),
        "eye_highlights": mat("eye_highlights_white_blockout", (1, 1, 1, 1), 0.15, specular=0.8),
        "mouth_dark": mat("mouth_dark_blockout_2D0808", (0.176, 0.031, 0.031, 1), 0.45, specular=0.2),
        "tongue_pink": mat("tongue_pink_blockout_E25744", (0.886, 0.341, 0.267, 1), 0.55, specular=0.2),
        "inner_ear_green": mat("inner_ear_green_recess_blockout", (0.56, 0.86, 0.22, 1), 0.86, specular=0.12),
        "brow_blue_green": mat("brow_dark_blue_green_blockout", (0.02, 0.17, 0.13, 1), 0.7, specular=0.12),
    }
    build_character(materials)
    setup_lighting_and_camera()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    render_front()
    make_comparison()
    handoff = write_handoff()
    print(f"Preview saved: {FRONT_PATH}")
    print(f"Comparison saved: {COMPARISON_PATH}")
    print(f"Blend saved: {BLEND_PATH}")
    print(f"Handoff saved: {handoff}")


if __name__ == "__main__":
    main()
