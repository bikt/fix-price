# Fipi Image-To-3D Input Package

Статус: next practical route  
Дата фиксации: 2026-05-16  
Назначение: подготовить входные материалы для image-to-3D сервиса перед Blender cleanup

## Почему Этот Route

Manual sculpt человеком сейчас недоступен. Scripted Blender/blockout route
показал низкое качество и не сохраняет facial identity. Поэтому следующий
практичный путь:

```text
approved references -> image-to-3D base -> Blender QA/cleanup -> staged approval
```

Image-to-3D base не считается финальной master-моделью. Это только стартовая
геометрия для проверки и дальнейшей чистки.

## Recommended Services

Приоритетные сервисы:

- Meshy
- Tripo AI
- Rodin
- Luma Genie

Spline AI можно проверить как эксперимент, но не как основной route для
`MASTER CHARACTER ASSET`.

## Upload Inputs

Основной input:

```text
FP Lead Agent/cg/fipi-master-character/turnaround-references/fipi_turnaround_draft_approved_2026-05-15.png
```

Дополнительные reference inputs:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_expression_sheet_candidate.png
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_material_closeups_candidate.png
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_proportion_guide_candidate.png
FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png
```

Documentation for upload / prompt:

```text
FP Lead Agent/cg/fipi-master-character/REFERENCE_APPROVAL_PACKAGE.md
FP Lead Agent/cg/fipi-master-character/FIPI_CHARACTER_BIBLE.md
FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md
FP Lead Agent/cg/fipi-master-character/blender-master-production/QUALITY_CHECKLIST.md
```

## Prompt For Image-To-3D Service

```text
Create a 3D base mesh of the exact same green-and-blue mascot character shown
in the uploaded turnaround. Preserve the character identity: bright green plush
body, fully green face, light-green oval belly patch only on torso, saturated
blue soft rounded spines on crown/back, large friendly oval eyes, small glossy
black nose, open joyful smile, rounded ears, short legs and soft feet, soft
hands with fingers.

Do not make a realistic hedgehog. Do not change the character into a different
mascot. Do not move the belly patch onto the face. Preserve front/side/back
silhouette and blue spine layout from the turnaround.

Output should be a clean 3D base suitable for Blender cleanup. Prefer GLB/FBX/OBJ
export with separated materials if possible.
```

## Export Requirements

Preferred export order:

1. `GLB`
2. `FBX`
3. `OBJ`

If service supports texture export, include:

- base color textures;
- normal maps if generated;
- roughness maps if generated;
- material separation for body, belly, spines, eyes, nose, mouth, tongue.

## Reject Criteria

Reject generated model immediately if:

- character is not instantly recognizable as Fipi;
- face becomes another mascot;
- eyes or smile differ strongly from references;
- belly patch appears on face;
- spines become realistic spikes or plastic leaves;
- body becomes brown/realistic hedgehog;
- mesh is unusable even as cleanup base;
- side/back silhouette contradicts approved turnaround.

## Blender QA After Download

After downloading generated model:

1. Import into Blender.
2. Render front/side/back preview.
3. Compare against approved turnaround.
4. Check material separation.
5. Check mesh density/topology.
6. Decide:
   - proceed to Blender cleanup;
   - regenerate with revised prompt;
   - try another service.

## Next Step

Tomorrow: choose one image-to-3D service, upload the approved turnaround package,
download `GLB/FBX/OBJ`, then run Blender QA before any cleanup work.
