# Fipi Expression And Material Notes

Статус: looks good by user, pending package approval  
Дата: 2026-05-15

## Files

Expression sheet candidate:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_expression_sheet_candidate.png
```

Material closeups candidate:

```text
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_material_closeups_candidate.png
```

## Expression Sheet Candidate

Покрывает:

- neutral/friendly expression;
- canonical joyful open smile;
- closed-mouth smile;
- wink/blink-like expression;
- eye direction variant;
- mild surprised expression.

Что хорошо:

- сохраняется зеленое лицо без светлой маски;
- глаза крупные, глянцевые, дружелюбные;
- нос маленький, черный, glossy;
- улыбки выглядят в рамках mascot identity;
- синие иголки и зеленое тело сохранены.

Риски:

- wink/blink требует отдельного approval: в production expression sheet лучше
  иметь чистый blink обоими глазами;
- surprised expression может увести персонажа в другой mood, нужно approval;
- sheet не размечен текстовыми labels, чтобы не ломать визуал, поэтому порядок
  выражений фиксируется в этом документе.

## Material Closeups Candidate

Покрывает:

- green body plush;
- light-green belly patch boundary;
- blue spine plush/strand material;
- glossy black nose;
- glossy eye;
- mouth cavity and tongue;
- inner ear;
- hand/finger and foot/toe surface.

Что хорошо:

- plush/velvety фактура читается на body, belly и spines;
- blue spines выглядят мягкими, не металлическими и не реалистично-колючими;
- глаза и нос имеют glossy response;
- mouth/tongue отделены по материалу;
- closeups пригодны как lookdev reference.

Риски:

- closeups не являются UV/texture source, это visual material direction;
- точные shader values нужно будет подбирать в Blender lookdev;
- spines material должен оставаться soft/plush, не превращаться в plastic.

## Approval Needed

Перед manual sculpt нужно решить:

- approve final reference package / revise specific sheet;
- нужен ли отдельный clean blink обоими глазами;
- нужен ли отдельный proportion guide image.

## Verdict

Reference stage advanced. Turnaround, expression candidate и material closeups
готовы для user approval. Manual sculpt все еще нельзя запускать до approval
этих sheets и proportion guide.
