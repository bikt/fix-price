# Fipi Master Model Production Plan

Status: production planning package  
Scope: Blender manual sculpt / professional character modeling only  
Current verdict: reference package approved, ready to start manual sculpt production

## 1. Purpose

Prepare a safe production route for creating `master.blend` for Fipi without repeating the rejected scripted-primitives failure.

The master model must become a reusable canonical character asset with stable mesh, UVs, materials, textures, rig, facial identity, and validation renders. The reference package is now approved for starting manual sculpt production. The sculpt process must still use stage approvals and stop-loss rules before retopo, materials, rig, or animation.

## 2. Source Of Truth

Read-only canon sources:

- `FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md`
- `FP Lead Agent/cg/fipi-master-character/FEASIBILITY_GATE_RESULT.md`
- `FP Lead Agent/cg/fipi-master-character/FIPI_CHARACTER_BIBLE.md`
- `FP Lead Agent/cg/fipi-master-character/MANUAL_SCULPT_BRIEF.md`
- `FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png`
- `FP Lead Agent/cg/fipi-master-character/reference-pack/REFERENCE_PACK_MANIFEST.md`
- `FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_pack_contact_sheet.png`

Do not use any rejected procedural candidate as visual truth. Existing procedural/blockout artifacts may be treated only as negative examples or technical pipeline notes.

## 3. Non-Negotiable Constraints

- Do not start Blender production until reference approval is complete.
- Do not use scripted primitives as the final visual route.
- Do not improve a rejected procedural mascot as the canonical master.
- Do not texture, rig, animate, export, or insert into Figma before form and face approval.
- Do not claim 1:1 similarity while side/back/top/neutral/expression/material references are missing.
- Do not mix this work with unrelated tasks.
- Every production stage must end with reviewable preview files and an honest verdict.

## 4. Production Method

Approved route after references are accepted:

1. Professional character modeling / manual sculpt in Blender or ZBrush-style workflow.
2. Sculpt blockout by a character artist, not scripted primitive assembly.
3. Manual facial identity sculpt before detail pass.
4. Manual spine, hands, feet, ears, belly patch, and silhouette passes.
5. Retopology into clean deformable quad-based mesh.
6. UV unwrap and separated texture sets.
7. PBR lookdev with plush/velvety body and spines, glossy eyes and nose only.
8. Reusable body rig plus facial controls or shape keys.
9. Validation renders and comparison sheets before master approval.

Optional image-to-3D may be used only as a temporary volume exploration base after approval. It must not be accepted as final topology, final face, final UVs, final materials, or final rig.

## 5. Stage Plan

### Stage 0: Reference Approval

Deliverables:

- Approved front, side, back, top, and neutral views.
- Approved expression sheet.
- Approved material closeups.
- Approved proportion guide.
- Written approval that the supplied reference set is sufficient to begin sculpt.

Exit gate:

- Completed. User approved the reference package on 2026-05-15.

Stop condition:

- If only the current posed/front-biased image is available, remain blocked and do not begin the master model.

### Stage 1: Proportion And Silhouette Planning

Tasks:

- Derive height, head/body relationship, belly size, arm length, leg stance, ear size, and spine mass from approved references.
- Create annotated silhouette boards for front, side, and back.
- Mark high-risk areas: eyes, nose, smile, cheeks, belly patch placement, spine rows, hands, feet, ears.

Deliverables:

- Proportion sheet.
- Silhouette overlay sheet.
- Written mismatch-risk notes.

Exit gate:

- FP Lead approves silhouette before sculpt detail.

### Stage 2: Manual Sculpt Blockout

Tasks:

- Build one cohesive soft mascot volume for head and body.
- Establish compact rounded body, broad upper head, round belly, short stable legs, raised friendly arms, large side ears, and dense blue spine mass.
- Keep the face fully green; the light belly patch stays on torso only.

Do not:

- Use a simple sphere/capsule/cylinder stack as the final body.
- Create petal-like procedural blue leaves.
- Add texture or rig work to hide form mismatch.

Deliverables:

- Front/side/back neutral blockout previews.
- Canonical-reference comparison sheet.
- Honest verdict: `ready for face blockout`, `not ready, needs sculpt iteration`, or `blocked, needs additional reference`.

Exit gate:

- FP Lead approves silhouette blockout.

