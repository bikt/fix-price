# Design System And App Study 2026-05-14

Рабочая карта для UI/Design System execution agent по проекту Fix-Price Android app.

## 1. Источники Правды

Локальные документы:

- `FP Lead Agent/design-system-map.md` - основная карта Figma-источников и правил сборки.
- `FP Lead Agent/design-system.md` - общие принципы Fix Price UI и базовые web/shared tokens.
- `FP Lead Agent/data-model.md` - модель рабочих данных проекта: Buildin, канбан, Figma sources, build rules.
- `FP Lead Agent/AGENTS.md` - оркестрация команды и правила sync с FP Lead agent.
- `FP Lead Agent/UI_AGENT_DESIGN_MEMORY.md` - рабочая память UI Agent.
- `FP Lead Agent/LEGACY_TO_NEW_MIGRATION_TEMPLATE.md` - обязательный процесс legacy -> Android v2.0.

Главное правило: новые Android-макеты создаются в `Android v2.0`; legacy `Mobile App - Android` используется только как reference сценариев, состояний и edge cases.

## 2. Figma Source Architecture

Порядок использования:

1. Foundations:
   - `DS - Colors` / `xrrrRVKXHqifNnhd3cC1bN`
   - `DS - Android typography` / `ScDQwwKHyWya2YaKFpClWa`
   - `DS - Gaps` / `1zQbV2SN44caC80Ib5eDMZ`
   - `DS - effects` / `pxURPtXGNxQPl2X6ZNn7fr`
   - `DS - Icons` / `fgeRWdjJlsH7uBcFJcadjY`
2. Base components:
   - `Android Ui-kit` / `8eyN4wOGRSWnqqxEGXhheB`
3. Complex product patterns:
   - `Android templates` / `GVjBHX6TemLKrZWKnOpfKm`
4. State validation:
   - `Android ui elements showcase` / `PlMyc3INhqfVp2I7hDvInA`
5. Target layouts:
   - `Android v2.0` / `w6fzp4MqBpWjgSMGrZK0XD`
6. Legacy reference:
   - `Mobile App - Android` / `oOt1o1Ln0lxhbb3ZSvoOWg`

## 3. Foundations

### Colors

File: `DS - Colors`.

- Pages: `Project cover`, separator, `🎨 Colors`.
- Variable collection: `Theme Colors`.
- Modes: `Light`, `Dark`.
- Variables: `140`.
- Groups:
  - `brand/*`
  - `background/*`
  - `text/*`
  - `button/*`
  - `icon/*`
  - `divider-border/*`
  - `opacity/*`
  - `app preloader/*`
  - `shades/*`
  - `support colors/*`
- Paint styles: `13`, mostly gradients and preloader styles.

Rule: use variables from `Theme Colors`, not hardcoded hex.

### Typography

File: `DS - Android typography`.

- Pages: `Project cover`, separator, `styles`.
- Text styles: `46`.
- Main Android UI font: `Roboto`.
- Key groups:
  - `Heading/H1...H4`
  - `Body/body-17...body-13` with regular, semibold, bold, strikethrough, underline variants
  - `Caps/*`
  - `etc/button`
  - `etc/bpc-price`
  - `Frame naming/*` only for canvas organization.

Rule: user-facing text should use Android typography styles.

### Gaps

File: `DS - Gaps`.

- Variable collection: `Dimensions`.
- Variables: `15`.
- Breakpoints:
  - `Breakpoint/desktop`: `1400`
  - `Breakpoint/tablet`: `768`
  - `Breakpoint/adaptive`: `375`
- Gap scale:
  - `2`, `4`, `8`, `12`, `16`, `20`, `24`, `32`, `40`, `48`, `56`, `64`

Rule: use `Gap/*` variables for padding, item spacing and spacer frames.

### Effects

File: `DS - effects`.

- Variables:
  - `radius-XS`: `4`
  - `radius-S`: `8`
  - `radius-M`: `16`
  - `radius-L`: `24`
  - `radius-XL`: `32`
  - blur variable currently named `ageBlur`: `10`
