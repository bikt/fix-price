# Fipi Master Asset Handoff

Статус: master candidate v0.1, rejected as visual master  
Вердикт FP Lead Agent: pipeline создан, но asset визуально не проходит как
каноничный Фипи и не может стать immutable master.

## Артефакты

- Master blend: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\master.blend`
- Preview: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\previews\fipi_master_joy_preview.png`
- Comparison: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\previews\fipi_master_reference_comparison.png`
- Metadata: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\fipi_master_metadata.json`
- Rig notes: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\rig\rig_notes.md`
- QA report: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\validation\qa_report.md`
- GLB export: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\master\exports\fipi_master.glb`
- Build script: `C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character\scripts\build_fipi_master_asset.py`

## Что Уже Есть

- Stable reference path.
- Character bible.
- Blender `master.blend`.
- Named character parts.
- Separated materials.
- Rig scaffold.
- Scene and JSON metadata.
- Preview render.
- Reference comparison sheet.
- QA report.
- GLB export.

## Почему Отклонено Как Визуальный Master

- Силуэт слишком отличается от canonical reference.
- Тело выглядит как процедурная болванка, а не мягкий sculpt mascot.
- Лицо не совпадает по facial identity.
- Глаза и рот выглядят более плоско/иконно, чем в reference.
- Иголки читаются как отдельные пластиковые лепестки, а не органичные мягкие
  синие иголки/пряди.
- Руки и кисти слишком трубчатые и не повторяют характер reference.
- Материал и фактура недостаточно похожи на plush/velvety канон.

## Что Еще Не Финал

- Mesh не является ручным clean quad sculpt.
- UV/textures не являются финальным hand-authored texture set.
- Rig scaffold не является финальным weight-painted animation rig.
- Facial identity требует approval или ручного sculpt/detail pass.

## Правило Использования

Этот asset нельзя считать immutable master. Для будущих сцен использовать его
можно только как технический reference pipeline/base artifact, не как
окончательный канонический персонаж.

## Следующий Правильный Шаг

Нужен manual sculpt/detail pass:

1. Reference planes и image board по canonical image.
2. Sculpt blockout поверх правильного силуэта, не из текущей болванки.
3. Ручная проработка лица: глаза, щеки, нос, улыбка, рот, язык.
4. Ручная проработка иголок: органичные синие пряди с вариативностью формы.
5. Руки, кисти, ноги и стопы как part of character identity.
6. Retopo в clean quad mesh.
7. UV unwrap и hand-authored texture/material pass.
8. Reusable rig + facial controls.
9. Comparison sheet до approval.
