# Fipi Master Blend Quality Checklist

Status: acceptance checklist for `master.blend`  
Use: FP Lead/user review before accepting the canonical Blender master asset

## 1. Gate Readiness

- [ ] Approved front/side/back/top turnaround exists.
- [ ] Approved neutral pose sheet exists.
- [ ] Approved expression sheet exists.
- [ ] Approved material closeups exist.
- [ ] Approved proportion guide exists.
- [ ] FP Lead approved the production method before modeling.
- [ ] No scripted-primitives route was used as the final visual method.
- [ ] No rejected procedural candidate was treated as visual truth.
- [ ] Current result is not claimed as 1:1 unless missing references were resolved and approved.

## 2. Identity Recognition

- [ ] Character is instantly recognizable as Fipi without context.
- [ ] Character does not read as a different hedgehog or generic mascot in similar colors.
- [ ] Overall emotional tone is friendly, open, joyful, and child-safe.
- [ ] Silhouette matches the approved Fipi silhouette from front, side, and back.
- [ ] Head/body relationship matches the approved proportions.
- [ ] Body is a cohesive soft mascot volume, not a simple capsule/sphere with attachments.

Automatic fail if:

- [ ] The face reads as another character.
- [ ] Silhouette is materially different from approved references.
- [ ] The asset relies on scene context, mountain background, camera angle, or lighting to be recognized.

## 3. Face

- [ ] Face is fully green with no light belly color moved onto the face.
- [ ] Eyes match approved shape, scale, spacing, placement, and friendly gaze.
- [ ] Pupils are black, large, lively, and correctly placed.
- [ ] Eye highlights are present and match approved visual character.
- [ ] Brows are short, softly curved, and match the approved mood.
- [ ] Nose is small, rounded, black, glossy, and correctly placed.
- [ ] Smile is open, joyful, and volumetric.
- [ ] Mouth has depth, a dark inner cavity, and a visible tongue where required.
- [ ] Cheeks and muzzle area are soft and organic.
- [ ] Expression does not become scared, aggressive, adult, human-like, or off-brand.

Automatic fail if:

- [ ] Eyes are flat icon shapes.
- [ ] Mouth is a simple painted arc with no volume.
- [ ] Nose size or placement changes facial identity.
- [ ] Approved expression controls break facial identity.

## 4. Body And Proportions

- [ ] Body is bright green and matches approved guide color/perception.
- [ ] Belly patch is light green and located only on torso.
- [ ] Belly patch is soft oval/round and integrated into plush surface.
- [ ] Belly patch is not a flat sticker.
- [ ] Arms are short, soft, friendly, and match approved pose/proportions.
- [ ] Hands have readable fingers matching reference intent.
- [ ] Legs are short, wide, stable, and match approved proportions.
- [ ] Feet are soft and stable with readable toes.
- [ ] Ears are large, rounded, green, and have inner form.

Automatic fail if:

- [ ] Belly patch rises onto the face.
- [ ] Hands or feet are simplified beyond recognition.
- [ ] Limb proportions make Fipi look like another character.

## 5. Spines

- [ ] Spines are saturated blue and match approved guide color/perception.
- [ ] Crown spines form the approved top silhouette.
- [ ] Side spines match approved side layout.
- [ ] Back spines match approved back layout.
- [ ] Spines are volumetric, soft, organic strands/needles.
- [ ] Spine sizes and directions have controlled natural variation.
- [ ] Spines are attached believably to the head/back volume.
- [ ] Spines have plush/toy-like material, not plastic.

Automatic fail if:

- [ ] Spines look like identical plastic leaves or petals.
- [ ] Spines are thin sharp spikes.
- [ ] Back/side spine layout is invented without approved reference.

## 6. Materials And Textures

- [ ] Body material reads plush/velvety.
- [ ] Belly material reads plush/velvety and lighter than body.
- [ ] Spine material reads plush/velvety blue, not plastic.
- [ ] Eyes are glossy and lively.
- [ ] Nose is glossy black.
- [ ] Mouth and tongue have separate readable materials.
- [ ] Surface texture is subtle and does not become noisy or dirty.
- [ ] Lighting does not shift colors away from canon.
- [ ] Materials are named clearly.

Required material names:

- [ ] `body_green`
- [ ] `belly_light_green`
- [ ] `spines_blue`
- [ ] `eyes_white`
- [ ] `eyes_black`
- [ ] `eye_highlights`
- [ ] `nose_black_glossy`
- [ ] `mouth_dark`
- [ ] `tongue_pink`
- [ ] `inner_ear_green`

Automatic fail if:

- [ ] Body reads as hard plastic, rubber, clay, or metal.
- [ ] Color scheme materially departs from approved guide colors.
- [ ] Materials are merged in a way that prevents future reuse/control.

## 7. Mesh And Topology

- [ ] Mesh is clean and production reusable.
- [ ] Topology is mostly quad-based.
- [ ] Edge loops support eyes.
- [ ] Edge loops support mouth and smile deformation.
- [ ] Edge loops support shoulders/arms/hands.
- [ ] Edge loops support hips/legs/feet.
- [ ] Mesh preserves approved silhouette from all views.
- [ ] Objects and collections are named clearly.
- [ ] No hidden throwaway geometry remains in the final asset.
- [ ] Modifiers are intentional and documented.

Automatic fail if:

- [ ] Generated or image-to-3D topology is left as final without retopo.
- [ ] Mesh cannot support rigging/facial controls.
- [ ] Topology changes facial identity or silhouette.

## 8. UV And Textures

- [ ] UV unwrap exists.
- [ ] UV islands are organized and reusable.
- [ ] UVs are not chaotic, overlapping unintentionally, or scene-specific.
- [ ] Texture set is saved and named clearly.
- [ ] Texture resolution is appropriate for master reuse.
- [ ] Texture paths are stable inside the project structure.
- [ ] UV layout is documented.

Automatic fail if:

- [ ] No UV unwrap exists.
- [ ] Textures cannot be reused in future scenes.
- [ ] Texture paths are broken.

## 9. Rig And Controls

- [ ] Reusable body rig exists.
- [ ] Rig hierarchy is named clearly.
- [ ] Neutral pose is supported.
- [ ] Arms-up joyful pose is supported.
- [ ] Waving pose/action is supported or rig-ready.
- [ ] Jumping pose/action is supported or rig-ready.
- [ ] Simple walk/locomotion readiness exists.
- [ ] Head turn works without breaking silhouette.
- [ ] Eye look controls exist.
- [ ] Blink controls exist.
- [ ] Smile controls or shape keys exist.
- [ ] Mouth open/close controls exist.
- [ ] Basic squash/stretch, if present, preserves canonical proportions.
- [ ] Rig notes are included.

Automatic fail if:

- [ ] Rig breaks the face identity.
- [ ] Deformations collapse hands, feet, mouth, eyes, or spines.
- [ ] Rig is scene-specific and not reusable.

## 10. Validation Renders

Required previews:

- [ ] Neutral front render.
- [ ] Neutral side render.
- [ ] Neutral back render.
- [ ] Top or top-three-quarter render.
- [ ] Canonical joyful expression render.
- [ ] Face closeup render.
- [ ] Spine closeups.
- [ ] Hands and feet closeups.
- [ ] Material closeups.
- [ ] Turntable or multi-angle validation sequence.
- [ ] Comparison sheet with canonical reference on the left and result on the right.
- [ ] Written mismatch list.

Automatic fail if:

- [ ] No side-by-side comparison exists.
- [ ] Preview camera/lighting hides known mismatches.
- [ ] Render is presented as approved without FP Lead/user approval.

## 11. Final File Package

Expected structure after approval:

```text
FP Lead Agent/cg/fipi-master-character/master/
  master.blend
  fipi_master_metadata.json
  previews/
  textures/
  exports/
  rig/
  validation/
```

Checklist:

- [ ] `master.blend` exists.
- [ ] Metadata exists.
- [ ] Preview files exist.
- [ ] Texture files exist.
- [ ] Rig notes exist.
- [ ] Validation QA report exists.
- [ ] Optional exports exist only after approval.

## 12. Verdict

Use one of these verdicts:

- [ ] `ready for user visual approval`
- [ ] `not ready, needs sculpt iteration`
- [ ] `blocked, needs additional front/side/back reference`

Do not use:

- [ ] `approved master` before explicit FP Lead/user approval.
- [ ] `1:1 complete` while reference blockers remain.
- [ ] `ready for rig` before silhouette and face approval.

