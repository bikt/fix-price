# Task Types And Definition Of Done

Справочник типов задач, стандартных агентов, Definition of Done и quality
gates.

## figma-migration

Использовать, когда нужно перенести legacy-раздел, flow или экран в новые
макеты.

Стандартные агенты:

- `Analytic Agent`
- `UX Agent`
- `Design System Agent`
- `UI Agent`
- `QA Agent`
- `Wiki Agent`, если нужно зафиксировать результат

Definition of Done:

- source и target определены;
- legacy-flow разобран целиком;
- есть scenario map;
- есть DS reuse map;
- есть migration/linkage map;
- все relevant states покрыты;
- новые экраны собраны на DS components/templates;
- нет ручных аналогов при наличии DS-компонента;
- QA verdict получен.

Quality gate:

```text
100% scenario coverage
+ DS compliance
+ state coverage
+ QA verdict
```

## ux-flow-analysis

Использовать для анализа сценария, навигации, состояний и пользовательской
понятности.

Стандартные агенты:

- `Analytic Agent`
- `UX Agent`
- `QA Agent`, если нужен независимый pass

Definition of Done:

- описана цель пользователя;
- описан happy path;
- описаны альтернативные ветки;
- описаны ошибки, loading, empty, success;
- указаны friction points;
- UX-замечания связаны с поведением и метрикой;
- есть рекомендации и open questions.

## design-system-review

Использовать для проверки DS-соответствия, components/templates и gaps.

Стандартные агенты:

- `Design System Agent`
- `UI Agent`, если нужна Figma-проверка
- `QA Agent`, если нужен verdict

Definition of Done:

- проверены tokens/styles/components/templates;
- найден source of truth;
- указаны DS gaps;
- ручные аналоги помечены как дефекты;
- есть список допустимых исключений;
- есть решение: pass / pass with risks / fail.

## qa-pass

Использовать для финальной приемки результата.

Стандартные агенты:

- `QA Agent`

Definition of Done:

- проверен scope;
- проверены screens/states/transitions;
- defect log оформлен по severity P0-P3;
- есть verdict:
  - `accepted`
  - `accepted with explicit risks`
  - `not accepted`
- указаны must-fix и open risks.

## buildin-wiki

Использовать для Buildin, канбана, документации, страниц, конспектов.

Стандартные агенты:

- `Wiki Agent`
- `Analytic Agent`, если нужен смысловой разбор

Definition of Done:

- найден существующий артефакт или подтверждено, что его нет;
- дубль не создан;
- локальный файл сохранен, если нужен;
- Buildin-страница/карточка обновлена;
- ссылка возвращена;
- проверено, что изменения сохранились;
- блокеры доступа названы явно.

## frontend-implementation

Использовать для кодовых задач.

Стандартные агенты:

- `Frontend Agent`
- `QA Agent`, если задача пользовательская
- `Analytic Agent`, если нужно уточнить поведение

Definition of Done:

- scope зафиксирован;
- код следует существующим паттернам;
- состояния реализованы;
- accessibility проверена;
- build/typecheck/test выполнены, если доступны;
- browser/smoke-check выполнен, если есть UI;
- риски и gaps названы.

## research-transcript

Использовать для аудио, созвонов, интервью и исследований.

Стандартные агенты:

- `Wiki Agent`
- `Analytic Agent`, если нужно выделить проблемы/решения

Definition of Done:

- транскрипт сохранен локально;
- summary структурировано;
- выделены основные моменты;
- выделены проблемы/боли;
- выделены решения;
- выделены improvements;
- action items и open questions вынесены отдельно;
- опубликовано в нужном месте, если это входит в scope.

## bug-fix

Использовать для конкретных дефектов.

Стандартные агенты:

- профильный агент по зоне дефекта;
- `QA Agent` для проверки;
- `Frontend Agent`, если дефект в коде;
- `UI Agent`, если дефект в Figma.

Definition of Done:

- воспроизведение описано;
- root cause найден или явно ограничен;
- fix выполнен;
- проверен сценарий дефекта;
- проверены соседние сценарии;
- residual risks названы.

## project-documentation

Использовать для инструкций, playbooks, архитектуры процесса и фиксации
договоренностей.

Стандартные агенты:

- `Wiki Agent`
- `Analytic Agent`, если нужна структура

Definition of Done:

- документ создан/обновлен;
- источник правды понятен;
- нет конфликта с существующими документами;
- ссылки на связанные документы добавлены;
- документ пригоден для повторного использования.

## cg-asset

Использовать для задач с 2D/3D-графикой, визуальными ассетами, рендерами,
Blender, Three.js, WebGL, иллюстрациями, текстурами и сложной графической
полировкой.

Стандартные агенты:

- `CG Agent`
- `Design System Agent`, если ассет входит в UI;
- `UI Agent`, если ассет встраивается в Figma;
- `Frontend Agent`, если нужен Three.js/WebGL;
- `QA Agent`, если нужен visual/interaction pass.

Обязательный approval gate для Figma:

1. CG/исполнитель готовит preview рендера или ассета.
2. `FP Lead agent` отправляет preview пользователю в чат.
3. Пользователь дает явный approve.
4. Только после approve ассет можно вставлять в Figma.
5. После вставки выполняется visual/DS/QA pass.

Definition of Done:

- роль ассета в пользовательском сценарии понятна;
- source/target и формат результата определены;
- графика не конфликтует с Fix Price DS/UI;
- композиция читается в целевом размере;
- 3D-форма, силуэт, масштаб, камера, материалы и свет проверены, если есть 3D;
- для Three.js/WebGL проверено, что canvas рендерится, responsive и
  интерактивен;
- для Blender сцена редактируемая, объекты/материалы названы понятно;
- ассеты сохранены в workspace, а не только во временной папке;
- если ассет вставляется в Figma, preview показан пользователю в чат и получен
  явный approve до вставки;
- есть sync с измененными артефактами, CG-решениями, проверками, рисками и
  нужными решениями `FP Lead agent`.
