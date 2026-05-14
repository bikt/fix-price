# Superpower UX Researcher Full App / Design System Study — 2026-05-14

Агент: `superpower-ux-researcher`

Цель: зафиксировать рабочее понимание дизайн-системы Fix Price, связей между Figma-артефактами, старым Android-приложением и новым `Android v2.0`, чтобы дальше выполнять UX/research-задачи и миграционные проверки в оркестрации FP Lead Agent.

## 1. Источники

Локальные источники:

- `FP Lead Agent/PROJECT_CONTEXT.md`
- `FP Lead Agent/design-system-map.md`
- `FP Lead Agent/design-system.md`
- `FP Lead Agent/data-model.md`
- `FP Lead Agent/AGENTS.md`
- `FP Lead Agent/TEAM_AGENT_ARCHITECTURE_PLAYBOOK.md`
- `FP Lead Agent/LEGACY_TO_NEW_MIGRATION_TEMPLATE.md`
- `FP Lead Agent/UI_AGENT_DESIGN_MEMORY.md`
- `FP Lead Agent/UI_AGENT_SYNC_FULL_DESIGN_STUDY_2026-05-14.md`
- `FP Lead Agent/UI_AGENT_SYNC_DESIGN_FILES_STRUCTURE_2026-05-14.md`
- `FP Lead Agent/UI_AGENT_SYNC_SUBSCRIPTIONS_*_2026-05-14.md`
- `.agents/superpower-ux-researcher/DESIGN_SYSTEM_RESEARCH_MEMORY.md`

Figma sources:

| Layer | File | Key | Role |
| --- | --- | --- | --- |
| Foundations | `DS - Colors` | `xrrrRVKXHqifNnhd3cC1bN` | Color variables and gradients |
| Foundations | `DS - Android typography` | `ScDQwwKHyWya2YaKFpClWa` | Android text styles |
| Foundations | `DS - Gaps` | `1zQbV2SN44caC80Ib5eDMZ` | Spacing and breakpoint variables |
| Foundations | `DS - effects` | `pxURPtXGNxQPl2X6ZNn7fr` | Radius, shadow and blur styles |
| Foundations | `DS - Icons` | `fgeRWdjJlsH7uBcFJcadjY` | Icon component sets |
| Components | `Android Ui-kit` | `8eyN4wOGRSWnqqxEGXhheB` | Base Android components |
| Templates | `Android templates` | `GVjBHX6TemLKrZWKnOpfKm` | Complex organisms and screen templates |
| Validation | `Android ui elements showcase` | `PlMyc3INhqfVp2I7hDvInA` | Component states and examples |
| Target app | `Android v2.0` | `w6fzp4MqBpWjgSMGrZK0XD` | New app layouts |
| Legacy app | `Mobile App - Android` | `oOt1o1Ln0lxhbb3ZSvoOWg` | Old app scenario reference |

## 2. System Architecture

The working design stack is layered:

```text
Foundations
  -> Android Ui-kit
    -> Android templates
      -> Android ui elements showcase for state validation
        -> Android v2.0 target layouts
          <- Mobile App - Android as legacy scenario reference
```

Priority rule:

1. Use foundation variables/styles first.
2. Use `Android Ui-kit` for base controls and components.
3. Use `Android templates` for complex product patterns.
4. Use showcase to verify states.
5. Build new layouts in `Android v2.0`.
6. Use legacy only to understand flows, states, branches and edge cases.

Legacy must not be used as a source of current visual styles, tokens or components.

## 3. Foundations

### Colors

Figma-confirmed:

- Local variable collection: `Theme Colors`.
- Modes: `Light`, `Dark`.
- Count: `140` variables.
- Paint styles: `13`, mainly gradients and preloader styles.

Core groups:

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

Key action tokens from local map:

- `brand/color-01`: `#91C30F`
- `brand/color-02`: `#0F4193`
- `background/bg-accent`: `#81BB3C`
- `background/bg-info`: Light `#3C7BE0`, Dark `#528AE3`
- `background/bg-negative`: Light `#E81B0C`, Dark `#F3291A`
- `button/button-primary`: `#81BB3C`
- `button/button-dark`: Light `#0F4193`, Dark `#114CAA`

