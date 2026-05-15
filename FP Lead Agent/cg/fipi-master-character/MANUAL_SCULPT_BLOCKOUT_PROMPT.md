# Manual Sculpt Blockout Prompt

Задача: создать первый ручной sculpt blockout Фипи по reference pack.

## Роль

Работай как senior character sculpt artist для production-ready mascot pipeline.
Твоя задача на этом этапе - не финальный render и не сцена, а точное
восстановление формы персонажа.

## Source Of Truth

Character bible:

```text
FP Lead Agent/cg/fipi-master-character/FIPI_CHARACTER_BIBLE.md
```

Reference pack:

```text
FP Lead Agent/cg/fipi-master-character/reference-pack/REFERENCE_PACK_MANIFEST.md
FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_pack_contact_sheet.png
FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_color_swatches.png
```

Canonical image:

```text
FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png
```

## Scope

In scope:

- silhouette blockout;
- head/body unified mascot volume;
- face blockout;
- eyes/nose/smile placement;
- ears;
- spines massing and pattern;
- arms/hands/fingers;
- legs/feet/toes;
- belly patch placement;
- neutral material colors only for readability;
- front preview and reference comparison.

Out of scope:

- final textures;
- final PBR lookdev;
- final UV;
- final rig;
- animation;
- scene/background;
- accessories;
- clothing;
- Figma insertion.

## Hard Rules

- Do not continue the rejected procedural model as final truth.
- Do not create a different hedgehog in similar colors.
- Do not move belly patch onto the face.
- Do not simplify hands into tubes.
- Do not make spines plastic leaves.
- Do not optimize for beauty over identity.
- Do not proceed to texture/rig before blockout approval.

## Acceptance Criteria For Blockout

- Силуэт уже узнается как Фипи из reference.
- Лицо похоже по идентичности, даже без финального материала.
- Глаза, нос и улыбка стоят на правильных местах.
- Иголки читаются как тот же pattern.
- Руки и кисти сохраняют характер reference.
- Ноги и стопы не ломают пропорции.
- Belly patch только на torso.
- FP Lead может показать preview пользователю для решения: continue / revise.

## Output

Save into:

```text
FP Lead Agent/cg/fipi-master-character/manual-sculpt-blockout/
```

Required files:

- `fipi_blockout.blend`
- `previews/fipi_blockout_front.png`
- `previews/fipi_blockout_reference_comparison.png`
- `BLOCKOUT_HANDOFF.md`

## Final Handoff Format

```text
Status:
Preview saved:
Comparison saved:
Blend saved:

What matches:
- ...

What does not match yet:
- ...

Decision needed from FP Lead:
- approve blockout direction / revise blockout
```
