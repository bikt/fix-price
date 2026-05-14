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

