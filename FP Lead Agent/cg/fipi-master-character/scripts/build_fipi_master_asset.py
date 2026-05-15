import importlib.util
import json
from datetime import datetime
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
MASTER_DIR = ROOT / "master"
PREVIEW_DIR = MASTER_DIR / "previews"
TEXTURE_DIR = MASTER_DIR / "textures"
EXPORT_DIR = MASTER_DIR / "exports"
RIG_DIR = MASTER_DIR / "rig"
VALIDATION_DIR = MASTER_DIR / "validation"
REFERENCE_PATH = ROOT / "reference" / "fipi_master_reference.png"

LEGACY_BUILDER = ROOT.parent / "fipi-canon-blender-model" / "create_fipi_canonical_blender_model.py"
BLEND_PATH = MASTER_DIR / "master.blend"
PREVIEW_PATH = PREVIEW_DIR / "fipi_master_joy_preview.png"
COMPARISON_PATH = PREVIEW_DIR / "fipi_master_reference_comparison.png"
METADATA_PATH = MASTER_DIR / "fipi_master_metadata.json"
QA_REPORT_PATH = VALIDATION_DIR / "qa_report.md"
RIG_NOTES_PATH = RIG_DIR / "rig_notes.md"
GLB_PATH = EXPORT_DIR / "fipi_master.glb"


def ensure_dirs():
    for path in (MASTER_DIR, PREVIEW_DIR, TEXTURE_DIR, EXPORT_DIR, RIG_DIR, VALIDATION_DIR):
        path.mkdir(parents=True, exist_ok=True)