- Effect styles:
  - `Shadows/Shadow-down/shadow-down-S/M/L`
  - `Shadows/Shadow-up/shadow-up-S/M/L`
  - `Shadows/Shadow custom/header-shadow`
  - `Blur/ageBlur`

Risk: local docs mention `Blur/appBlur`, but Figma currently exposes `Blur/ageBlur`. Treat naming as DS debt to confirm.

### Icons

File: `DS - Icons`.

- Page: `Icons`.
- Component sets: `10`.
- Components: `182`.
- Sets:
  - `Icon / Outline` - `95` variants
  - `Icon / Placeholder` - `7`
  - `Icon / Pickup Point` - `8`
  - `Icon / Map pins` - `23`
  - `Icon / Filled` - `11`
  - `Icon / Catalog` - `18`
  - `Checkout Icons` - `9`
  - `Иконки СПЗ` - `4`
  - `Icon / Map pins / Наличие` - `2`
  - `Icon / fav` - `2`

Rule: actions and navigation use DS icon instances; do not draw local SVGs when a DS icon exists.

## 4. Component Layer

### Android Ui-kit

File: `Android Ui-kit`.

- Pages: `Project cover`, `❌ удалить после внедрения`, component pages, `🔴 Ошибки в компонентах`.
- Component sets: `98`.
- Components: `663`.
- Important pages:
  - `🏠 Accordion 🟢`
  - `🏠 Alert & Action 🟡`
  - `🏠 AppBar 🟢`
  - `🏠 Badge 🟢`
  - `🏠 Bottom Sheet 🟡`
  - `🏠 Button 🟢`
  - `🏠 Cell 🟢`
  - `🏠 Input Text 🟢`
  - `🏠 Loader 🟡`
  - `🏠 NavBar`
  - `🏠 Product card`
  - `🏠 Product photo`
  - `🏠 Search 🟡`
  - `🏠 Snackbar`
  - `🏠 Status Bar`
  - `🏠 Switcher`
  - `🏠 Tabs`

Core component sets:

- App and navigation: `AppBar / Default`, `Status Bar`, `navBar / set`, `navBar / icons`, `navBar / Bar`, `navBar / Cart`.
- Actions: `Button / Primary`, `Secondary`, `Dark`, `Error`, `Outline`, `Minimal`, `Floating`, `Social`, `QTY`.
- Forms: `Input / Text`, `Email`, `Phone`, `Password`, `Textarea`.
- Feedback: `Alert`, `ActionSheet`, `Alert Wrap`, `ActionSheet Wrap`, `Snackbar`, `Loader / Full Screen`.
- Sheets: `Bottom Sheet Header`, `Modal Handler`, `Bottom Sheet Actions`, `Bottom sheet master`, `Bottom sheet / text content`.
- Commerce: `Product card / Catalog`, `Product card / Cart`, `Product Photo`, `Product photo / Catalog`, `Product photo / Cart`, `Product photo / Slider`.
- Selection: `Switcher / Button`, `Switcher / Row`, checkbox, radio, tabs, segmented controls.

Rule: final app screens should reuse these components when they exist.

### Showcase

File: `Android ui elements showcase`.

- Acts as state-validation and changelog file.
- Mirrors UI-kit component pages.
- Some pages are empty at top-level but still define the expected reference taxonomy.
- Use it when variant behavior or states are unclear.

## 5. Template Layer

File: `Android templates`.

- Component sets: `234`.
- Components: `1213`.
- Main page groups:
  - `📁 Общие организмы`
  - `📁 Общие темплейты`
  - `📁 Главная`
  - `📁 Отзывы покупателей`
  - `📁 Регистрация, Вход, Восстановление`
  - `📁 Профиль`
  - `📁 Каталог`
  - `📁 Корзина`
  - `📁 Чекаут`
  - `📁 Магазины`
  - `📁 Акции`

High-value templates/organisms:

