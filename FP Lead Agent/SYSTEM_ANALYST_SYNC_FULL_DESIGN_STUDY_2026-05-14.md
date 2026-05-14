# Sync для FP Lead agent

Агент: System Analyst / BFT decomposition agent

Задача: изучить дизайн-систему, артефакты, токены, стили, компоненты, макеты, связи между разделами, legacy app и Android v2.0.

Статус: выполнено

Что сделано:

- Сверены локальные DS-артефакты: `design-system-map.md`, `UI_AGENT_DESIGN_MEMORY.md`, `LEGACY_TO_NEW_MIGRATION_TEMPLATE.md`, системно-аналитический reference.
- Через Figma изучена структура legacy `Mobile App - Android`.
- Через Figma изучена структура target `Android v2.0`.
- Зафиксирована модель связей: BFT -> legacy scenario audit -> DS reuse map -> rebuild in Android v2.0 -> QA coverage.
- Выделены продуктовые сценарные кластеры legacy: auth, settings/account, SPZ/fulfillment, catalog, product card, checkout, TYP, favorites, loyalty/card, 18+, stories/onboarding/update.
- Зафиксирован статус Android v2.0: что уже начато/пересобрано и какие зоны пока пустые.
- Составлена migration map `legacy area -> Android v2.0 target -> status -> analytical action`.
- Выделены продуктовые сущности для будущей декомпозиции БФТ.
- Обновлен `system-analyst-superpower/SKILL.md`, чтобы агент использовал новую карту.

Измененные артефакты:

- `.agents/system-analyst-superpower/references/fix-price-android-system-map.md`
- `.agents/system-analyst-superpower/SKILL.md`
- `SYSTEM_ANALYST_SYNC_FULL_DESIGN_STUDY_2026-05-14.md`

Ссылки:

- `FP Lead Agent/.agents/system-analyst-superpower/references/fix-price-android-system-map.md`
- `FP Lead Agent/.agents/system-analyst-superpower/references/design-system-mockups.md`
- `FP Lead Agent/design-system-map.md`
- `FP Lead Agent/LEGACY_TO_NEW_MIGRATION_TEMPLATE.md`

Что проверено:

- DS source hierarchy and Figma keys.
- Foundations: colors, typography, spacing, effects, icons.
- UI-kit role and known variant property API risk.
- Templates role as scenario/product pattern layer.
- Legacy sitemap and main product/user scenarios.
- Android v2.0 current populated/empty sections.

Блокеры:

- Figma API не всегда раскрывает содержимое Section как children; для точного frame-by-frame coverage при конкретной миграции нужен визуальный/manual pass по выбранному разделу.
- У части `Android Ui-kit` component sets variant properties не читаются через API; состояния нужно подтверждать через showcase или вручную.

Нужное решение FP Lead agent:

- Утвердить эту карту как базовую аналитическую память для дальнейших БФТ.
- Для следующей задачи указывать legacy area или Android v2.0 target page, чтобы я сразу делал декомпозицию по migration-template.
