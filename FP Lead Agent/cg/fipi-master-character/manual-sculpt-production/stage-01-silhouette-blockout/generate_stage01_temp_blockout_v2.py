import math
import os

import bpy
from mathutils import Vector


ROOT = r"C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character"
OUT_DIR = os.path.join(ROOT, "manual-sculpt-production", "stage-01-silhouette-blockout")
PREVIEW_DIR = os.path.join(OUT_DIR, "previews")
TURNAROUND = os.path.join(ROOT, "turnaround-references", "fipi_turnaround_draft_approved_2026-05-15.png")
PROPORTION = os.path.join(ROOT, "expression-material-stage", "fipi_proportion_guide_candidate.png")

os.makedirs(PREVIEW_DIR, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_mat(name, color, roughness=0.8):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    return mat


def assign(obj, mat):
    obj.data.materials.append(mat)


def ellipsoid(name, loc, scale, mat, segments=64, rings=32, rotation=(0, 0, 0), collection=None):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=segments,
        ring_count=rings,
        radius=1.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    assign(obj, mat)
    bpy.ops.object.shade_smooth()
    if collection:
        for col in list(obj.users_collection):
            col.objects.unlink(obj)
        collection.objects.link(obj)
    return obj


def add_text(name, text, loc, size=0.16, rotation=(0, 0, 0), collection=None):
    bpy.ops.object.text_add(location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    if collection:
        for col in list(obj.users_collection):
            col.objects.unlink(obj)
        collection.objects.link(obj)
    return obj


def image_plane(name, path, loc, width, mat_name):
    img = bpy.data.images.load(path, check_existing=True)
    height = width * img.size[1] / img.size[0]
    mesh = bpy.data.meshes.new(name + "_mesh")
    verts = [
        (-width / 2, -height / 2, 0),
        (width / 2, -height / 2, 0),
        (width / 2, height / 2, 0),
        (-width / 2, height / 2, 0),
    ]
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for poly in mesh.polygons:
        for loop_index, uv in zip(poly.loop_indices, [(0, 0), (1, 0), (1, 1), (0, 1)]):
            uv_layer.data[loop_index].uv = uv
    mesh.update()

    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = loc

    mat = bpy.data.materials.new(mat_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    tex = nodes.new("ShaderNodeTexImage")
    tex.image = img
    mat.node_tree.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 1.0
    obj.data.materials.append(mat)
    return obj


def setup_render(scene, res_x=1600, res_y=1600):
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = res_x
    scene.render.resolution_y = res_y
    scene.eevee.taa_render_samples = 64
    scene.view_settings.view_transform = "Filmic"
    scene.view_settings.look = "Medium High Contrast"
    scene.world = bpy.data.worlds.new(scene.name + "_world")
    scene.world.color = (0.76, 0.76, 0.74)


def set_camera(name, loc, target, ortho, filepath):
    cam_data = bpy.data.cameras.new(name)
    cam = bpy.data.objects.new(name, cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = loc
    direction = Vector(target) - Vector(loc)
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = ortho
    bpy.context.scene.camera = cam
    bpy.context.scene.render.filepath = filepath
    bpy.ops.render.render(write_still=True)
    return cam


clear_scene()
scene = bpy.context.scene
scene.name = "STAGE_01_TEMPORARY_BLOCKOUT_V2"
setup_render(scene)

stage = bpy.data.collections.new("TEMPORARY_SCULPT_BLOCKOUT_CANDIDATE_STAGE_01_V2_ONLY")
bpy.context.scene.collection.children.link(stage)

body_green = make_mat("stage01_v2_body_green_placeholder", (0.46, 0.81, 0.13, 1))
belly_green = make_mat("stage01_v2_belly_light_green_placeholder", (0.82, 0.91, 0.32, 1))
spine_blue = make_mat("stage01_v2_layered_spine_mass_placeholder", (0.0, 0.25, 0.86, 1))
dark_green = make_mat("stage01_v2_inner_ear_recess_placeholder", (0.24, 0.56, 0.08, 1))
eye_white = make_mat("stage01_v2_eye_placement_placeholder", (0.94, 0.96, 0.94, 1))
black = make_mat("stage01_v2_black_anchor_placeholder", (0.018, 0.018, 0.016, 1), 0.35)
mouth = make_mat("stage01_v2_mouth_anchor_placeholder", (0.18, 0.035, 0.025, 1), 0.8)

# Green unified plush volume. The larger lower head overlap reduces the separate ball/capsule read.
ellipsoid("TEMP_v2_unified_head_upper_mass", (0, -0.08, 2.78), (1.30, 1.02, 1.02), body_green, collection=stage)
ellipsoid("TEMP_v2_soft_lower_face_to_torso_bridge", (0, -0.04, 2.10), (1.08, 0.90, 0.78), body_green, collection=stage)
ellipsoid("TEMP_v2_rounded_torso_belly_mass", (0, 0.02, 1.28), (0.96, 0.82, 0.98), body_green, collection=stage)
ellipsoid("TEMP_v2_torso_only_belly_patch_soft_oval", (0, -0.84, 1.33), (0.58, 0.040, 0.64), belly_green, 48, 24, collection=stage)

# Large side ears with a soft inset marker, aligned to approved eye/head band.
for side in (-1, 1):
    ellipsoid(f"TEMP_v2_large_round_side_ear_{side}", (side * 1.12, -0.05, 2.67), (0.34, 0.23, 0.38), body_green, 48, 24, collection=stage)
    ellipsoid(f"TEMP_v2_inner_ear_mass_marker_{side}", (side * 1.14, -0.22, 2.66), (0.20, 0.035, 0.23), dark_green, 32, 16, collection=stage)

# Short arms with three-finger hand masses, closer to the turnaround than v1 blob hands.
for side in (-1, 1):
    ellipsoid(
        f"TEMP_v2_short_soft_arm_{side}",
        (side * 0.88, -0.14, 1.27),
        (0.20, 0.18, 0.58),
        body_green,
        48,
        24,
        (0, 0, math.radians(side * 7)),
        stage,
    )
    ellipsoid(f"TEMP_v2_palm_mass_{side}", (side * 0.91, -0.26, 0.79), (0.17, 0.13, 0.16), body_green, 32, 16, collection=stage)
    for index, offset in enumerate((-0.11, 0.0, 0.11)):
        ellipsoid(
            f"TEMP_v2_hand_finger_mass_{side}_{index}",
            (side * (0.90 + offset), -0.36, 0.82 - abs(offset) * 0.18),
            (0.065, 0.07, 0.13),
            body_green,
            24,
            12,
            collection=stage,
        )

# Legs and feet: lower, wider, with visible toe massing instead of a single blob.
for side in (-1, 1):
    ellipsoid(f"TEMP_v2_short_stable_leg_{side}", (side * 0.34, 0.02, 0.44), (0.26, 0.25, 0.47), body_green, 40, 18, collection=stage)
    ellipsoid(f"TEMP_v2_flat_wide_foot_base_{side}", (side * 0.36, -0.22, 0.12), (0.34, 0.39, 0.14), body_green, 40, 16, collection=stage)
    for index, offset in enumerate((-0.16, 0.0, 0.16)):
        ellipsoid(
            f"TEMP_v2_foot_toe_mass_{side}_{index}",
            (side * (0.36 + offset), -0.50, 0.19),
            (0.105, 0.105, 0.085),
            body_green,
            24,
            12,
            collection=stage,
        )

# Layered spine massing. These are intentionally broad layout masses, not final detailed plastic leaves.
# Back rows are staggered vertically to read like the approved shell silhouette without using one smooth shell.
rows = [
    (3.18, 5, 0.72, 0.32, 0.32),
    (2.76, 6, 0.88, 0.34, 0.42),
    (2.32, 6, 0.98, 0.36, 0.50),
    (1.88, 5, 0.82, 0.34, 0.56),
    (1.46, 4, 0.58, 0.31, 0.54),
    (1.10, 3, 0.34, 0.27, 0.46),
]
for row_index, (z, count, half_width, sx, sy) in enumerate(rows):
    for i in range(count):
        x = 0 if count == 1 else -half_width + (2 * half_width) * i / (count - 1)
        y = 0.57 + row_index * 0.015 + abs(x) * 0.07
        tilt_y = math.radians(-x * 13)
        tilt_x = math.radians(8 + row_index * 3)
        ellipsoid(
            f"TEMP_v2_layered_back_spine_mass_r{row_index}_{i}",
            (x, y, z - abs(x) * 0.12),
            (sx, sy, 0.40 + row_index * 0.035),
            spine_blue,
            40,
            18,
            (tilt_x, tilt_y, 0),
            stage,
        )

# Crown fan reads from the front as separate rounded spine masses.
for i, x in enumerate([-0.72, -0.48, -0.24, 0.0, 0.24, 0.48, 0.72]):
    ellipsoid(
        f"TEMP_v2_crown_spine_mass_{i}",
        (x, 0.02 + abs(x) * 0.08, 3.55 - abs(x) * 0.05),
        (0.20, 0.26, 0.46),
        spine_blue,
        40,
        18,
        (math.radians(4), math.radians(-x * 18), 0),
        stage,
    )

# Side spine row silhouette visible from front/side.
for side in (-1, 1):
    for i, (z, y, sx, sz) in enumerate([(2.85, 0.42, 0.22, 0.42), (2.38, 0.52, 0.24, 0.52), (1.92, 0.58, 0.22, 0.48), (1.48, 0.58, 0.19, 0.38)]):
        ellipsoid(
            f"TEMP_v2_side_spine_mass_{side}_{i}",
            (side * (1.02 + i * 0.015), y, z),
            (sx, 0.28, sz),
            spine_blue,
            36,
            16,
            (math.radians(8), math.radians(side * 18), 0),
            stage,
        )

# Rough face placement only; no identity/detail pass.
for side in (-1, 1):
    ellipsoid(f"TEMP_v2_eye_position_marker_{side}", (side * 0.36, -1.05, 2.73), (0.19, 0.026, 0.27), eye_white, 32, 16, collection=stage)
    ellipsoid(f"TEMP_v2_pupil_position_marker_{side}", (side * 0.37, -1.08, 2.68), (0.078, 0.014, 0.145), black, 24, 12, collection=stage)
ellipsoid("TEMP_v2_small_round_nose_anchor", (0, -1.10, 2.42), (0.20, 0.085, 0.145), black, 32, 16, collection=stage)
ellipsoid("TEMP_v2_smile_opening_anchor_no_detail", (0, -1.05, 2.16), (0.31, 0.026, 0.12), mouth, 32, 12, collection=stage)

ground_mat = make_mat("stage01_v2_neutral_gray_ground", (0.68, 0.68, 0.66, 1))
bpy.ops.mesh.primitive_plane_add(size=7.0, location=(0, 0, -0.02))
ground = bpy.context.object
ground.name = "stage01_v2_neutral_ground"
assign(ground, ground_mat)

bpy.ops.object.light_add(type="AREA", location=(-2.4, -4.0, 5.5))
key = bpy.context.object
key.name = "stage01_v2_large_soft_key_light"
key.data.energy = 520
key.data.size = 5.5

bpy.ops.object.light_add(type="AREA", location=(2.7, 3.1, 4.2))
fill = bpy.context.object
fill.name = "stage01_v2_soft_fill_light"
fill.data.energy = 125
fill.data.size = 6.0

label = add_text(
    "TEMPORARY_CANDIDATE_LABEL_V2",
    "TEMPORARY SCULPT BLOCKOUT CANDIDATE V2 - STAGE 1 ONLY - NOT PRODUCTION MESH",
    (0, 2.1, 4.1),
    0.13,
    (math.radians(75), 0, 0),
    stage,
)
label.hide_render = True

scene["stage_status"] = "temporary sculpt blockout candidate v2"
scene["not_final"] = "Not production topology, not approved master, no retopo/UV/material/rig/detail pass."
scene["stage_scope"] = "Stage 1 silhouette/proportion/blockout revision only."
scene["revision_focus"] = "Closer approved turnaround proportions, layered soft spine masses, less generic hands/feet."

front_path = os.path.join(PREVIEW_DIR, "fipi_stage01_silhouette_front_v2.png")
side_path = os.path.join(PREVIEW_DIR, "fipi_stage01_silhouette_side_v2.png")
back_path = os.path.join(PREVIEW_DIR, "fipi_stage01_silhouette_back_v2.png")

set_camera("stage01_v2_camera_front", (0, -7, 2.05), (0, 0, 2.05), 4.75, front_path)
set_camera("stage01_v2_camera_side", (-7, 0, 2.05), (0, 0, 2.05), 4.75, side_path)
set_camera("stage01_v2_camera_back", (0, 7, 2.05), (0, 0, 2.05), 4.75, back_path)

# Blender-native comparison board is stored in the .blend for context. Final PNG comparison is composed separately.
board_scene = bpy.data.scenes.new("STAGE_01_REFERENCE_COMPARISON_BOARD_V2")
bpy.context.window.scene = board_scene
setup_render(board_scene, 2400, 1500)
image_plane("approved_turnaround_reference_v2", TURNAROUND, (-3.0, 1.45, 0), 3.85, "mat_approved_turnaround_v2")
image_plane("approved_proportion_guide_v2", PROPORTION, (-3.0, -1.55, 0), 3.85, "mat_approved_proportion_v2")
image_plane("candidate_front_preview_v2", front_path, (1.05, 1.25, 0), 1.35, "mat_candidate_front_v2")
image_plane("candidate_side_preview_v2", side_path, (2.60, 1.25, 0), 1.35, "mat_candidate_side_v2")
image_plane("candidate_back_preview_v2", back_path, (4.15, 1.25, 0), 1.35, "mat_candidate_back_v2")
add_text("board_title_v2", "Stage 1 v2 silhouette comparison - temporary blockout only", (0.25, 3.0, 0.02), 0.16)

bpy.ops.object.light_add(type="AREA", location=(0, -3, 4))
board_light = bpy.context.object
board_light.name = "comparison_board_v2_soft_light"
board_light.data.energy = 260
board_light.data.size = 7

cam_data = bpy.data.cameras.new("comparison_board_v2_camera")
cam = bpy.data.objects.new("comparison_board_v2_camera", cam_data)
board_scene.collection.objects.link(cam)
cam.location = (0.0, 0, 7.0)
cam.rotation_euler = (0, 0, 0)
cam.data.type = "ORTHO"
cam.data.ortho_scale = 6.6
board_scene.camera = cam

bpy.context.window.scene = scene
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "fipi_stage01_blockout_v2.blend"))
