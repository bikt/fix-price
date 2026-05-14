# Fix Price App Design Study

Frontend Agent working map for the Fix Price Android design system, legacy app, and `Android v2.0` rebuild process.

## How To Use This

Read this together with `fix-price-design-memory.md` before implementing UI from Fix Price mockups.

Primary shared study artifacts:

- `FP Lead Agent/DESIGN_SYSTEM_AND_APP_STUDY_2026-05-14.md`
- `FP Lead Agent/UI_AGENT_FULL_DESIGN_STUDY_2026-05-14.md`
- `FP Lead Agent/LEGACY_TO_NEW_MIGRATION_TEMPLATE.md`

## Source Priority

1. Foundations: `DS - Colors`, `DS - Android typography`, `DS - Gaps`, `DS - effects`, `DS - Icons`.
2. Base components: `Android Ui-kit`.
3. Complex patterns: `Android templates`.
4. State validation: `Android ui elements showcase`.
5. Target layouts: `Android v2.0`.
6. Legacy scenarios: `Mobile App - Android`.

Legacy is a source for flows, states, transitions, copy, and edge cases. It is not a source for final visual styling.

## Figma Source Map

| Layer | File | Key | Frontend relevance |
| --- | --- | --- | --- |
| Colors | `DS - Colors` | `xrrrRVKXHqifNnhd3cC1bN` | Map semantic colors to implementation tokens |
| Typography | `DS - Android typography` | `ScDQwwKHyWya2YaKFpClWa` | Map text styles to type tokens/components |
| Spacing | `DS - Gaps` | `1zQbV2SN44caC80Ib5eDMZ` | Use gap scale and breakpoint logic |
| Effects | `DS - effects` | `pxURPtXGNxQPl2X6ZNn7fr` | Elevation, radius, blur semantics |
| Icons | `DS - Icons` | `fgeRWdjJlsH7uBcFJcadjY` | Use library icons, not ad hoc drawings |
| UI Kit | `Android Ui-kit` | `8eyN4wOGRSWnqqxEGXhheB` | Base component boundaries and states |
| Templates | `Android templates` | `GVjBHX6TemLKrZWKnOpfKm` | Screen organisms and reusable product patterns |
| Showcase | `Android ui elements showcase` | `PlMyc3INhqfVp2I7hDvInA` | State validation and changelog |
| Target App | `Android v2.0` | `w6fzp4MqBpWjgSMGrZK0XD` | Current spec for rebuilt screens |
| Legacy App | `Mobile App - Android` | `oOt1o1Ln0lxhbb3ZSvoOWg` | Scenario and edge-case source |

## Foundations

- Colors: `Theme Colors`, `Light` and `Dark`, `140` variables. Groups include `brand`, `background`, `text`, `button`, `icon`, `divider-border`, `opacity`, `support colors`.
- Android action colors: `button/button-primary #81BB3C`, `button/button-dark #0F4193`, `background/bg-negative #E81B0C`.
- Typography: `46` text styles, user-facing Android UI uses `Roboto`; `Frame naming/*` is only for canvas organization.
- Gaps: `Dimensions` collection, breakpoints `adaptive 375`, `tablet 768`, `desktop 1400`; gap scale `2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64`.
- Effects: radius variables `radius-XS/S/M/L/XL`, shadow styles `Shadow-down`, `Shadow-up`, `header-shadow`. Naming debt: docs say `appBlur`, Figma currently exposes `ageBlur`.
- Icons: `10` component sets, `182` components; use DS icons for navigation/actions.

## Component And Template Layers

`Android Ui-kit` has roughly `98` component sets and `663` components. Key families:

- App chrome: `AppBar`, `Status Bar`, `NavBar`.
- Actions: `Button / Primary`, `Secondary`, `Dark`, `Error`, `Outline`, `Minimal`, `QTY`, `Floating`.
- Inputs: `Input / Text`, `Email`, `Phone`, `Password`, `Textarea`.
- Feedback: `Alert`, `ActionSheet`, `Snackbar`, `Loader / Full Screen`.
- Commerce: `Product card / Catalog`, `Product card / Cart`, `Product Photo`, `Price tag`, `QTY`.
- Navigation and selection: tabs, segmented controls, switchers, checkbox, radio.
- Sheets: `Bottom Sheet Header`, `Bottom Sheet Actions`, `Bottom sheet master`, `Bottom sheet / text content`.

`Android templates` has roughly `234` component sets and `1213` components. Use it for organisms and screen patterns:

- Error screens, app rate, bottom sheet info variants.
- Profile navbar/header/blocks.
- Catalog main/category/search/filter.
- Product card details and BPC states.
- Cart summary/items/empty/no SPZ.
- Checkout address, recipient, payment, promo, loyalty, delivery, total.
- TYP pickup/delivery/PVZ/express.
- Stores map/list/city.
- Promotions main/detail.

