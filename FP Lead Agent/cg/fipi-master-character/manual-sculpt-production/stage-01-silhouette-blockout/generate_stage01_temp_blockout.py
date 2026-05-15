import math
import os

import bpy
from mathutils import Vector


ROOT = r"C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character"
OUT_DIR = os.path.join(
    ROOT,
    "manual-sculpt-production",
    "stage-01-silhouette-blockout",
)
PREVIEW_DIR = os.path.join(OUT_DIR, "previews")
TURNAROUND = os.path.join(
    ROOT,
    "turnaround-references",
    "fipi_turnaround_draft_approved_2026-05-15.png",
)
PROPORTION = os.path.join(
    ROOT,
    "expression-material-stage",
    "fipi_proportion_guide_candidate.png",
)

os.makedirs(PREVIEW_DIR, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_mat(name, color, roughness=0.85, metallic=0.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat


def assign(obj, mat):
    obj.data.materials.append(mat)


def add_uv_ellipsoid(name, loc, scale, mat, segments=64, rings=32, rotation=(0, 0, 0)):
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
    try:
        bpy.ops.object.shade_smooth()
    except Exception:
        pass
    return obj


def add_text(name, text, loc, size=0.16, rotation=(0, 0, 0)):
    bpy.ops.object.text_add(location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    return obj


def add_image_plane(name, path, loc, width, mat_name):
    img = bpy.data.images.load(path, check_existing=True)
    height = width * img.size[1] / img.size[0]
    mesh = bpy.data.meshes.new(name + "_mesh")
    verts = [
        (-width / 2, -height / 2, 0),
        (width / 2, -height / 2, 0),
        (width / 2, height / 2, 0),
        (-width / 2, height / 2, 0),
    ]
    faces = [(0, 1, 2, 3)]
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for poly in mesh.polygons:
        for loop_index, uv in zip(poly.loop_indices, [(0, 0), (1, 0), (1, 1), (0, 1)]):
            uv_layer.data[loop_index].uv = uv
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
    scene.world = bpy.data.worlds.new("stage01_soft_gray_world")
    scene.world.color = (0.78, 0.78, 0.78)


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
setup_render(scene)

body_green = make_mat("stage01_body_green_placeholder", (0.45, 0.80, 0.13, 1))
belly_green = make_mat("stage01_belly_light_green_placeholder", (0.82, 0.92, 0.30, 1))
spine_blue = make_mat("stage01_spine_blue_volume_shell_placeholder", (0.0, 0.23, 0.85, 1))
dark_green = make_mat("stage01_inner_ear_shadow_placeholder", (0.24, 0.58, 0.08, 1))
eye_white = make_mat("stage01_eye_white_placement_placeholder", (0.94, 0.96, 0.94, 1))
black = make_mat("stage01_black_face_anchor_placeholder", (0.015, 0.016, 0.015, 1), roughness=0.35)
mouth = make_mat("stage01_mouth_anchor_placeholder", (0.16, 0.03, 0.02, 1), roughness=0.8)

# Character faces negative Y. Positive Y is back/spine side.
stage = bpy.data.collections.new("TEMPORARY_SCULPT_BLOCKOUT_CANDIDATE_STAGE_01_ONLY")
bpy.context.scene.collection.children.link(stage)

def move_to_stage(obj):
    for col in list(obj.users_collection):
        col.objects.unlink(obj)
    stage.objects.link(obj)
    return obj


# Core soft mascot mass.
for obj in [
    add_uv_ellipsoid("TEMP_head_body_unified_head_mass", (0, -0.02, 2.78), (1.38, 1.08, 1.18), body_green),
    add_uv_ellipsoid("TEMP_head_body_unified_torso_mass", (0, 0.02, 1.45), (1.08, 0.90, 1.25), body_green),
    add_uv_ellipsoid("TEMP_torso_only_belly_patch_mass", (0, -0.88, 1.44), (0.68, 0.045, 0.78), belly_green, 48, 24),
]:
    move_to_stage(obj)

# Ears and rough inner volume.
for side in (-1, 1):
    move_to_stage(add_uv_ellipsoid(f"TEMP_large_round_side_ear_{side}", (side * 1.18, -0.06, 2.72), (0.34, 0.22, 0.40), body_green, 48, 24))
    move_to_stage(add_uv_ellipsoid(f"TEMP_inner_ear_recess_marker_{side}", (side * 1.20, -0.22, 2.70), (0.20, 0.035, 0.25), dark_green, 32, 16))

# Limbs: short, stable, soft.
for side in (-1, 1):
    move_to_stage(add_uv_ellipsoid(f"TEMP_short_arm_mass_{side}", (side * 0.96, -0.18, 1.40), (0.25, 0.22, 0.72), body_green, 48, 24, (0, 0, math.radians(side * 8))))
    move_to_stage(add_uv_ellipsoid(f"TEMP_soft_hand_mass_{side}", (side * 0.99, -0.26, 0.84), (0.22, 0.18, 0.20), body_green, 32, 16))
    move_to_stage(add_uv_ellipsoid(f"TEMP_short_leg_mass_{side}", (side * 0.38, 0.02, 0.47), (0.30, 0.30, 0.55), body_green, 48, 24))
    move_to_stage(add_uv_ellipsoid(f"TEMP_wide_stable_foot_mass_{side}", (side * 0.38, -0.22, 0.13), (0.42, 0.46, 0.18), body_green, 48, 16))
    for toe in (-0.16, 0.0, 0.16):
        move_to_stage(add_uv_ellipsoid(f"TEMP_toe_mass_marker_{side}_{toe}", (side * (0.38 + toe), -0.54, 0.19), (0.13, 0.12, 0.10), body_green, 24, 12))

# Stage 1 spine layout: broad volume shell, not detailed strand pass.
move_to_stage(add_uv_ellipsoid("TEMP_back_spine_volume_shell_main", (0, 0.72, 2.03), (1.28, 0.50, 1.66), spine_blue, 64, 32))
move_to_stage(add_uv_ellipsoid("TEMP_left_side_spine_volume_shell", (-1.06, 0.32, 2.28), (0.32, 0.38, 1.20), spine_blue, 48, 24))
move_to_stage(add_uv_ellipsoid("TEMP_right_side_spine_volume_shell", (1.06, 0.32, 2.28), (0.32, 0.38, 1.20), spine_blue, 48, 24))
for index, (x, tilt, depth) in enumerate(
    [
        (-0.78, -28, 0.14),
        (-0.52, -18, 0.08),
        (-0.25, -8, 0.04),
        (0.0, 0, 0.02),
        (0.25, 8, 0.04),
        (0.52, 18, 0.08),
        (0.78, 28, 0.14),
    ]
):
    move_to_stage(
        add_uv_ellipsoid(
            f"TEMP_crown_spine_mass_layout_{index}",
            (x, depth, 3.64 - abs(x) * 0.10),
            (0.22, 0.30, 0.50),
            spine_blue,
            40,
            18,
            (0, math.radians(tilt), 0),
        )
    )

# Rough face placement only.
for side in (-1, 1):
    move_to_stage(add_uv_ellipsoid(f"TEMP_eye_placement_oval_{side}", (side * 0.38, -1.13, 2.82), (0.22, 0.030, 0.31), eye_white, 32, 16))
    move_to_stage(add_uv_ellipsoid(f"TEMP_pupil_placement_marker_{side}", (side * 0.39, -1.16, 2.75), (0.10, 0.015, 0.17), black, 24, 12))
move_to_stage(add_uv_ellipsoid("TEMP_small_round_nose_anchor", (0, -1.19, 2.48), (0.23, 0.09, 0.17), black, 32, 16))
move_to_stage(add_uv_ellipsoid("TEMP_open_smile_anchor_no_detail", (0, -1.12, 2.14), (0.38, 0.030, 0.16), mouth, 32, 12))

# Ground and lights.
ground_mat = make_mat("stage01_neutral_gray_ground", (0.68, 0.68, 0.66, 1))
bpy.ops.mesh.primitive_plane_add(size=7.0, location=(0, 0, -0.02))
ground = bpy.context.object
ground.name = "stage01_neutral_ground"
assign(ground, ground_mat)

bpy.ops.object.light_add(type="AREA", location=(-2.5, -4.0, 5.5))
key = bpy.context.object
key.name = "stage01_large_soft_key_light"
key.data.energy = 480
key.data.size = 5.0

bpy.ops.object.light_add(type="AREA", location=(2.5, 3.0, 4.0))
fill = bpy.context.object
fill.name = "stage01_soft_fill_light"
fill.data.energy = 95
fill.data.size = 6.0

label = add_text(
    "TEMPORARY_CANDIDATE_LABEL",
    "TEMPORARY SCULPT BLOCKOUT CANDIDATE - STAGE 1 ONLY - NOT PRODUCTION MESH",
    (0, 2.2, 4.0),
    0.13,
    (math.radians(75), 0, 0),
)
move_to_stage(label)
label.hide_render = True

bpy.context.scene["stage_status"] = "temporary sculpt blockout candidate"
bpy.context.scene["not_final"] = "Not production topology, not approved master, no retopo/UV/material/rig/detail pass."
bpy.context.scene["stage_scope"] = "Stage 1 silhouette/proportion/blockout only."

front_path = os.path.join(PREVIEW_DIR, "fipi_stage01_silhouette_front.png")
side_path = os.path.join(PREVIEW_DIR, "fipi_stage01_silhouette_side.png")
back_path = os.path.join(PREVIEW_DIR, "fipi_stage01_silhouette_back.png")

set_camera("stage01_camera_front", (0, -7, 2.05), (0, 0, 2.05), 5.15, front_path)
set_camera("stage01_camera_side", (-7, 0, 2.05), (0, 0, 2.05), 5.15, side_path)
set_camera("stage01_camera_back", (0, 7, 2.05), (0, 0, 2.05), 5.15, back_path)

# Comparison board using approved references plus generated previews.
board_scene = bpy.data.scenes.new("STAGE_01_REFERENCE_COMPARISON_BOARD")
bpy.context.window.scene = board_scene
setup_render(board_scene, 2400, 1500)

board_world = bpy.data.worlds.new("comparison_board_world")
board_world.color = (0.86, 0.86, 0.84)
board_scene.world = board_world

add_image_plane("approved_turnaround_reference", TURNAROUND, (-3.0, 1.45, 0), 3.85, "mat_approved_turnaround")
add_image_plane("approved_proportion_guide", PROPORTION, (-3.0, -1.55, 0), 3.85, "mat_approved_proportion")
add_image_plane("candidate_front_preview", front_path, (1.05, 1.25, 0), 1.35, "mat_candidate_front")
add_image_plane("candidate_side_preview", side_path, (2.60, 1.25, 0), 1.35, "mat_candidate_side")
add_image_plane("candidate_back_preview", back_path, (4.15, 1.25, 0), 1.35, "mat_candidate_back")

add_text("board_title", "Stage 1 silhouette comparison: approved references vs temporary blockout candidate", (0.25, 3.0, 0.02), 0.16)
add_text("board_ref_label", "Approved turnaround / proportion guide", (-3.0, 2.62, 0.02), 0.12)
add_text("board_candidate_label", "Temporary candidate renders - front / side / back", (2.6, 2.32, 0.02), 0.12)
add_text("board_warning", "Not production mesh. No face detail, spine detail, retopo, UV, materials, rig, or animation.", (2.6, -0.12, 0.02), 0.10)

bpy.ops.object.light_add(type="AREA", location=(0, -3, 4))
board_light = bpy.context.object
board_light.name = "comparison_board_soft_light"
board_light.data.energy = 260
board_light.data.size = 7

cam_data = bpy.data.cameras.new("comparison_board_camera")
cam = bpy.data.objects.new("comparison_board_camera", cam_data)
board_scene.collection.objects.link(cam)
cam.location = (0.0, 0, 7.0)
cam.rotation_euler = (0, 0, 0)
cam.data.type = "ORTHO"
cam.data.ortho_scale = 6.6
board_scene.camera = cam
board_scene.render.filepath = os.path.join(PREVIEW_DIR, "fipi_stage01_reference_comparison.png")
bpy.ops.render.render(write_still=True)

bpy.context.window.scene = scene
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "fipi_stage01_blockout.blend"))