- `Template / Error Screen`
- `Bottom sheet / info variants`
- `Organism / Profile / Navbar`
- `Organism / Profile header`
- `Organism / Profile / block row`
- `Organism / Profile / block rows set`
- `Template / Login`
- `Template / Registration`
- `Template / Card Registration`
- `Template / Password Recovery`
- `Tempalate / Catalog / Main`
- `Tempalate / Catalog / Category`
- `Tempalate / Catalog / Search`
- `Cart Summary`
- `Add to Cart`
- `Shipping templates`
- `Payment Options`
- `Org / Check-out / Delivery Methods`
- `Org / Check-out / Total`
- `Template / TYP/*`

Important current DS debt:

- Subscriptions source component set is named `Subscrptions / Switchers` with typo.
- It has two variants: `user=true` and `user=false`.
- It is built from `Switcher` instances and dividers.
- The source contains placeholder-like nested text layers. Existing DS-only canvas hides/overrides visible placeholders, but source cleanup is still needed.

## 6. Legacy App Structure

File: `Mobile App - Android`.

- Page count: `43`.
- Role: old app reference for flows, states, edge cases and historical behavior.

Top-level product areas:

- Errors
- Home
- Search
- First launch / localization
- Onboarding
- Animations
- Stories
- App update
- Fix Price card
- Popups
- Reviews
- Registration / Login
- Password recovery
- Confirmation errors
- App rating
- Profile
- Notification center
- Settings
- Pickup/delivery point selection
- Favorite addresses
- Profile completion
- My purchases
- Promocodes
- Favorite categories
- Help
- Favorite products
- Legal information
- Subscriptions
- Account deletion
- Catalog
- Product card
- Cart
- Checkout
- TYP / order success
- Stores
- Promotions
- Epics
- Alcohol / 18+ goods
- Promo code on order legacy branch

Observed scenario-rich legacy sections:

- `Регистрация, Вход`: MTS ID primary/secondary login, VK ID primary/secondary login, loader, unavailable login options, error variants, normal registration form.
- `Выбор СПЗ`: delivery, pickup, pickup point, intermediate selection screen, city change.
- `Чекаут`: pickup, pickup point, delivery, private cases, quick order.
- `TYP`: pickup point, courier, express delivery, processing orders.
- `Избранные товары`: MVP and post-MVP branches.
- `Подписки`: auth/anon subscriptions, push/system settings branch, electronic receipts/email confirmation branch, loaders, error modals, no-letter bottom sheet, success, RU/KZ banner split.

Legacy rule: do not copy visual style or detached components from this file into final v2.0. Copy scenarios and states only.

## 7. Android v2.0 Structure

File: `Android v2.0`.

- Page count: `43`.
- Role: target app layout file.
- Structure mirrors legacy at a high level, but many pages are empty or partial.

Current observed pages with content:

- `📁 Главная`
  - `Главная / Light`
  - `Главная / Dark`
- `↪️ Поиск`
  - search component sets: `search / search cell`, `search / brand logo`, `search / blocks`
- `↪️ Обновление приложения`
  - `Обновление приложения / Light`
  - `Обновление приложения / Dark`
- `📁 Профиль`
  - profile task sections, including user data masking, profile blocks, review block, confirm email design, favorite addresses, user statuses
- `↪️ Центр уведомлений`
  - Light/Dark sections
- `↪️ Настройки`
  - edit personal data, settings, change password sections
- `↪️ Любимые категории`
  - Light/Dark sections
- `↪️ Выбор СПЗ`
  - delivery, pickup, pickup point, intermediate screen, city change, duplicated Light/Dark lanes
- `↪️ Дополнение профиля`
  - Light/Dark sections
- `↪️ Подтверждение почты`
  - `Подверждение почты / Light`
  - `Подверждение почты / Dark`
- `↪️ Промокоды`
  - two Light sections
- `↪️ Правовая информация`
  - Light/Dark sections
- `↪️ Подписки`
  - current canonical section: `594:696`, `Подписки / DS-only restart / 2026-05-14`
- `📁 Чекаут`
  - `Чекаут / Light`
  - `Чекаут / Dark`

