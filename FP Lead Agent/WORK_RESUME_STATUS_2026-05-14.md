# Статус работы на 2026-05-14

Этот файл фиксирует текущий контекст проекта Fix-Price перед сохранением в Git.

## Главная договоренность дня

Модель sidebar-агентов переиграна.

Теперь sidebar-агенты не считаются операционной командой, которой `FP Lead
agent` должен писать напрямую. Они являются галереей наставников, экспертных
профилей и best practices.

Рабочая архитектура:

```text
Sidebar agents = mentor gallery / best-practice library
FP Lead agent = orchestration layer
Background agents = execution layer
Artifacts = Figma, Buildin, Git, local docs
Sync = background agents -> FP Lead agent
```

Пользователь прокачивает sidebar-агентов. `FP Lead agent` использует их handoff
и инструкции для постановки задач фоновым агентам. Фоновые агенты выполняют
работу и возвращают sync `FP Lead agent`.

## Сохраненные mentor handoff

Добавлены и связаны с моделью sidebar-наставников:

- `UX_AGENT_MENTOR_HANDOFF.md`
- `DESIGN_SYSTEM_AGENT_MENTOR_HANDOFF.md`
- `UI_AGENT_MENTOR_HANDOFF.md`
- `FRONTEND_AGENT_MENTOR_HANDOFF.md`
- `WIKI_AGENT_MENTOR_HANDOFF.md`
- `QA_AGENT_MENTOR_HANDOFF.md`
- `ANALYTIC_AGENT_MENTOR_HANDOFF.md`

Эти документы использовать как quality layer при постановке задач фоновым
агентам.

## Обновленная модель

Основной документ:

- `SIDEBAR_AGENTS_OPERATING_MODEL.md`

Обновлены:

- `AGENTS.md`
- `.agents/AGENT_ORCHESTRATION.md`
- `.agents/*/SKILL.md`

В `SKILL.md` локальных агентов старый блок обязательного sync для sidebar-чата
заменен на правило: sidebar-профиль является наставником и best-practice
источником; sync обязателен для фоновых исполнителей, которых запускает
`FP Lead agent`.

## Figma / Подписки

Фоновый UI Agent продолжил миграцию раздела `Подписки` в `Android v2.0`.

Sync от UI Agent:

- target file: `Android v2.0 / ↪️ Подписки`;
- основной section: `Подписки / Flow / Light / full migration 2026-05-14`;
- покрыты auth/anon, push/system settings, system error, RU/KZ banner split,
  email branch, loaders, bottom sheet, success, input/snackbar error states;
- добавлен QA handoff / coverage map;
- existing email confirmation flow переиспользован через linked mirrors;
- caveat: Figma API не записал granular rectangle-hotspot reactions и прямой
  cross-page prototype link.

Задача готова к QA-pass с caveat по cross-page prototype limitation.

## Buildin / Wiki / Созвон iOS DS

Фоновому Wiki Agent была поставлена задача:

- транскрибировать запись звонка;
- выделить основные моменты, проблемы, решения, улучшения;
- сохранить Markdown в `FP Lead Agent/transcripts/`;
- опубликовать результат в Buildin: `Работа -> Созвоны -> Созвон iOS DS`.

Затем пользователь попросил остановить фонового Wiki Agent. Поток был остановлен.
Задачу нужно передать новому фоновому Wiki Agent при необходимости.

## Git

Не коммитить временную директорию:

```text
.playwright-cli/
```

Это артефакты браузерной проверки и не являются проектным контекстом.

## Новая операционная система задач

Добавлены документы:

- `PROJECT_OPERATING_SYSTEM.md`
- `TASK_TYPES_AND_DOD.md`
- `TASK_REGISTRY.md`
- `CG_AGENT_MENTOR_HANDOFF.md`

Новый стандарт:

1. Перед запуском значимой задачи фиксировать task type, source, target, scope,
   out of scope, Definition of Done и access/readiness.
2. Выбирать mentor handoff под задачу.
3. Запускать фоновых агентов с раздельным ownership.
4. Требовать progress/final sync.
5. Закрывать задачу только после quality gate.
6. Вести значимые задачи в `TASK_REGISTRY.md`.

## CG Agent

Пользователь создал sidebar `CG Agent`.

Новая роль зафиксирована как mentor/best-practice профиль, а не как
операционный исполнитель по умолчанию.

Добавлено:

- `CG_AGENT_MENTOR_HANDOFF.md`
- `cg-asset` task type в `TASK_TYPES_AND_DOD.md`
- ссылка на CG handoff в `PROJECT_OPERATING_SYSTEM.md`
- роль `CG Agent` в `SIDEBAR_AGENTS_OPERATING_MODEL.md`

Теперь `FP Lead agent` может запускать фонового исполнителя в роли `CG Agent`
для задач по 2D/3D-графике, визуальным ассетам, Blender, Three.js, WebGL,
рендерам, композиции и CG quality pass.
