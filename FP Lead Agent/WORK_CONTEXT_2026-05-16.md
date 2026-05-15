# Work Context 2026-05-16

Статус: остановка на ночь, продолжить завтра.

## 1. Роль FP Lead Agent

FP Lead Agent остается мозгом команды:

- принимает решения;
- раздает задачи фоновым агентам;
- не делает работу профильных агентов за них;
- контролирует gates и качество;
- показывает пользователю preview перед финальным использованием.

## 2. CG Agent Role Update

CG-agent больше не должен быть исполнителем "сделай 3D Фипи из воздуха".

Новая роль:

- CG Art Director / Technical CG Producer;
- готовит reference packs;
- выбирает production route;
- запрещает слабые методы;
- пишет prompts/handoffs;
- сравнивает результат с каноном;
- фиксирует risks/gaps;
- останавливает плохой route до потери времени.

Запрещено для canonical character:

- scripted Blender primitives как финальный путь;
- "почти похожий mascot";
- улучшать отклоненные болванки;
- идти в rig/materials/animation до silhouette/face approval.

## 3. Approved VPN JPEG

VPN JPEG approved пользователем.

Файл:

```text
FP Lead Agent/cg/fipi-vpn-forest/fipi_vpn_forest.jpg
```

Статус:

```text
approved standalone JPEG, not a master character asset
```

## 4. Fipi Master Character Status

Master character bible создана:

```text
FP Lead Agent/cg/fipi-master-character/FIPI_CHARACTER_BIBLE.md
```

Quality gate создан:

```text
FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md
```

Reference approval package approved пользователем:

```text
FP Lead Agent/cg/fipi-master-character/REFERENCE_APPROVAL_PACKAGE.md
```

Approved/candidate references:

```text
FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png
FP Lead Agent/cg/fipi-master-character/turnaround-references/fipi_turnaround_draft_approved_2026-05-15.png
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_expression_sheet_candidate.png
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_material_closeups_candidate.png
FP Lead Agent/cg/fipi-master-character/expression-material-stage/fipi_proportion_guide_candidate.png
```

## 5. Blender Stage 1 Status

Stage 1 silhouette/blockout был запущен через `Hypatia`.

V1 и V2 созданы, но не приняты:

```text
FP Lead Agent/cg/fipi-master-character/manual-sculpt-production/stage-01-silhouette-blockout/
```

Текущий verdict:

```text
not ready, needs silhouette revision
```

FP Lead recommendation:

```text
stop scripted/blockout revisions; switch to image-to-3D base or real manual sculpt tool
```

Причина:

- v2 чуть лучше по spine mass, но все еще не Фипи;
- scripted/blockout approach продолжает давать примитивного персонажа;
- лицо, форма головы/тела, руки, стопы и пластика иголок не проходят silhouette approval.

## 6. Next Practical Route

Так как человека для manual sculpt сейчас нет, выбран следующий маршрут:

```text
approved references -> image-to-3D base -> Blender QA/cleanup -> staged approval
```

Input package:

```text
FP Lead Agent/cg/fipi-master-character/IMAGE_TO_3D_INPUT_PACKAGE.md
```

Кандидаты сервисов:

- Meshy
- Tripo AI
- Rodin
- Luma Genie
- Spline AI only as experiment, not main master route

Spline использовать как scene/presentation tool после появления нормального
`GLB`, а не как основной sculpt tool.

## 7. Tomorrow Plan

1. Выбрать image-to-3D сервис.
2. Загрузить approved turnaround package.
3. Скачать `GLB/FBX/OBJ`.
4. Импортировать модель в Blender.
5. Сделать front/side/back QA preview.
6. Решить:
   - модель подходит для Blender cleanup;
   - нужно регенерировать;
   - нужно пробовать другой сервис.

## 8. Git Note

Не трогать старые удаления:

```text
FP Lead Agent/cg/fipi-punk-drummer/*
```

Они были удалены до текущей фиксации и не относятся к сегодняшнему commit scope.
