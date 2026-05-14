# Fix Price Android System Map

Analyst reference for BFT decomposition, functional specs, migration tasks, and acceptance criteria for the Fix Price Android app.

## Executive Model

The Android product is maintained as a layered design system and migration pipeline:

```text
Business BFT
-> System analysis / decomposition
-> Legacy scenario audit in Mobile App - Android
-> DS reuse map from foundations, UI-kit, templates, showcase
-> Rebuild in Android v2.0
-> QA: legacy flow coverage + DS compliance + state coverage
```

For analytics work, the main task is not to describe screens as pictures. The task is to preserve product behavior and user scenarios from legacy, then specify how they are rebuilt with new variables, styles, components, and templates.

## Source Hierarchy

Use this order when resolving conflicts:

1. `design-system-map.md` and inspected Figma files.
2. `Android v2.0` as target implementation/design file.
3. `Android templates` for scenario-level patterns.
4. `Android Ui-kit` for base components.
5. Foundations: `DS - Colors`, `DS - Android typography`, `DS - Gaps`, `DS - effects`, `DS - Icons`.
6. `Android ui elements showcase` for state validation.
7. `Mobile App - Android` only for legacy scenarios, states, edge cases, and historical behavior.
8. `design-system.md` only when it does not conflict with Android DS.

## Figma Files And Roles

| Layer | File | Key | Role |
| --- | --- | --- | --- |
| Colors | `DS - Colors` | `xrrrRVKXHqifNnhd3cC1bN` | Semantic Light/Dark color variables |
| Typography | `DS - Android typography` | `ScDQwwKHyWya2YaKFpClWa` | Android text styles |
| Spacing | `DS - Gaps` | `1zQbV2SN44caC80Ib5eDMZ` | Gap scale and breakpoints |
| Effects | `DS - effects` | `pxURPtXGNxQPl2X6ZNn7fr` | Radius, shadows, blur |
| Icons | `DS - Icons` | `fgeRWdjJlsH7uBcFJcadjY` | Icon component sets |
| Base components | `Android Ui-kit` | `8eyN4wOGRSWnqqxEGXhheB` | Buttons, inputs, nav, product cards, sheets |
| Scenario patterns | `Android templates` | `GVjBHX6TemLKrZWKnOpfKm` | Complex organisms and screen templates |
| State examples | `Android ui elements showcase` | `PlMyc3INhqfVp2I7hDvInA` | Validation examples for component states |
| Target app | `Android v2.0` | `w6fzp4MqBpWjgSMGrZK0XD` | New app layouts rebuilt on DS |
| Legacy app | `Mobile App - Android` | `oOt1o1Ln0lxhbb3ZSvoOWg` | Old flows and behavior reference |

## Design System Relationships

### Foundations

- Colors: `Theme Colors`, Light/Dark, 140 variables. Key groups are `brand/*`, `background/*`, `text/*`, `button/*`, `icon/*`, `divider-border/*`, `opacity/*`, `shades/*`, `support colors/*`.
- Typography: 46 styles. Product UI uses Roboto. `Frame naming/*` styles are for canvas organization and must not be used as product text.
- Spacing: `Dimensions` collection with `Gap/2..64` and breakpoints `adaptive=375`, `tablet=768`, `desktop=1400`.
- Effects: radius variables `radius-XS/S/M/L/XL`, current `Shadows/*`, `Blur/appBlur=12`. `Shadows/Old/*` are legacy.
- Icons: 10 component sets, 182 components. Main sets include `Icon / Outline`, `Icon / Filled`, `Icon / Catalog`, `Icon / Pickup Point`, `Icon / Map pins`, `Icon / fav`, `Checkout Icons`.

### Component Layer

`Android Ui-kit` is the source for base reusable components:

- Buttons: primary, secondary, dark, error, outline, minimal, QTY, floating, social.
- Inputs: text, email, phone, password, textarea.
- Product: product card, catalog/cart variants, product photo, price variants.
- Navigation: AppBar, NavBar, tabs, segmented controls.
- Feedback and overlays: Alert, ActionSheet, Bottom Sheet, Snackbar, Informer, Loader, Modal Background.
- Commerce controls: Search, Product Slider, QTY, Radio Button, Checkbox, Upload Photo.

Known technical risk: several component sets throw Figma API errors when reading variant properties. For those, validate variants manually in the component page or showcase before freezing requirements.

### Template Layer

`Android templates` is the product-pattern layer. Use before custom assembly:

- General organisms and shared templates.
- Home, localization, stories, update app.
- Reviews, login/registration/recovery.
- Profile, favorite categories, notification center, settings.
- SPZ/store/pickup/delivery selection.
- Catalog, cart, checkout, stores, promotions.