## 8. Current Subscriptions State

Target page: `Android v2.0 / ↪️ Подписки`, node `65:35667`.

Current canonical section:

- `594:696`
- `Подписки / DS-only restart / 2026-05-14`
- Size: `5200 x 5200`
- Top-level children: `54`
- Nested frames: `282`
- Nested instances: `447`

The current lane contains 20 explicit states:

1. Auth subscriptions
2. Anonymous subscriptions
3. Push settings alert
4. API error alert
5. RU banner split
6. KZ banner split
7. Email confirmed entry
8. Email unconfirmed entry
9. Email start
10. Email typed
11. Email invalid
12. Email sent
13. No-letter sheet
14. Email success
15. Email snackbar error
16. Email loader
17. Loader save push
18. Loader save email checks
19. Loader resend
20. Bottom sheet component

Current coverage notes inside the section:

- manual/scaffold section `586:1868` was deleted;
- subscription branch uses imported `Subscrptions / Switchers`;
- alert states use `Alert Wrap`;
- loaders use `Loader / Full Screen`;
- bottom sheet uses `Bottom sheet master`;
- email branch clones canonical states from `↪️ Подтверждение почты / Light`;
- remaining DS gaps are source component typo/placeholders, RU/KZ final legal copy, and missing dedicated email-check row variant.

## 9. Product And User Scenario Model

The app is a mobile commerce product for frequent value shopping. The core user jobs are:

- find a product quickly;
- understand price, discount, card price and stock availability;
- choose pickup/delivery context;
- add products to cart;
- checkout with correct recipient, address, delivery method, payment and loyalty settings;
- track order outcome;
- manage profile, addresses, favorites, notifications, subscriptions and legal settings.

Scenario clusters:

- Acquisition/onboarding:
  - first launch/localization;
  - onboarding;
  - country/city context.
- Discovery:
  - home feed;
  - search;
  - catalog categories;
  - product card;
  - stores/promotions.
- Commerce:
  - product selection;
  - cart;
  - checkout;
  - delivery/pickup/pickup point;
  - promo code;
  - loyalty program/card price;
  - TYP/order success.
- Account:
  - registration/login via phone, MTS ID, VK ID;
  - password recovery;
  - account/email confirmation;
  - profile completion;
  - account deletion.
- Retention/service:
  - notification center;
  - subscriptions;
  - electronic receipts;
  - app rating;
  - customer reviews;
  - favorite categories/products/addresses;
  - help/legal information.
- Risk/compliance:
  - alcohol and 18+ goods;
  - confirmation errors;
  - system errors;
  - unavailable states.

## 10. Migration Rules

For every legacy -> Android v2.0 task:

1. Start from legacy scenarios and states, not visuals.
2. Rebuild in `Android v2.0`.
3. Use foundations first: colors, typography, gaps, effects, icons.
4. Use `Android Ui-kit` for base components.
5. Use `Android templates` for organisms and screen templates.
6. Use `Showcase` when variants/states are unclear.
7. Do not create manual analogs where a DS component/template exists.
8. If a DS source is incomplete, mark a DS-gap instead of faking a final manual component.
9. Keep links between related pages explicit; do not duplicate existing flows such as `Подтверждение почты`.
10. Close only after:

```text
100% flow coverage
+ DS pass
+ QA pass
```

## 11. Open Risks And Gaps

- `Android v2.0` remains partially filled; many pages exist only as structure.
- Some component/page names have mixed RU/EN naming and typos.
- `Subscrptions / Switchers` typo and hidden placeholder text should be cleaned at DS source level.
- Local docs mention `Blur/appBlur`, Figma currently exposes `Blur/ageBlur`; naming needs confirmation.
- Some UI-kit component sets may have variant-property read issues; check variants visually/in showcase before large-scale reuse.
- Templates contain many local complex components; before creating new screens, verify they do not duplicate newer UI-kit components.
- Buildin/current kanban context is documented locally, but real kanban edits should be done only by Wiki Agent.