### Stage 3: Face Identity Sculpt

Tasks:

- Sculpt large oval eyes with correct placement, scale, lively highlights, and friendly gaze.
- Sculpt small rounded glossy black nose.
- Sculpt open joyful smile with depth, dark mouth cavity, and visible tongue.
- Preserve soft cheeks and non-human mascot expression.
- Place short curved brows in the same emotional register as the canon.

Failure signs:

- Eyes read flat, icon-like, scared, aggressive, or unlike Fipi.
- Mouth becomes a simple drawn arc.
- Nose becomes too large, too sharp, or non-glossy.
- Face reads as another mascot in similar colors.

Deliverables:

- Close face preview.
- Front full-body preview.
- Side-by-side face identity comparison.

Exit gate:

- FP Lead approves face identity before spines/detail/retopo.

### Stage 4: Spines, Hands, Feet, Ears, Belly

Tasks:

- Sculpt blue spines as soft organic volumetric strands, not plastic leaves.
- Establish crown, side, and back spine rows from approved references.
- Keep spine size varied and direction readable.
- Sculpt small friendly hands with visible fingers.
- Sculpt short stable feet with visible toes.
- Sculpt large rounded ears with inner form.
- Sculpt soft oval belly patch on torso only.

Deliverables:

- Detail pass previews: crown, side spines, back spines, hands, feet, ears, belly.
- Updated full-body comparison sheet.

Exit gate:

- FP Lead approves secondary forms before retopo.

### Stage 5: Retopology

Tasks:

- Retopo into clean mostly quad-based mesh.
- Add deformation loops around eyes, mouth, shoulders, elbows, wrists/hands, hips, knees, ankles/feet.
- Preserve sculpt silhouette and facial identity.
- Name objects clearly.
- Keep separated logical parts where production needs it: eyes, nose, mouth/tongue, spines if appropriate, body, belly patch, rig controls.

Deliverables:

- Wireframe screenshots front/side/back.
- Mesh statistics.
- Retopo notes.

Exit gate:

- FP Lead approves retopo before UV/materials.

### Stage 6: UV And Materials

Tasks:

- Create reusable UV unwrap with clean islands.
- Set up separated PBR materials:
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
- Match guide colors from the reference pack:
  - body green `#74CD26`
  - belly light green `#D5E95B`
  - spines blue `#0054C4`
  - nose black `#121414`
  - mouth dark `#2D0808`
  - tongue red `#E25744`
- Add soft plush/velvety surface behavior for body, belly, ears, limbs, and spines.
- Keep glossy response limited mainly to eyes and nose.

Deliverables:

- UV preview.
- Material closeup renders.
- Neutral full-body render.

Exit gate:

- FP Lead approves lookdev before rig.

### Stage 7: Rig And Facial Controls

Tasks:

- Build reusable body rig.
- Add eye look controls.
- Add blink controls.
- Add smile and mouth open/close controls.
- Add basic squash/stretch only if it preserves the master proportions.
- Support neutral pose, joyful arms-up pose, waving, jumping, walking/simple locomotion, and head turn.

Deliverables:

- Rig hierarchy notes.
- Control list.
- Neutral, arms-up, wave, blink, mouth open/close validation previews.

Exit gate:

- FP Lead approves rig before export/scene use.

### Stage 8: Master Validation

Tasks:

- Save final `master.blend`.
- Produce validation renders.
- Produce comparison sheet with canonical reference on the left and result on the right.
- Produce turntable or multi-angle validation sequence.
- Document known deviations honestly.

Required final files:

- `master.blend`
- metadata JSON
- previews
- textures
- exports if approved
- rig notes
- validation QA report

Exit gate:

- FP Lead and user approve master asset.

## 6. Stop-Loss Rule

If any preview is not recognizable as Fipi:

- Stop production.
- Do not add detail.
- Do not texture.
- Do not rig.
- Do not animate.
- Document the mismatch.
- Return to reference/silhouette/face sculpt or request missing references.

## 7. Final Verdict Policy

Allowed production verdicts:

- `ready for user visual approval`
- `not ready, needs sculpt iteration`
- `blocked, needs additional front/side/back reference`

Forbidden verdicts:

- `approved master` without explicit FP Lead/user approval.
- `1:1 complete` while missing references remain unresolved.
- `ready for rig` before face and silhouette approval.