Important reusable patterns include error screen, app rate, order feedback, login, registration, password recovery, profile header/block rows, checkout/cart summary, shipping/payment/recipient blocks, SPZ address cards, bottom sheet info/sort/date-time variants.

### Showcase Layer

`Android ui elements showcase` validates states, not source components. Use it to confirm default, selected, disabled, loading, error, empty, pressed/focus, Light/Dark behavior.

## Legacy App Product Scenarios

The old `Mobile App - Android` file has 43 pages. It is the source of product behavior and flow coverage.

### Core Sitemap

- Errors.
- Home.
- Search.
- First launch / localization.
- Onboarding.
- Animations.
- Stories.
- App update.
- Fix Price card.
- Popups.
- Customer reviews.
- Registration and login.
- Password recovery.
- Confirmation errors.
- App rating.
- Profile.
- Notification center.
- Settings.
- SPZ selection.
- Favorite addresses.
- Profile completion.
- My purchases.
- Promocodes.
- Favorite categories.
- Help.
- Favorite products.
- Legal info.
- Subscriptions.
- Account deletion.
- Catalog.
- Product card.
- Cart.
- Checkout.
- TYP.
- Stores.
- Promotions.
- Epics: alcohol / 18+, order promocode.

### Legacy Scenario Clusters

| Cluster | Legacy evidence | Analytical meaning |
| --- | --- | --- |
| Auth and registration | Primary/secondary login via MTS ID, primary/secondary login via VK ID, loader, unavailable login options, no-internet VK ID, ordinary registration form | Need external identity provider states, fallback registration, loader and error handling |
| Settings and account | User settings, personal data management, change password, subscriptions, app version, legal Yandex Maps terms | Need account data, credential/security flows, app/legal metadata |
| SPZ / fulfillment choice | Delivery, pickup, pickup point, intermediate transition screen, city change | Need fulfillment mode model, geo/city state, address selection, map/list behavior |
| Catalog | Catalog frames with product listing structure | Need category/product list, sorting/filtering, product cards, empty/loading/error |
| Product card | Product slider, all features, product information blocks | Need gallery, product attributes, stock/price/CTA, feature rows |
| Checkout | Pickup, pickup point, delivery, special cases, quick order | Need order placement by fulfillment mode and special-case branching |
| TYP | Pickup point, courier, express delivery, orders in processing | Need post-payment/result states by fulfillment mode |
| Favorites | Favorite products MVP and post-MVP, favorite categories | Need saved products/categories, MVP boundaries, empty states |
| Loyalty / Fix Price card | Charity donation with points, profile completion blocker before points write-off | Need loyalty points, donation, profile completeness gate |
| 18+ / alcohol | Profile action blocks and 18+ modal | Need age restriction flow, legal confirmation, blocked states |
| Stories / onboarding / app update | Stories components, onboarding sections, update app sections | Need engagement/education and forced/optional update states |

## Android v2.0 Target State

The new `Android v2.0` file also has 43 pages. It is the target location for rebuilt screens.

### Populated Or Started In Android v2.0

- Home: `Главная / Light`, `Главная / Dark`.
- Search: component sets `search / search cell`, `search / brand logo`, `search / blocks`; includes history, search, category, brand, recent searches, frequent searches.
- App update: Light and Dark sections.
- Profile: tasks/sections for hidden user data, profile blocks `Покупки`, `Прогр.лояльности`, `Адрес`, feedback block, confirm email, favorite addresses, user statuses.
- Notification center: Light and Dark.
- Settings: personal data editing, settings, password change.
- Favorite categories: Light and Dark.
- SPZ selection: delivery, pickup, pickup point, transition to SPZ selection, city change, duplicated Light/Dark-like section pairs.
- Profile completion: Light and Dark.
- Email confirmation: Light and Dark.
- Promocodes: Light sections.
- Legal info: Light and Dark.
- Subscriptions: `Подписки / DS-only restart / 2026-05-14`.
- Checkout: Light and Dark sections, each with pickup, pickup point, delivery, special cases, quick order.

### Empty Or Not Yet Rebuilt In Android v2.0

- Errors.
- First launch / localization.
- Onboarding.
- Animations.
- Stories.
- Fix Price card.
- Popups.
- Customer reviews.
- Registration and login.
- Password recovery.
- Confirmation errors.
- App rating.
- Favorite addresses.
- Account confirmation.
- My purchases.
- Help.
- Favorite products.
- Account deletion.
- Catalog.
- Product card.
- Cart.
- TYP.
- Stores.
- Promotions.

## Legacy To Android v2.0 Migration Map

Use this map during BFT decomposition:

| Legacy area | Android v2.0 target | Status | Required analytical action |
| --- | --- | --- | --- |
| Home | `📁 Главная` | Started | Map old home states to Light/Dark sections; verify full content coverage |
| Search | `↪️ Поиск` | Started with DS components | Specify search history, suggestions, categories, brands, clear action, empty/error states |
| Localization | `↪️ Первый запуск / Локализация` | Empty | Extract legacy first-launch city/country rules before design task |
| Onboarding | `↪️ Onboarding` | Empty | Preserve onboarding screens and branching |
| Stories | `↪️ Stories` | Empty | Preserve story states, close/fav/share/mute/comment/QA if relevant |
| App update | `↪️ Обновление приложения` | Started | Define optional/forced update behavior and error states |
| Fix Price card | `↪️ Карта Fix Price` | Empty | Preserve loyalty card, charity donation, profile-completion gate |
| Reviews | `📁 Отзывы покупателей` | Empty | Map order feedback/rating flow from templates/legacy |
| Auth | `📁 Регистрация, Вход` | Empty | Preserve MTS ID, VK ID, ordinary registration, loader, unavailable options, no-internet/errors |
| Profile | `📁 Профиль` plus child pages | Started | Split by profile blocks, statuses, hidden data, confirmation, favorites, purchases |
| Settings | `↪️ Настройки` | Started | Preserve account data, password, subscriptions, app/legal info |
| SPZ selection | `↪️ Выбор СПЗ` | Started | Preserve delivery/pickup/PVZ/city-change/map/list states |
| Favorite products | `↪️ Избранные товары` | Empty | Preserve MVP and post-MVP boundaries |
| Catalog | `📁 Каталог` | Empty | Preserve category list, products, filters/sort, states |
| Product card | `↪️ Карта товара` | Empty | Preserve gallery, product info, attributes, stock, CTA |
| Cart | `📁 Корзина` | Empty | Extract cart states from templates/legacy before rebuild |
| Checkout | `📁 Чекаут` | Started | Verify all fulfillment modes, special cases, quick order |
| TYP | `↪️ TYP` | Empty | Preserve pickup/courier/express/order-processing result states |
| Stores | `📁 Магазины` | Empty | Need legacy flow or business BFT before decomposition |
| Promotions | `📁 Акции` | Empty | Need legacy flow or business BFT before decomposition |
| 18+ | likely Profile/Product/Checkout modal areas | Not placed | Decide target placement and preserve legal gate |

## Product Entities For System Analysis

Use these entities when decomposing BFT:

- User profile.
- Auth session and external identity provider: MTS ID, VK ID.
- City / region.
- Store / pickup point / delivery address / SPZ.
- Fulfillment mode: delivery, pickup, pickup point, express.
- Product.
- Category.
- Brand.
- Product price, card price, promotion, discount.
- Stock / availability.
- Cart item and quantity.
- Order.
- Payment method.
- Recipient.
- Loyalty card / points.
- Donation / charity.
- Favorite product.
- Favorite category.
- Notification.
- Subscription.
- Promocode.
- App version / update state.
- Age restriction / 18+ confirmation.
- Review / rating / feedback.

## BFT Decomposition Rules

For every BFT item, produce tasks by scenario and state, not by visual fragment.

Each decomposed task should include:

- Legacy source page/section.
- Android v2.0 target page/section.
- Related template and UI-kit components.
- Data entities and fields.
- Business rules.
- User flow and navigation/back behavior.
- Component and system states.
- Light/Dark requirement.
- Edge cases.
- Acceptance criteria.
- Open decisions for business, DS, UI, backend, mobile, QA.

## Acceptance Criteria Pattern

Use this checklist before saying a migration task is complete:

- Legacy flow is fully covered.
- Every full-screen screen and modal/bottom sheet is accounted for.
- All known states are covered: default, loading, empty, error, disabled, selected, success, offline/no internet, blocked by missing data.
- Navigation and return paths are specified.
- Light/Dark behavior is specified or explicitly out of scope.
- DS components/templates are reused.
- Tokens/styles are semantic, not hardcoded.
- Any manual component exception is documented and approved by DS/Lead.
- QA can trace each acceptance criterion back to legacy and Android v2.0 target.

## Known Risks

- Figma sections often do not expose all spatially contained screens as `children` via API; manual visual check may still be needed for exact frame coverage.
- Some `Android Ui-kit` component sets have unreadable variant properties via API.
- `Android v2.0` is partially migrated; many pages are placeholders.
- Some duplicated section names exist in Android v2.0, especially Light/Dark or repeated Light sections. The task owner must confirm whether duplicates are intentional.
- Legacy naming mixes Russian, English, typos, and temporary labels. Requirements should normalize terminology without losing source references.