Research / UX implication: when auditing screens, color findings should be expressed as token compliance, affordance, hierarchy and accessibility issues, not as arbitrary color preferences.

### Typography

Figma-confirmed:

- `46` local text styles.
- Main Android UI font: `Roboto`.
- Organization/frame naming uses `Inter`.

Core styles:

- `Heading/H1` 24/27 ExtraBold.
- `Heading/H2` 21/22 SemiBold.
- `Heading/H3` 19/23 Medium.
- `Heading/H4` 16/20 Medium.
- `Body/body-17..13` with regular, semibold, bold, strike, underline variants.
- `Caps/*`, including badge, nav and overline.
- `etc/button`.
- `etc/bpc-price`.

Research / UX implication: text critique should check not only copy clarity, but whether hierarchy follows available text styles, especially for price, CTA, errors and status labels.

### Spacing

Figma-confirmed:

- Local variable collection: `Dimensions`.
- Count: `15` variables.

Variables:

- Breakpoints: `Breakpoint/desktop`, `Breakpoint/tablet`, `Breakpoint/adaptive`.
- Gap scale: `Gap/2`, `Gap/4`, `Gap/8`, `Gap/12`, `Gap/16`, `Gap/20`, `Gap/24`, `Gap/32`, `Gap/40`, `Gap/48`, `Gap/56`, `Gap/64`.

Research / UX implication: density is intentional for retail, but dense screens still need scannable grouping, predictable rhythm and touch-safe spacing.

### Effects

Figma-confirmed:

- Radius collection: `radius-XS`, `radius-S`, `radius-M`, `radius-L`, `radius-XL`.
- Blur collection has `ageBlur` naming in Figma; local map calls it `appBlur`. Treat as naming mismatch to verify before implementation.
- Effect styles: 8.

Styles:

- `Shadows/Shadow-down/shadow-down-S`
- `Shadows/Shadow-down/shadow-down-M`
- `Shadows/Shadow-down/shadow-down-L`
- `Shadows/Shadow-up/shadow-up-S`
- `Shadows/Shadow-up/shadow-up-M`
- `Shadows/Shadow-up/shadow-up-L`
- `Shadows/Shadow custom/header-shadow`
- `Blur/ageBlur`

Research / UX implication: modal, bottom-sheet, sticky and elevated elements should use known effect styles. Any custom shadow/radius should be flagged as DS risk.

### Icons

Figma-confirmed:

- `10` component sets.
- `182` components.

Sets:

- `Icon / Outline` — 95 variants.
- `Icon / Placeholder` — 7.
- `Icon / Pickup Point` — 8.
- `Icon / Map pins` — 23.
- `Icon / Filled` — 11.
- `Icon / Catalog` — 18.
- `Checkout Icons` — 9.
- `Иконки СПЗ` — 4.
- `Icon / Map pins / Наличие` — 2.
- `Icon / fav` — 2.

Research / UX implication: icon usage matters in navigation, product favorite actions, pickup/delivery selection and map/store flows. If an icon is unavailable, that is a DS gap, not an invitation to draw local icons silently.

## 4. Android Ui-kit Layer

Figma-confirmed:

- `98` component sets.
- `663` components.

Core pages and components:

- `Alert & Action`: `Alert`, `ActionSheet`.
- `AppBar`: `AppBar / Default`.
- `Badge`: `Badge / Navbar`.
- `Bottom Sheet`: `Bottom Sheet Header`, `Bottom Sheet Actions`, `Bottom sheet / text content`.
- `Button`: `Primary`, `Secondary`, `Dark`, `Error`, `Outline`, `Minimal`, `QTY`, `Floating`, `Social`.
- `Checkbox`: button and icon variants.
- `Input Text`: text, email, phone, password, textarea, product comment, app feedback.
- `NavBar`: set, icons, profile icon, bar, cart dynamic, cart.
- `Product`: price tag, product card cart/catalog, product photo catalog/cart/slider.
- `QTY`, `Radio Button`, `Search`, `Switcher`, `Tabs`, `Snackbar`, `Loader`, `Keyboard`, `Stories`.

Important state model:

- Buttons include normal, pressed, loading, disabled, sizes and fixed backgrounds.
- Inputs include filled, focus, disabled, editable, footer, error states.
- Search includes app/default variants.
- Product card/photo and cart components encode key commerce states.

