# Task Registry

Единый реестр значимых задач Fix-Price.

Статусы:

- `todo`
- `in-progress`
- `blocked`
- `ready-for-qa`
- `done`
- `paused`

## Активные и последние задачи

| ID | Название | Тип | Owner | Агенты | Статус | Links | Last sync | Next action |
|---|---|---|---|---|---|---|---|---|
| FP-2026-05-14-001 | Миграция раздела `Подписки` | figma-migration | FP Lead agent | UI Agent, далее QA Agent | ready-for-qa | Android v2.0 / `↪️ Подписки`; section `Подписки / Flow / Light / full migration 2026-05-14` | UI Agent сообщил о полном flow, caveat по cross-page prototype limitation | Запустить QA-pass по coverage, DS compliance и prototype expectations |
| FP-2026-05-14-002 | Созвон iOS DS: транскрипт и Buildin | research-transcript | FP Lead agent | Wiki Agent | paused | `C:/Users/mrbik/Desktop/tmp/Запись звонка [4a837105-c2a5-521f-8b20-560202fd4a85].aac` | Фоновый Wiki Agent был остановлен пользователем | При необходимости запустить нового фонового Wiki Agent по `research-transcript` DoD |
| FP-2026-05-14-003 | Sidebar agents mentor model | project-documentation | FP Lead agent | Lead + sidebar briefs | done | `SIDEBAR_AGENTS_OPERATING_MODEL.md`, mentor handoff files | Mentor gallery model зафиксирована | Использовать handoff при новых задачах |
| FP-2026-05-14-004 | Project operating system | project-documentation | FP Lead agent | Lead | done | `PROJECT_OPERATING_SYSTEM.md`, `TASK_TYPES_AND_DOD.md`, `TASK_REGISTRY.md` | Операционная система применена | Использовать intake, DoD и registry для новых задач |

## Шаблон записи

```text
| ID | Название | Тип | Owner | Агенты | Статус | Links | Last sync | Next action |
|---|---|---|---|---|---|---|---|---|
| FP-YYYY-MM-DD-XXX | ... | ... | ... | ... | todo | ... | ... | ... |
```

