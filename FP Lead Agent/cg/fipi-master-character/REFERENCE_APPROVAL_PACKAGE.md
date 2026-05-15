# Fipi Reference Approval Package

Статус: approved by user  
Дата: 2026-05-15  
Назначение: передача reference pack в manual sculpt production после approval

## 1. Summary

Reference stage для master Blender модели Фипи собран. Пакет закрывает:

- canonical identity reference;
- turnaround candidate;
- expression sheet candidate;
- material closeups candidate;
- proportion guide candidate;
- character bible;
- quality gate;
- production plan;
- sculpt acceptance checklist.

После approval этого пакета можно запускать следующий этап:
manual sculpt / professional character modeling. Нельзя возвращаться к scripted
Blender primitives как финальному visual route.

## 2. Canonical Source

Canonical image:

```text
FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png
```

Character bible:

```text
FP Lead Agent/cg/fipi-master-character/FIPI_CHARACTER_BIBLE.md
```

Quality gate:

```text
FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md
```

## 3. Approved / Candidate Visual References

Turnaround reference candidate:

```text
FP Lead Agent/cg/fipi-master-character/turnaround-references/fipi_turnaround_draft_approved_2026-05-15.png
```

Turnaround notes:

```text
FP Lead Agent/cg/fipi-master-character/turnaround-references/TURNAROUND_REFERENCE_NOTES.md
```

Expression sheet candidate:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_expression_sheet_candidate.png
```

Material closeups candidate:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_material_closeups_candidate.png
```

Proportion guide candidate:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_proportion_guide_candidate.png
```

Expression/material notes:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/EXPRESSION_MATERIAL_NOTES.md
```

Expression/material stage plan:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/EXPRESSION_AND_MATERIAL_STAGE_PLAN.md
```

## 4. Existing Reference Pack

Reference pack manifest:

```text
FP Lead Agent/cg/fipi-master-character/reference-pack/REFERENCE_PACK_MANIFEST.md
```

Contact sheet:

```text
FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_pack_contact_sheet.png
```

Color swatches:

```text
FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_color_swatches.png
```

## 5. Production Documents

Feasibility gate result:

```text
FP Lead Agent/cg/fipi-master-character/FEASIBILITY_GATE_RESULT.md
```

Master model production plan:

```text
FP Lead Agent/cg/fipi-master-character/blender-master-production/MASTER_MODEL_PRODUCTION_PLAN.md
```

Turnaround requirements:

```text
FP Lead Agent/cg/fipi-master-character/blender-master-production/TURNAROUND_REQUIREMENTS.md
```

Blender master task prompt:

```text
FP Lead Agent/cg/fipi-master-character/blender-master-production/BLENDER_MASTER_TASK_PROMPT.md
```

Quality checklist:

```text
FP Lead Agent/cg/fipi-master-character/blender-master-production/QUALITY_CHECKLIST.md
```

Manual sculpt brief:

```text
FP Lead Agent/cg/fipi-master-character/MANUAL_SCULPT_BRIEF.md
```

## 6. Approval Status

User feedback so far:

- VPN JPEG: approved.
- Turnaround reference: "выглядит хорошо".
- Expression sheet / material closeups: "выглядит хорошо".
- Proportion guide: pending explicit approval.

Package status:

```text
approved for manual sculpt production
```

## 7. Known Risks

- Turnaround side/back views are generated reference candidates, not source
  photography or official production turnaround.
- Back spine pattern is a generated interpretation and must be treated as
  approved only after user confirmation.
- Expression sheet includes a wink/blink-like panel; a clean both-eyes blink can
  be generated if needed.
- Material closeups are visual lookdev direction, not UV textures.
- Proportion guide is a sculpt planning guide, not exact CAD measurement.

## 8. Manual Sculpt Start Gate

Manual sculpt can start because the user approved:

- turnaround reference;
- expression sheet;
- material closeups;
- proportion guide;
- this reference approval package.

Once approved, the next task should use:

```text
FP Lead Agent/cg/fipi-master-character/blender-master-production/BLENDER_MASTER_TASK_PROMPT.md
```

## 9. Forbidden Routes

Do not use:

- scripted primitives as final route;
- rejected `master candidate v0.1`;
- rejected `manual-sculpt-blockout`;
- pure image-to-3D as final asset;
- rig/animation before sculpt approval.

## 10. Next Decision

FP Lead/user decision:

```text
approved, proceed to manual sculpt production
```