Research / UX implication: when evaluating a flow, ask whether each state exists and is reachable: default, loading, empty, error, disabled, selected, pressed/focus, success.

## 5. Android Templates Layer

Figma-confirmed:

- Templates cover product-level organisms and screen patterns across app areas.

Key groups:

- Common organisms and templates.
- Main screen.
- First launch / localization.
- Stories.
- App update.
- Order feedback.
- Login, registration, recovery.
- Profile.
- Favorite categories.
- Notification center.
- Settings.
- СПЗ selection.
- Favorite addresses.
- Profile completion.
- My purchases.
- Promocodes.
- Legal information.
- Subscriptions.
- Account deletion.
- Catalog.
- Product card.
- Cart.
- Checkout.
- TYP.
- Shops.
- Promotions.

High-value template patterns:

- `Template / Error Screen`.
- `Organism / App Rate`.
- `Bottom sheet / info variants` with many informational sheet variants.
- `Template / Login`, `Template / Registration`, `Template / Password Recovery`.
- `Подписки` template in registration/login/recovery page.
- Profile header, blocks, loyalty, notifications, icons.
- СПЗ tabs, address cards, filters, pickup/delivery info.
- Promocode blocks, inputs and informers.
- Catalog main/category/search, filters, sorting, category tiles.
- Big Product Card variants by auth state and SPZ state.
- Cart items, informers, summary, buttons, navbar.
- Checkout recipient, payment, order settings.
- TYP order info and post-order states.
- Order feedback templates with rating, emoji, questions and textarea.

Research / UX implication: templates already encode many moments for collecting user feedback: app rate, order feedback, story QA/comment, app feedback textarea, error screens, bottom sheets and promo/profile flows.

## 6. Legacy App Structure

Figma-confirmed legacy file:

- File: `Mobile App - Android`.
- Pages: `43`.
- Sections: `28`.
- Frames: `255`.
- Components: `21`.
- Instances: `141`.

Legacy is a scenario/reference file. It contains historical screens, branches and edge cases. It should be studied before migration, then rebuilt with new DS components.

Observed legacy scenario areas:

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
- Order/customer feedback.
- Login and registration:
  - MTS ID primary/secondary login.
  - VK ID primary/secondary login.
  - Loaders.
  - Unavailable login options.
  - Internet/error states.
  - Classic registration form.
- Password recovery.
- Confirmation errors.
- App rating.
- Profile.
- Notification center.
- Settings.
- СПЗ selection:
  - delivery;
  - self pickup;
  - pickup point;
  - transition to СПЗ selection;
  - city change.
- Favorite addresses.
- Profile completion.
- My purchases.
- Promocodes.
- Favorite categories.
- Help.
- Favorite products:
  - MVP;
  - post-MVP.
- Legal information.
- Subscriptions.
- Account deletion.
- Catalog.
- Product card.
- Cart.
- Checkout:
  - self pickup;
  - pickup point;
  - delivery;
  - special cases;
  - quick order.
- TYP:
  - pickup point;
  - courier;
  - express delivery;
  - orders in processing.
- Shops.
- Promotions.
- Epics:
  - alcohol / 18+ goods;
  - order promocode marked for deletion.

Research implication: the real product is not just shopping. It includes identity, loyalty/profile, location and fulfillment, post-order, feedback, legal/privacy, subscription/communication preferences and special regulated-goods flows.

## 7. Android v2.0 Target State

Figma-confirmed `Android v2.0` currently has these non-empty pages/sections:

- `Главная`: `Главная / Light`, `Главная / Dark`.
- `Поиск`: component sets `search / search cell`, `search / brand logo`, `search / blocks`.
- `Обновление приложения`: Light and Dark.
- `Профиль`: multiple task sections for hidden user data, profile blocks, leave-review block, email confirmation, favorite addresses, user statuses.
- `Центр уведомлений`: Light and Dark.
- `Настройки`: edit personal data, settings, password change sections, with apparent duplicates.
- `Любимые категории`: Light and Dark.
- `Выбор СПЗ`: delivery, self pickup, pickup point, transition screen, city change; duplicated likely for Light/Dark or iteration pairs.
- `Дополнение профиля`: Light and Dark.
- `Подтверждение почты`: Light and Dark.
- `Промокоды`: two Light sections.
- `Правовая информация`: Light and Dark.
- `Подписки`: current section `Подписки / DS-only restart / 2026-05-14`.
- `Чекаут`: Light and Dark.

