# Project Operating System

Операционная система выполнения задач в проекте Fix-Price.

Цель: задачи должны выполняться быстрее, четче и с меньшим количеством ошибок.
Для этого каждая задача проходит через единый intake, типизацию, выбор агентов,
quality gates и проверяемый sync.

## Главный принцип

```text
Сначала тип задачи и Definition of Done.
Потом агенты и execution.
Потом quality gate и финальный verdict.
```

`FP Lead agent` отвечает за то, чтобы задача не уходила в работу как размытая
просьба. Перед запуском он фиксирует минимальный task brief.

## Слои системы

```text
Пользователь
-> FP Lead agent
-> task intake
-> выбор task type
-> выбор mentor handoff
-> фоновые агенты
-> sync
-> quality gate
-> финальный ответ
```

Sidebar-агенты остаются mentor gallery / best-practice library. Фоновые агенты
являются execution layer.

## Обязательный intake brief

Перед запуском значимой задачи `FP Lead agent` фиксирует:

```text
Задача:
Тип:
Source:
Target:
Scope:
Out of scope:
Нужные агенты:
Definition of Done:
Риски:
Access/readiness:
```

Для маленьких задач brief может быть коротким, но тип, scope и Definition of
Done должны быть понятны.

## Task types

Базовые типы задач:

- `figma-migration`
- `ux-flow-analysis`
- `design-system-review`
- `qa-pass`
- `buildin-wiki`
- `frontend-implementation`
- `research-transcript`
- `bug-fix`
- `project-documentation`
- `cg-asset`

Подробные DoD и gates описаны в `TASK_TYPES_AND_DOD.md`.

## Access/readiness check

Перед задачами с внешними сервисами проверить:

- Figma доступ есть?
- Buildin доступ есть?
- GitHub доступ есть?
- файл/аудио/ссылка доступны?
- target найден?
- агент может писать туда, куда нужно?
- есть ли риск создать дубль?

Если доступ не готов, сначала решается доступ, затем запускается execution.

## Выбор mentor handoff

`FP Lead agent` выбирает нужные наставнические briefs:

- `ANALYTIC_AGENT_MENTOR_HANDOFF.md`
- `UX_AGENT_MENTOR_HANDOFF.md`
- `DESIGN_SYSTEM_AGENT_MENTOR_HANDOFF.md`
- `UI_AGENT_MENTOR_HANDOFF.md`
- `FRONTEND_AGENT_MENTOR_HANDOFF.md`
- `WIKI_AGENT_MENTOR_HANDOFF.md`
- `QA_AGENT_MENTOR_HANDOFF.md`
- `CG_AGENT_MENTOR_HANDOFF.md`

Например, для Figma migration обычно подключаются:

```text
Analytic + UX + Design System + UI + QA
```

Для Buildin/созвона:

```text
Wiki + Analytic, если нужно выделить проблемы/решения/action items
```

## Правила параллельной работы

Параллелить можно только разные зоны ownership.

Хорошо:

- Analytic Agent готовит scenario map.
- Design System Agent готовит DS reuse map.
- QA Agent готовит checklist.
- UI Agent собирает Figma после достаточного handoff.

Плохо:

- два агента одновременно правят один и тот же Figma section;
- два агента создают одну и ту же Buildin-страницу;
- несколько агентов меняют один файл без разделенного ownership.

## Sync-форматы

### Progress sync

```text
Агент:
Статус:
Сделано:
Блокер:
Следующий шаг:
```

### Final sync

```text
Агент:
Задача:
Статус:
Что сделано:
Измененные артефакты:
Ссылки:
Coverage:
Что проверено:
Риски:
Verdict:
Нужное решение FP Lead agent:
```

## Quality gates

Значимая задача не считается готовой только по словам исполнителя.

Минимальные gates:

- исполнитель вернул final sync;
- есть ссылки/артефакты;
- coverage описан;
- риски названы;
- QA или Lead-check выполнен;
- Definition of Done выполнен или есть explicit risk.

Для Figma migration финальная формула:

```text
100% scenario coverage
+ DS compliance
+ state coverage
+ QA verdict
```

## Task registry

Все значимые задачи фиксируются в `TASK_REGISTRY.md`.

Минимальные поля:

```text
ID:
Название:
Тип:
Owner:
Агенты:
Статус:
Links:
Last sync:
Next action:
```

Registry нужен, чтобы видеть, кто чем занят, что заблокировано и что требует
решения.

## Post-mortem

После крупных задач фиксировать:

```text
Что сработало:
Что тормозило:
Что улучшить в prompt/process:
Какие правила добавить в mentor handoff:
```

Это превращает каждую сложную задачу в улучшение системы.
