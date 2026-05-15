# Fipi Manual Sculpt Brief

Статус: следующий обязательный этап после rejection `master candidate v0.1`.

## Задача

Создать production-ready `MASTER CHARACTER ASSET` Фипи, визуально совпадающий с
canonical reference. Не улучшать процедурную болванку как финальный путь.
Работать как character sculpt / retopo / lookdev pipeline.

## Source Of Truth

```text
FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png
```

Reference pack для sculpt-разбора:

```text
FP Lead Agent/cg/fipi-master-character/reference-pack/REFERENCE_PACK_MANIFEST.md
FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_pack_contact_sheet.png
FP Lead Agent/cg/fipi-master-character/reference-pack/fipi_reference_color_swatches.png
```

## Цель

Получить `master.blend`, который можно использовать во всех будущих сценах как
единственный канонический Фипи:

- тот же mesh;
- тот же UV;
- те же textures;
- те же materials;
- тот же rig;
- та же facial identity.

## Почему Предыдущий Pass Не Принят

`master candidate v0.1` полезен как технический pipeline artifact, но не как
визуальный master:

- силуэт отличается;
- тело выглядит процедурным;
- лицо не совпадает;
- глаза/рот слишком плоские;
- иголки пластиковые и неорганичные;
- руки/кисти слишком простые;
- нет уровня plush/velvety фактуры reference;
- topology/UV/rig не production-final.

## Обязательный Workflow

1. **Reference Analysis**
   - выделить пропорции;
   - facial identity;
   - силуэт;
   - spines pattern;
   - руки/кисти;
   - стопы;
   - материалы и фактуру.

2. **Manual Sculpt Blockout**
   - начать с правильного силуэта;
   - не использовать шар/капсулу как финальный body;
   - голова и тело должны ощущаться как цельный мягкий mascot-volume;
   - лицо полностью зеленое, без светлой маски.

3. **Facial Sculpt**
   - глаза: форма, посадка, блики, живость;
   - нос: маленький черный glossy;
   - улыбка: открытая, объемная, с темной полостью и языком;
   - щеки: мягкие, friendly, как в reference.

4. **Spines Sculpt**
   - насыщенные синие мягкие иголки/пряди;
   - плотный гребень сверху;
   - продолжение по спине и бокам;
   - вариативность размера и направления;
   - не пластиковые листья.

5. **Body Details**
   - светло-зеленый belly patch только на torso;
   - короткие устойчивые ноги;
   - мягкие стопы с пальцами;
   - поднятые руки с органичными кистями и пальцами.

6. **Retopology**
   - clean quad mesh;
   - loops вокруг глаз, рта, плеч, кистей, ног;
   - deform-friendly topology.

7. **UV And Textures**
   - UV unwrap;
   - separated texture sets;
   - plush/velvety surface detail;
   - PBR materials.

8. **Rig**
   - reusable body rig;
   - facial shape keys или controls;
   - blink;
   - eye look;
   - smile;
   - mouth open/close;
   - arms wave;
   - jump-ready controls.

9. **Validation**
   - neutral preview;
   - joyful arms-up preview;
   - turntable;
   - reference comparison sheet;
   - QA report.

## Acceptance Criteria

- Персонаж без контекста узнается как тот же Фипи из reference.
- Facial identity совпадает.
- Силуэт совпадает.
- Цвета совпадают.
- Пузо не попадает на лицо.
- Иголки синие, мягкие, органичные.
- Материалы похожи на plush/velvety reference.
- Mesh clean и reusable.
- UV и texture set готовы к повторному использованию.
- Rig готов для будущих сцен.
- FP Lead показывает preview пользователю до утверждения.

## Output

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

## Verdict Policy

Нельзя писать `approved master`, если сходство не достигнуто. Допустимые
вердикты:

- `ready for user visual approval`;
- `not ready, needs sculpt iteration`;
- `blocked, needs additional front/side/back reference`.