Notable current gaps / caution:

- Many pages exist as structure but are empty in `Android v2.0`.
- Some sections are duplicated or have naming inconsistencies, such as duplicated Light labels.
- `Подписки` appears to have a newer `DS-only restart` section. Earlier UI Agent sync files mention previous section IDs and a sequence of rebuild attempts. Treat current Figma state as source of truth and sync files as history.
- Current target file is a migration workspace, not a fully finished app map.

Research implication: when evaluating readiness, do not confuse "page exists" with "flow complete." Check sections, states, transitions and parity with legacy.

## 8. Product And User Scenario Map

### Commerce Discovery

Scenarios:

- open app / home;
- discover promotions and main content;
- search by query;
- browse catalog;
- filter/sort category;
- inspect product card;
- understand price, card price, promo, availability;
- add product to cart or favorite.

Research questions:

- Can the user find the desired product quickly?
- Do search and catalog language match user vocabulary?
- Are price, discount and card-price conditions clear?
- Are out-of-stock and notify-me states understandable?

Metrics:

- search success rate;
- zero-result search rate;
- product detail view rate;
- add-to-cart conversion;
- favorite action rate;
- filter usage and reset rate.

### Product Decision

Scenarios:

- open product card;
- view gallery;
- read characteristics;
- compare availability by selected СПЗ/city;
- choose cart action.

Research questions:

- Is enough information visible before the CTA?
- Does the user understand availability and fulfillment constraints?
- Is price hierarchy stronger than secondary details?

Metrics:

- PDP-to-cart conversion;
- product card bounce;
- scroll depth to characteristics;
- support contacts about price/availability.

### Cart And Checkout

Scenarios:

- view cart;
- change quantity;
- see unavailable/changed items;
- apply promocode;
- select recipient;
- choose fulfillment;
- choose payment;
- place order.

Research questions:

- Does the user understand the final price and blockers?
- Are cart and checkout abandonment reasons visible?
- Are delivery/pickup differences clear?

Metrics:

- cart-to-checkout conversion;
- checkout completion;
- quantity change errors;
- promocode error rate;
- support contacts during checkout.

### Fulfillment And Location

Scenarios:

- choose city;
- choose СПЗ;
- choose delivery;
- choose self pickup;
- choose pickup point;
- switch city/store/point;
- understand availability.

Research questions:

- Does the user understand why location is needed?
- Can the user confidently choose between delivery/self pickup/pickup point?
- Are map, availability and pickup conditions clear?

Metrics:

- СПЗ selection completion;
- city change completion;
- fulfillment switch rate;
- pickup/delivery support contacts.

### Identity And Profile

Scenarios:

- login via MTS ID / VK ID;
- classic registration;
- password recovery;
- confirm email/account;
- edit personal data;
- complete profile;
- manage favorite addresses;
- manage favorite categories/products;
- manage subscriptions;
- delete account.

Research questions:

- Which login method is understood and trusted?
- Are error and recovery paths clear?
- Do users understand why profile data is requested?
- Do subscription settings map to user expectations?

Metrics:

- login completion;
- registration completion;
- recovery success;
- email confirmation success;
- profile completion;
- subscription opt-in/out rate.

### Loyalty, Promotions And Retention

Scenarios:

- Fix Price card / loyalty blocks;
- favorite categories;
- promocodes;
- promotions;
- stories;
- push/system settings;
- notification center.

Research questions:

- Does the user understand personal benefit?
- Are promotions useful without visual noise?
- Do notifications feel controllable?

Metrics:

- promo engagement;
- promocode activation;
- notification opt-in;
- loyalty block CTR;
- story interaction.

### Feedback And Post-order

Scenarios:

- app rating;
- order feedback;
- TYP;
- order status;
- feedback after order/pickup/delivery;
- support/help.

Research questions:

- Are feedback questions timed correctly?
- Can feedback identify actionable UX/product issues?
- Do post-order screens set expectations?

Metrics:

- CSAT/CES;
- order feedback completion;
- negative feedback topic distribution;
- repeat support contact.

