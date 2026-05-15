# Fipi Turnaround Requirements

Status: required before Blender master production  
Purpose: define the missing references needed before a manual sculpt artist can create a reliable reusable `master.blend`

## 1. Current Reference Status

Available references:

- Canonical posed/front-biased reference: `reference/fipi_master_reference.png`
- Draft-approved turnaround candidate:
  `turnaround-references/fipi_turnaround_draft_approved_2026-05-15.png`
- Contact sheet: `reference-pack/fipi_reference_pack_contact_sheet.png`
- Crops for face identity, eyes/nose/smile, crown spines, side spines, hands/fingers, belly patch, feet/toes.
- Color guide swatches:
  - body green `#74CD26`
  - belly light green `#D5E95B`
  - spines blue `#0054C4`
  - nose black `#121414`
  - mouth dark `#2D0808`
  - tongue red `#E25744`

Limitation:

The current pack is useful for identity analysis. A draft turnaround candidate
now exists and was approved by the user as looking good, but it is still a
reference candidate. It does not yet replace the need for expression sheet,
material closeups, proportion guide, and final reference approval before manual
sculpt.

## 2. Required Turnaround Views

All turnaround views should be orthographic or near-orthographic, same scale, same neutral lighting, no camera drama, no mountain/background dependency, and no pose exaggeration.

### Front View

Must show:

- Full body in neutral stance.
- Face centered and unobstructed.
- Exact eye shape, eye spacing, pupil size, highlights, brows, nose, mouth, cheeks.
- Belly patch shape and vertical placement.
- Arm length, hand shape, finger count/readability.
- Leg length, foot width, toe forms.
- Ear size and position.
- Visible crown spines and side spines.

Approval notes:

- The current canonical image may guide mood and identity, but a clean neutral front view is still required before final 1:1 claims.

### Left Side View

Must show:

- Head/body depth.
- Nose projection.
- Mouth depth and cheek volume.
- Ear depth and inner ear shape.
- Arm volume and hand thickness.
- Belly projection.
- Spine rows along crown, side, and back.
- Foot depth and toe placement.

### Right Side View

Must show:

- Whether the model is symmetrical or has intentional asymmetry.
- Right-side spine visibility and density.
- Right arm/hand silhouette.
- Ear position and size.

### Back View

Must show:

- Exact blue spine pattern, count, layering, and direction.
- Back body silhouette without face/belly distraction.
- Where spines start at crown and end near lower back.
- Relationship between spines, ears, arms, and torso.
- Whether green body is visible between spine rows.

This is one of the highest-priority missing views.

### Top View

Must show:

- Crown spine layout.
- Head width/depth.
- Ear placement.
- Spine row thickness and direction.
- Arm position relative to body.

### Bottom / Foot Contact View

Optional but useful:

- Foot pads or flat contact zones.
- Toe placement.
- Character balance for rigging and standing poses.

## 3. Required Neutral Pose Sheet

Needed because the current canonical image has raised arms and perspective distortion.

Neutral pose requirements:

- Feet planted and readable.
- Arms relaxed enough to reveal side body and spine layout.
- Face forward.
- Mouth may be in canonical friendly smile, but expression must not distort proportions.
- No accessories, clothing, props, mountain, or scenic occlusion.

Deliverables:

- Neutral front.
- Neutral side.
- Neutral back.
- Neutral three-quarter front.
- Neutral three-quarter back.

## 4. Required Expression Sheet

Minimum expressions:

- Canonical joyful smile from the current reference.
- Neutral friendly smile.
- Mouth closed smile.
- Mouth open smile.
- Blink.
- Eye look left/right/up/down.
- Mild surprised/open-mouth variant only if future scenes require it.

For each expression, preserve:

- Eye shape and placement.
- Nose shape and placement.
- Cheek softness.
- Brow mood.
- Non-human mascot identity.

Do not approve expression references that make Fipi look scared, aggressive, adult, human-like, or like a different mascot.

## 5. Required Material Closeups

Controlled material references are required before lookdev.

### Body Green Plush

Need closeups showing:

- Soft plush/velvety texture.
- Fine fuzz direction.
- Roughness level.
- How light rolls over cheeks, arms, belly edge, and legs.
- No hard plastic shine.

### Belly Light Green Plush

Need closeups showing:

- Soft oval patch boundary.
- Same plush family as body.
- Lighter color without becoming white/yellow.
- Patch integrated into torso, not a sticker.

### Spines Blue

Need closeups showing:

- Saturated blue color.
- Soft volumetric strand/needle form.
- Surface texture.
- Variation in size and direction.
- Attachment to head/back.

### Eyes

Need closeups showing:

- White sclera material.
- Black pupil material.
- Highlight placement.
- Gloss level.
- Eye curvature and thickness.

### Nose

Need closeups showing:

- Rounded black glossy shape.
- Nose size relative to eyes and mouth.
- Soft attachment to muzzle/face.

### Mouth And Tongue

Need closeups showing:

- Mouth cavity depth.
- Dark mouth material.
- Tongue shape, color, and placement.
- Smile corner shape.

### Inner Ear

Need closeups showing:

- Ear rim thickness.
- Inner ear green tone.
- Soft rounded interior form.

## 6. Required Proportion Guide

The sculpt artist needs a measurement sheet, even if approximate.

Include:

- Overall height.
- Head/body combined volume proportions.
- Head width at ears.
- Belly patch height and width.
- Eye size and spacing.
- Nose size.
- Mouth width.
- Ear diameter.
- Arm length and thickness.
- Hand/finger size.
- Leg length and foot size.
- Spine height, width, and row spacing.

The guide may be visual rather than numeric, but it must be approved before sculpt begins.

## 7. Approval Requirements

Before Blender sculpt starts, FP Lead must approve:

- Turnaround sheet.
- Neutral pose sheet.
- Expression sheet.
- Material closeups.
- Proportion guide.
- Written statement that the references are sufficient to begin manual sculpt.

If any of these are missing, the correct verdict is:

`blocked, needs more references`

## 8. Rejection Criteria For References

Reject a reference pack if:

- Views are not aligned or not same scale.
- Side/back/top views are guessed without approval.
- The face changes between views.
- Belly patch moves onto the face.
- Spines change style, color, count logic, or direction between views.
- Materials look plastic/rubber/clay instead of plush/velvety.
- Images introduce clothing, props, scenery, or pose distortion into the master base.
- Reference ambiguity would force the sculpt artist to invent major forms.
