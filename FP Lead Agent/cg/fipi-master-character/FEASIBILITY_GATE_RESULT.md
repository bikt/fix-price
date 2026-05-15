Task:
Create a canonical 3D Fipi 1:1 reusable master character asset, preserving facial identity, silhouette, proportions, materials, topology consistency, UV consistency, and rig reusability.

Target similarity:
Target is 1:1 canonical similarity to `reference/fipi_master_reference.png`. Current references are not sufficient to honestly guarantee a production 1:1 model, because they are derived from a single posed/front-biased image and do not define side, back, top, neutral pose, or full hidden spine/body structure. Any output from the current pack alone can only be judged as an approximation until missing views are supplied and approved.

Available references:
- Canonical full reference: `reference/fipi_master_reference.png`
- Reference pack crops: full character, face identity, eyes/nose/smile, crown spines, side spines, hands/fingers, belly patch, feet/toes.
- Contact sheet: `reference-pack/fipi_reference_pack_contact_sheet.png`
- Color swatches from manifest: body green `#74CD26`, belly light green `#D5E95B`, spines blue `#0054C4`, nose black `#121414`, mouth dark `#2D0808`, tongue red `#E25744`.
- Character bible and quality gate define identity, materials, topology, rig, and approval constraints.

Missing references:
- Approved front/side/back turnaround in neutral pose.
- Orthographic or near-orthographic front, left side, right side, back, and top views.
- Clean back view showing the exact spine pattern, count, layering, direction, and silhouette.
- Neutral face reference plus approved facial expression sheet for smile/open mouth/eyes/brows.
- Clear unobstructed hands, fingers, feet, toes, ears, and belly patch references.
- Material closeups for plush/velvety surface, blue spines, glossy eyes, glossy nose, mouth, and tongue.
- Proportion guide or measurement sheet for head/body/arms/legs/belly/spines.
- Approval that the current AI-looking canonical image is the final source of truth despite perspective, pose, and generated-image ambiguity.

Recommended method:
Do not begin Blender production yet. First produce/approve a reference and silhouette planning package from the current canonical image, then obtain or create an approved front/side/back turnaround. After that, use Professional Character Modeling / Manual Sculpt as the primary route: manual sculpt by a character artist, then retopo, UV, separated PBR materials, reusable rig, and facial controls or shape keys. Image-to-3D may be used only as a rough base to accelerate volume discovery, followed by manual cleanup, sculpt correction, retopo, UV, material rebuild, and rigging. It must not be accepted as final topology or final facial identity.

Rejected methods:
- Scripted Blender primitives from spheres, capsules, cylinders, cones, or petal-like spines.
- Improving the rejected `master candidate v0.1` or `manual-sculpt-blockout` as the final visual route.
- Procedural "almost mascot" generation followed by details.
- Pure image-to-3D as final asset without manual sculpt, cleanup, retopo, UV, and rig pass.
- Texture, rig, animation, scene render, or Figma insertion before form and face approval.
- Any route that creates a different hedgehog in similar green/blue colors instead of preserving Fipi facial identity.

Risks:
- Single-image/crop reference cannot define accurate 3D volume, back silhouette, spine layout, ear depth, limb depth, or hidden topology.
- Perspective and raised-arm pose distort proportions for neutral reusable asset creation.
- Facial identity is the highest-risk area; small changes to eye shape, eye spacing, nose size, mouth curvature, cheeks, and brow placement will create a different character.
- Spines may become plastic leaves, sharp spikes, or generic petals without manual sculpt direction.
- Procedural/blockout methods will not provide clean quad topology, UV layout, facial controls, or identity consistency.
- Image-to-3D may hallucinate back/side geometry and produce unusable topology unless treated only as a temporary base.

Expected failure signs:
- Character is not instantly recognizable as Fipi without context.
- Face reads as another mascot: wrong eyes, wrong smile, wrong nose, wrong cheeks, or wrong brow mood.
- Belly patch rises onto the face or becomes a flat sticker.
- Body becomes a simple capsule/sphere with accessories rather than an organic compact mascot volume.
- Blue spines look like identical plastic leaves, sharp spikes, or a generic mohawk.
- Hands, fingers, feet, or ears are simplified beyond the reference identity.
- Materials look plastic, rubber, clay, or metal instead of soft plush/velvety, with only eyes/nose/gloss elements allowed to be glossy.
- Mesh is not clean, not reusable, not retopo-ready, or cannot support UV/rig/facial controls.

Required approvals:
- FP Lead approval of this Feasibility Gate.
- Approval or creation of missing front/side/back/top/neutral references before 1:1 production modeling.
- Approval of production route: Manual Sculpt / Professional Character Modeling, with optional image-to-3D rough base only if manual cleanup is mandatory.
- Stage approvals in order: reference pack, silhouette blockout, face blockout, spines/hands/feet, sculpt detail, retopo/UV, material/lookdev, rig, animation/scene.
- Explicit stop-loss approval if first preview does not match facial identity or silhouette.

First output:
Reference/silhouette planning package only: annotated canonical reference, list of missing turnaround views, proportion notes, facial identity notes, spine-layout notes, and production checklist. No modeling, no render, no rig, no animation.

Verdict:
blocked, needs more references