### Special And Risk Flows

Scenarios:

- alcohol / 18+ goods;
- legal information;
- unavailable login options;
- no internet;
- system errors;
- loaders and empty states;
- app update.

Research questions:

- Are constraints explained before they block the user?
- Does the error state provide a next step?
- Are legal and age-related flows understandable?

Metrics:

- error recovery rate;
- abandon after restriction;
- update acceptance;
- legal/18+ support contacts.

## 9. Migration Model: Legacy -> Android v2.0

Migration is not visual copying. It is scenario reconstruction.

A migration is accepted only when:

```text
100% flow coverage
+ DS pass
+ QA pass
```

Required migration coverage:

- all full-screen legacy screens;
- all meaningful states;
- all branches;
- all transitions and returns;
- all loading, error, empty, disabled, success states;
- all cross-links to related flows;
- DS components/templates used where available;
- no orphan frames;
- no manually built analog when DS component/template exists.

Recommended role split:

- Lead Agent: orchestration and final decision.
- Analytic Agent: scope, states, dependencies, acceptance criteria.
- Design System Agent: component/template reuse map and DS gaps.
- UI Agent: Figma rebuild.
- QA Agent: coverage, DS and state-by-state verification.
- Superpower UX Researcher: user scenario integrity, research questions, friction points, feedback instrumentation and metric framing.

## 10. Researcher Operating Memory

When asked to review or support any Fix Price task:

1. Identify the scenario and whether it is legacy, new, or migration.
2. Check source hierarchy:
   - foundations;
   - UI-kit;
   - templates;
   - showcase;
   - Android v2.0;
   - legacy.
3. Translate UX issue into:
   - user behavior;
   - affected scenario;
   - business metric;
   - evidence source;
   - confidence level.
4. Check whether the issue is:
   - UX logic;
   - DS compliance;
   - missing state;
   - broken migration coverage;
   - unclear copy;
   - research gap.
5. Recommend next action:
   - quick UI/UX fix;
   - DS/template fix;
   - QA check;
   - usability test;
   - analytics check;
   - micro-survey/user feedback hook.

## 11. Feedback Collection Opportunities

Good moments for user opinion collection:

- Search with no result: "Что вы пытались найти?"
- Search result without product click/add-to-cart: "Нашли нужный товар?"
- Product card/PDP: "Достаточно ли информации для выбора?"
- Out of stock: demand signal and notify-me intent.
- Cart abandonment: "Что мешает оформить заказ?"
- Checkout abandonment: stage-specific reason question.
- Promocode error: "Что пошло не так с промокодом?"
- СПЗ selection: "Удобно ли выбрать способ получения?"
- City/store change: "Нашли нужный город/магазин?"
- Login/registration error: one-tap error reason and recovery clarity.
- Email confirmation/subscriptions: "Понятно ли, какие уведомления вы получите?"
- Order completion: CES/CSAT.
- Order feedback/TYP: structured reason tags + optional text.
- Error screens: "Сообщить о проблеме" with scenario metadata.

## 12. Open Risks

- `Android v2.0` is a migration workspace, not a complete app source of truth.
- Several target pages are empty or partially filled.
- Some new sections are duplicated or have ambiguous Light/Dark labels.
- `Подписки` has recent conflicting history in sync files; current Figma section is `DS-only restart / 2026-05-14`.
- UI-kit variant properties can be unreliable through Figma API for some sets; verify in component pages/showcase for critical work.
- Naming is mixed Russian/English and contains typos (`tetriary`, `Infromer`, `Tempalate`, `Подтвеждение`, etc.).
- Local `design-system.md` describes broader/web Fix Price rules and can differ from Android DS; Android map wins for Android app work.
- `Blur/appBlur` vs `Blur/ageBlur` naming mismatch should be checked before implementation.
- Legacy pages with `0` top-level nodes may still be meaningful if content is nested or hidden; use specific node IDs from Lead/Analytic handoff when available.

## 13. Final Working Rule

For every future task from FP Lead Agent or direct sidebar task:

- send start sync to FP Lead Agent;
- perform only role-appropriate work unless explicitly assigned otherwise;
- preserve DS and migration hierarchy;
- return final sync with artifacts, checked sources, risks and requested Lead decision.