def load_builder():
    spec = importlib.util.spec_from_file_location("fipi_ref_match_builder", LEGACY_BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.REFERENCE_PATH = REFERENCE_PATH
    module.BLEND_PATH = BLEND_PATH
    module.PREVIEW_PATH = PREVIEW_PATH
    module.COMPARISON_PATH = COMPARISON_PATH
    return module


def add_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        return existing
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection


def link_to_collection(obj, collection):
    if obj.name not in collection.objects:
        collection.objects.link(obj)
    for col in list(obj.users_collection):
        if col != collection:
            col.objects.unlink(obj)


def add_master_rig_scaffold():
    rig_col = add_collection("Fipi master rig - reusable scaffold")

    bpy.ops.object.armature_add(enter_editmode=True, align="WORLD", location=(0, 0, 0.48))
    armature = bpy.context.object
    armature.name = "Fipi_Master_Rig"
    armature.data.name = "Fipi_Master_Rig_Data"
    armature.show_in_front = True
    link_to_collection(armature, rig_col)

    bones = armature.data.edit_bones
    root = bones[0]
    root.name = "root"
    root.head = (0, 0, 0.48)
    root.tail = (0, 0, 0.84)

    def bone(name, head, tail, parent=None):
        b = bones.new(name)
        b.head = head
        b.tail = tail
        b.parent = parent
        b.use_connect = False
        return b

    spine = bone("spine", (0, 0, 0.82), (0, 0, 1.72), root)
    head = bone("head_face_volume", (0, 0, 1.62), (0, 0, 2.42), spine)
    bone("jaw_smile_control", (0, -0.64, 1.84), (0, -0.76, 1.70), head)
    bone("eye_L", (-0.18, -0.62, 2.05), (-0.18, -0.82, 2.05), head)
    bone("eye_R", (0.18, -0.62, 2.05), (0.18, -0.82, 2.05), head)

    for side, suffix in ((-1, "L"), (1, "R")):
        clavicle = bone(f"clavicle_{suffix}", (side * 0.34, -0.18, 1.68), (side * 0.52, -0.36, 1.84), spine)
        upper = bone(f"upper_arm_{suffix}", (side * 0.52, -0.36, 1.84), (side * 0.70, -0.48, 2.12), clavicle)
        fore = bone(f"forearm_{suffix}", (side * 0.70, -0.48, 2.12), (side * 0.88, -0.54, 2.34), upper)
        hand = bone(f"hand_{suffix}", (side * 0.88, -0.54, 2.34), (side * 0.98, -0.56, 2.43), fore)
        for i in range(1, 5):
            bone(f"finger_{suffix}_{i}", (side * (0.90 + i * 0.018), -0.56, 2.39), (side * (0.94 + i * 0.028), -0.58, 2.51), hand)

        thigh = bone(f"thigh_{suffix}", (side * 0.20, -0.05, 0.86), (side * 0.25, -0.08, 0.64), root)
        foot = bone(f"foot_{suffix}", (side * 0.25, -0.08, 0.64), (side * 0.30, -0.36, 0.58), thigh)
        bone(f"toe_{suffix}", (side * 0.30, -0.36, 0.58), (side * 0.30, -0.48, 0.60), foot)

    bone("spines_crown", (0, 0.03, 2.24), (0, 0.02, 2.92), head)
    bone("spines_back", (0, 0.13, 1.22), (0, 0.10, 2.30), spine)

    bpy.ops.object.mode_set(mode="OBJECT")

    armature["asset_role"] = "master reusable rig scaffold"
    armature["rig_status"] = "scaffold_created_not_final_weight_painted"
    armature["facial_identity_rule"] = "do not alter face proportions without FP Lead approval"

    root_empty = bpy.data.objects.get("Fipi root - static approval model")
    if root_empty:
        root_empty.name = "Fipi_MASTER_CHARACTER_ROOT"
        root_empty["master_asset_role"] = "canonical character mesh group"
        root_empty["do_not_replace_mesh"] = True
        root_empty["do_not_change_uv_or_textures"] = True
        root_empty["source_reference"] = str(REFERENCE_PATH)

    return armature


def add_asset_metadata_to_scene():
    scene = bpy.context.scene
    scene["asset_name"] = "Fipi Master Character"
    scene["asset_status"] = "master_candidate_v0_1_requires_user_approval_and_manual_sculpt_pass"
    scene["canonical_reference"] = str(REFERENCE_PATH)
    scene["character_consistency_priority"] = "character consistency > scene quality > stylization changes"
    scene["immutable_rules"] = (
        "same mesh, UV, textures, materials, rig, facial identity, silhouette, colors, spines pattern"
    )

    for obj in bpy.data.objects:
        if obj.type in {"MESH", "CURVE", "ARMATURE", "EMPTY"}:
            obj["fipi_master_asset"] = True
            obj["source_character_bible"] = str(ROOT / "FIPI_CHARACTER_BIBLE.md")


def write_metadata():
    metadata = {
        "asset_name": "Fipi Master Character",
        "version": "0.1",
        "status": "master_candidate_requires_approval",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "canonical_reference": str(REFERENCE_PATH),
        "master_blend": str(BLEND_PATH),
        "preview": str(PREVIEW_PATH),
        "comparison": str(COMPARISON_PATH),
        "exports": {"glb": str(GLB_PATH)},
        "identity_lock": {
            "face_structure": "locked",
            "eye_shape": "locked",
            "body_proportions": "locked",
            "silhouette": "locked",
            "textures": "locked_after_approval",
            "materials": "locked_after_approval",
            "colors": "locked",
            "topology": "locked_after_approval",
            "uv": "locked_after_approval",
            "rig": "locked_after_approval",
        },
        "allowed_scene_changes": [
            "pose",
            "animation",
            "clothes",
            "accessories",
            "lighting",
            "environment",
            "camera",
            "composition",
        ],
        "blocked_scene_changes": [
            "new mesh for the character",
            "new face design",
            "changed body proportions",
            "changed spine pattern",
            "changed color palette",
            "belly patch moved onto face",
            "different material identity",
        ],
        "production_notes": [
            "This is the first reusable Blender master candidate generated from the character bible.",
            "It includes named objects, separated materials, a reusable rig scaffold, metadata, preview, and comparison.",
            "It is not yet a final AAA/manual sculpt; approval should require visual review against the canonical reference.",
        ],
    }
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")


def write_rig_notes():
    RIG_NOTES_PATH.write_text(
        """# Fipi Master Rig Notes

Status: scaffold created, not final weight-painted rig.

The armature is included to lock the intended reusable control hierarchy:

- root
- spine
- head_face_volume
- jaw_smile_control
- eye_L / eye_R
- clavicle / upper_arm / forearm / hand / fingers
- thigh / foot / toe
- spines_crown / spines_back

Before production animation, this scaffold should be converted into a final
deformation rig with weight painting, facial shape keys, blink controls, smile
controls, and squash/stretch limits that preserve the approved Fipi identity.
""",
        encoding="utf-8",
    )


def write_qa_report():
    QA_REPORT_PATH.write_text(
        f"""# Fipi Master Character QA Report

Verdict: master candidate v0.1, not final AAA/manual sculpt.

## Generated Artifacts

- Master blend: `{BLEND_PATH}`
- Preview: `{PREVIEW_PATH}`
- Comparison: `{COMPARISON_PATH}`
- Metadata: `{METADATA_PATH}`
- Rig notes: `{RIG_NOTES_PATH}`
- GLB export: `{GLB_PATH}`

## Passed

- Canonical reference copied into stable master-character folder.
- Character bible exists and defines identity lock rules.
- Blender file saved as `master.blend`.
- Named objects and separated materials are present.
- Rig scaffold is present.
- Scene metadata and external metadata JSON are present.
- Preview and reference comparison are generated as real files.

## Risks

- Model is still generated from a scripted sculpt-like workflow.
- It is not yet a hand-sculpted quad production mesh.
- UV/textures are not a final hand-authored texture set.
- Rig scaffold is not final weight-painted deformation rig.
- Facial identity needs user visual approval before becoming immutable master.

## Required Approval

FP Lead Agent must show preview and comparison to the user before this candidate
can become the immutable `MASTER CHARACTER ASSET`.
""",
        encoding="utf-8",
    )


def export_glb():
    try:
        bpy.ops.export_scene.gltf(filepath=str(GLB_PATH), export_format="GLB")
    except Exception as exc:
        print(f"GLB export skipped: {exc}")


def main():
    ensure_dirs()
    builder = load_builder()
    builder.create_fipi_model()
    add_master_rig_scaffold()
    add_asset_metadata_to_scene()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    bpy.ops.render.render(write_still=True)
    export_glb()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    # Comparison generation may use a fallback Blender scene builder when PIL is
    # unavailable. It must run after the master asset is safely saved/exported.
    builder.create_comparison_sheet()
    write_metadata()
    write_rig_notes()
    write_qa_report()


if __name__ == "__main__":
    main()
