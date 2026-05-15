# Blender Master Task Prompt

Use this prompt only after FP Lead approves the missing turnaround, neutral, expression, proportion, and material references.

## Prompt For Next Executor

You are the production CG character artist for the Fix Price Fipi master character asset.

Your task is to create the canonical reusable `master.blend` for Fipi through manual sculpt / professional character modeling. Work in Blender or an equivalent character sculpt workflow, but the final deliverable must be a Blender master asset. Do not use scripted primitives as the visual production route. Do not improve rejected procedural candidates as the final character.

## Canon Sources

Read and follow:

- `FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md`
- `FP Lead Agent/cg/fipi-master-character/FEASIBILITY_GATE_RESULT.md`
- `FP Lead Agent/cg/fipi-master-character/FIPI_CHARACTER_BIBLE.md`
- `FP Lead Agent/cg/fipi-master-character/MANUAL_SCULPT_BRIEF.md`
- `FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png`
- `FP Lead Agent/cg/fipi-master-character/reference-pack/REFERENCE_PACK_MANIFEST.md`
- `FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_pack_contact_sheet.png`
- Approved turnaround, neutral pose, expression, material, and proportion sheets supplied by FP Lead.

## Current Gate

Do not begin if the approved turnaround package is missing.

If only the existing posed/front-biased reference is available, return:

```text
Status: blocked
Reason: missing approved front/side/back/top/neutral/expression/material references
Verdict: blocked, needs more references
```

## Target

Create a production-ready `MASTER CHARACTER ASSET` that can be reused in future scenes as the same Fipi:

- same mesh
- same UV layout
- same textures
- same materials
- same rig
- same facial identity
- same scale
- same color canon
- same silhouette identity

Do not create “a hedgehog in similar colors.” Preserve Fipi.

## Production Workflow

### 1. Reference Analysis

Before modeling, produce notes or boards identifying:

- face identity markers
- front/side/back silhouette
- head/body volume
- eye shape and placement
- nose shape and placement
- mouth shape, depth, tongue, smile corners
- cheek volume
- brow shape
- ear size and position
- belly patch position and shape
- hand/finger structure
- foot/toe structure
- crown/side/back spine layout
- material zones

Wait for approval if FP Lead requests a reference-analysis gate.

### 2. Manual Sculpt Blockout

Sculpt the core form manually.

Required:

- Compact friendly rounded mascot body.
- Head and torso feel like one soft organic mascot volume.
- Broad upper head.
- Large expressive oval eyes.
- Small glossy rounded black nose.
- Open joyful smile with depth.
- Fully green face with no light face mask.
- Light green belly patch only on torso.
- Short stable legs.
- Raised or neutral arms according to approved base pose.
- Large rounded side ears with inner form.
- Dense blue spines on crown, sides, and back.

Forbidden:

- Final body from scripted sphere/capsule/cylinder assembly.
- Plastic leaf spines.
- Generic mascot silhouette.
- Face that differs from the approved reference.
- Texture/lighting tricks to hide sculpt mismatch.

### 3. Face Approval Pass

The face is the highest-risk area and must be approved before detail, retopo, materials, or rig.

Submit:

- close face render
- full-body front render
- side-by-side comparison with canonical/approved face reference
- mismatch list
- verdict

Allowed verdicts:

- `ready for FP Lead face approval`
- `not ready, needs sculpt iteration`
- `blocked, needs additional face reference`

### 4. Secondary Form Pass

After face approval, sculpt:

- blue spine rows
- ears
- hands and fingers
- feet and toes
- belly patch volume and border
- plush surface detail

Submit detail previews for approval.

### 5. Retopology

Create clean reusable topology:

- mostly quad-based mesh
- edge loops around eyes and mouth
- deformation loops for shoulders, arms, hands, hips, legs, feet
- topology that supports facial controls or shape keys
- stable named objects and collections

Do not keep generated/image-to-3D topology as final.

### 6. UV And Materials

Create UVs and separated PBR materials:

- `body_green`
- `belly_light_green`
- `spines_blue`
- `eyes_white`
- `eyes_black`
- `eye_highlights`
- `nose_black_glossy`
- `mouth_dark`
- `tongue_pink`
- `inner_ear_green`
- optional accessories only if approved separately

Use reference guide colors:

- body green `#74CD26`
- belly light green `#D5E95B`
- spines blue `#0054C4`
- nose black `#121414`
- mouth dark `#2D0808`
- tongue red `#E25744`

Material direction:

- plush/velvety body, belly, ears, limbs, and spines
- glossy eyes and nose
- mouth and tongue as separate readable materials
- no hard plastic body material

### 7. Rig

Build reusable rig:

- neutral pose support
- arms-up joyful pose
- waving
- jumping
- simple walk/locomotion readiness
- head turn
- eye look controls
- blink
- smile controls
- mouth open/close
- basic squash/stretch only if it does not change canonical proportions

### 8. Validation

Before calling the asset ready, deliver:

- `master.blend`
- metadata JSON
- texture set
- neutral preview
- canonical joyful preview
- front/side/back/top validation renders
- face closeup render
- material closeup renders
- turntable or multi-angle validation sequence
- reference comparison sheet with canonical reference on the left and result on the right
- QA report listing pass/fail items and known deviations

## Stop-Loss Rule

If the first preview does not read as Fipi:

- Stop.
- Do not detail.
- Do not retopo.
- Do not texture.
- Do not rig.
- Record mismatches.
- Return `not ready, needs sculpt iteration` or `blocked, needs additional reference`.

## Final Response Format

When handing off work, return:

```text
Status:
Created files:
Preview files:
Approvals needed:
Known deviations:
Blockers:
Verdict:
```

Do not write `approved master` unless FP Lead and user explicitly approve the final validation package.