`Android ui elements showcase` mirrors UI-kit and validates states. Some pages can be thin or empty, so cross-check with UI-kit pages and existing `Android v2.0` sections.

## Legacy App Scenario Inventory

`Mobile App - Android` is the source for product and user scenarios:

- First launch/localization: country, city, permissions, transition to home.
- Auth: registration, login, SMS/flash call/code confirmation, password recovery, provider branches, server and validation errors.
- Home: anonymous/user, confirmed/unconfirmed, banners, stories, loyalty entry, catalog/product/promo entry.
- Search: modal search, typing, query refinement, brands, category transition, filters, no results, backend empty/error, 18+ blur/age-confirmation flows.
- Catalog and product: main catalog, categories, sorting/filtering, product grid, product card, variants, stock, BPC special price, characteristics, related products.
- Cart and checkout: full/short/empty/no-SPZ, unavailable items, summary, delivery/pickup/PVZ, recipient, payment, promo, loyalty, total, private cases, fast order.
- TYP: order status, pickup/delivery/PVZ/express, items, summary, cancellation, rating.
- Profile: loyalty/card, purchases, categories, notifications, settings, addresses, profile completion, promo codes, legal, subscriptions, account deletion.
- Stores and promos: map/list/city/store info, promotions list/detail.
- Errors: too many attempts, validation, auth required, expired/invalid code, already confirmed, backend/system errors, snackbar states.

Frontend implication: when coding a flow, check both `Android v2.0` and legacy. If `Android v2.0` is partial, legacy tells what states must still exist.

## Android v2.0 Target State

`Android v2.0` mirrors legacy taxonomy but is not fully complete. Observed filled or partially filled areas include:

- `Главная` with Light/Dark sections.
- `Поиск` with many `360x800` screens, labels, loaders, bottom sheets and flow arrows.
- `Обновление приложения`, `Центр уведомлений`, `Настройки`, `Любимые категории` with Light/Dark sections.
- `Профиль` with task sections and status/user-card states.
- `Подтверждение почты` with canonical email confirmation states.
- `Подписки` with a current DS-only restart section.
- `Чекаут` with Light/Dark sections.

Many pages are still placeholders or partially migrated. Treat `Android v2.0` as the current spec for completed sections, but do not assume empty pages mean the product has no flow.

## Active Subscriptions Context

Current sync files identify the active/canonical subscriptions rebuild:

- Target file: `Android v2.0`, key `w6fzp4MqBpWjgSMGrZK0XD`.
- Target page: `↪️ Подписки`, node `65:35667`.
- Current canonical section in latest UI study: `594:696`, `Подписки / DS-only restart / 2026-05-14`.
- Prior manual/scaffold section `586:1868` was removed.
- Old background-agent section `489:1983` was removed earlier.
- DS source has typo/debt: `Subscrptions / Switchers`; variants `user=true`, `user=false`.
- The section should cover auth/anon subscriptions, push settings, API/system errors, RU/KZ split, email confirmed/unconfirmed, email confirmation branch, loaders, no-letter bottom sheet, success/error states.

Frontend implication: do not implement subscriptions from an older scaffold note without checking the latest sync. The canonical target changed over the day.

## Migration Rule

A legacy-to-new migration is complete only when:

```text
100% flow coverage
+ DS pass
+ QA pass
```

Checklist:

- All legacy screens are represented or explicitly mapped elsewhere.
- All states are preserved: default, loading, empty, error, disabled, success, selected, pressed/focus where relevant.
- All transitions and branch scenarios are restored or documented.
- New screens are built from current DS components/templates.
- No manual analog is used when a DS component exists.
- DS gaps are documented instead of hidden.
- Target lives in `Android v2.0`.

## Frontend Handoff Rules

- Build from the project's existing code patterns first.
- Translate DS tokens into code tokens or existing CSS/theme variables; avoid magic values where practical.
- Use the Figma component/template names to understand behavior, but choose code boundaries based on the app architecture.
- Preserve mobile commerce density: search, price, stock, CTA, city/fulfillment context should be easy to scan.
- Always cover loading, empty, error, disabled, selected, focus states if the scenario requires them.
- Track mappings for complex work: `legacy state -> Android v2.0 state -> frontend route/component/state`.
- Validate sticky elements, bottom sheets, loaders, text overflow, and accessibility labels.

## Open Risks

- `Android v2.0` is a work-in-progress file and can contain scaffold-only sections.
- Some Figma API reads time out on deep traversal; inspect page/section scope incrementally.
- Mixed naming and typos exist: `Subscrptions`, `Bage`, `Infromer`, `Charachteristics`, `tetriary`, `ageBlur`, `Подверждение`.
- UI-kit variant properties can be unreliable through the API; verify visually or via showcase.
- Template components can duplicate older UI-kit concepts; check current DS source before implementation.
- Latest team sync files can supersede older canvas sections.
