# Fix Price Android Design System Mockups - Analyst Memory

Use this reference when doing systems analysis for Fix Price Android app features, requirements, BFT/BRD, functional specs, edge cases, acceptance criteria, or design-to-development decomposition.

## Source Of Truth

- Primary map: `design-system-map.md`.
- Current app file: `Android v2.0`, Figma key `w6fzp4MqBpWjgSMGrZK0XD`.
- Legacy app file: `Mobile App - Android`, Figma key `oOt1o1Ln0lxhbb3ZSvoOWg`, reference only.
- Foundation files:
  - `DS - Colors`, key `xrrrRVKXHqifNnhd3cC1bN`.
  - `DS - Android typography`, key `ScDQwwKHyWya2YaKFpClWa`.
  - `DS - Gaps`, key `1zQbV2SN44caC80Ib5eDMZ`.
  - `DS - effects`, key `pxURPtXGNxQPl2X6ZNn7fr`.
  - `DS - Icons`, key `fgeRWdjJlsH7uBcFJcadjY`.
- Component files:
  - `Android Ui-kit`, key `8eyN4wOGRSWnqqxEGXhheB`.
  - `Android templates`, key `GVjBHX6TemLKrZWKnOpfKm`.
  - `Android ui elements showcase`, key `PlMyc3INhqfVp2I7hDvInA`.

If `design-system.md` conflicts with `design-system-map.md` or Figma inspection, use `design-system-map.md` and inspected Figma data for Android work.

## Build Order

1. Define the user scenario, role, entry point, success outcome, and business rule.
2. Check `Android v2.0` for an existing target page or section.
3. Check `Android templates` for ready scenario-level organisms/templates.
4. Check `Android Ui-kit` for base components.
5. Check foundations for colors, typography, spacing, radius, effects, and icons.
6. Check `Android ui elements showcase` when component states are ambiguous.
7. Use legacy app only to understand old behavior, edge cases, or historical flow.

## Foundations

### Colors

- File has `Theme Colors` variable collection.
- Modes: `Light`, `Dark`.
- Variable count: `140`.
- Key groups: `brand/*`, `background/*`, `text/*`, `button/*`, `icon/*`, `divider-border/*`, `opacity/*`, `app preloader/*`, `shades/*`, `support colors/*`.
- Important action colors:
  - `brand/color-01`: `#91C30F`.
  - `brand/color-02`: `#0F4193`.
  - `background/bg-accent`: `#81BB3C`.
  - `background/bg-info`: Light `#3C7BE0`, Dark `#528AE3`.
  - `background/bg-negative`: Light `#E81B0C`, Dark `#F3291A`.
  - `button/button-primary`: `#81BB3C`.
  - `button/button-dark`: Light `#0F4193`, Dark `#114CAA`.
- Analyst rule: specify semantic token use, not raw hex, in requirements and handoff notes.

### Typography

- File has `46` text styles.
- Product UI font: `Roboto`.
- Frame naming/cover styles use `Inter`; do not use them for product text.
- Key styles:
  - `Heading/H1`: 24/27, Roboto ExtraBold.
  - `Heading/H2`: 21/22, Roboto SemiBold.
  - `Heading/H3`: 19/23, Roboto Medium.
  - `Heading/H4`: 16/20, Roboto Medium.
  - `Body/body-17`, `Body/body-16`, `Body/body-15`, `Body/body-14`, `Body/body-13`.
  - Body modifiers: `-sb`, `-b`, `-st`, `-und`.
  - `Caps/caps-12`, `Caps/caps-12-sb`, `Caps/caps-10-sb`, `Caps/caps-nav`, `Caps/caps-badge`, `Caps/caps-overline`.
  - Price-related: `Caps/price-sub`, `Caps/price-sub-st`, `etc/bpc-price`.
  - Button text: `etc/button`.

### Spacing

- File has `Dimensions` variable collection.
- Variable count: `15`.
- Breakpoints:
  - `Breakpoint/adaptive`: `375`.
  - `Breakpoint/tablet`: `768`.
  - `Breakpoint/desktop`: `1400`.
- Gap scale: `2`, `4`, `8`, `12`, `16`, `20`, `24`, `32`, `40`, `48`, `56`, `64`.
- Analyst rule: acceptance criteria for layout should reference `Gap/*`, not arbitrary spacing.

### Effects

- Radius variables:
  - `radius-XS`: `4`.
  - `radius-S`: `8`.
  - `radius-M`: `16`.
  - `radius-L`: `24`.
  - `radius-XL`: `32`.
- Blur:
  - `Blur/appBlur`: `12`.
- Current shadows:
  - `Shadows/Shadow-down/shadow-down-S`: `0 4 12 rgba(0,0,0,.08)`.
  - `Shadows/Shadow-down/shadow-down-M`: `0 8 24 rgba(0,0,0,.16)`.
  - `Shadows/Shadow-down/shadow-down-L`: `0 12 32 rgba(0,0,0,.16)`.
  - `Shadows/Shadow-up/shadow-up-S`: `0 -4 12 rgba(0,0,0,.08)`.
  - `Shadows/Shadow-up/shadow-up-M`: `0 -8 24 rgba(0,0,0,.16)`.
  - `Shadows/Shadow-up/shadow-up-L`: `0 -12 32 rgba(0,0,0,.16)`.
  - `Shadows/Shadow custom/header-shadow`: `0 2 24 -8 rgba(112,138,176,.20)`.
- Legacy group `Shadows/Old/*` exists. Do not use for new specs unless explicitly preserving old behavior.

### Icons

- File has `10` component sets and `182` components.
- Main sets:
  - `Icon / Outline`: 95 variants, property `Icon`.
  - `Icon / Placeholder`: 7 variants, property `Size`.
  - `Icon / Pickup Point`: 8 variants, property `Service`.
  - `Icon / Map pins`: 23 variants, properties `Picked`, `Type`, `inStock`.
  - `Icon / Filled`: 11 variants, properties `icon`, `filled`.
  - `Icon / Catalog`: 18 variants.
  - `Checkout Icons`: 9 variants.
  - `Иконки СПЗ`: 4 variants.
  - `Icon / Map pins / Наличие`: 2 variants.
  - `Icon / fav`: 2 variants, property `active`.
- Analyst rule: for any action requiring an icon, specify the semantic icon need and expected state; designer/developer should reuse DS icon sets.

## Android Ui-kit

- File has `44` pages.
- Component sets: `97`.
- Components: `661`.
- Main page groups:
  - `Accordion`, `Alert & Action`, `AppBar`, `Badge`, `Bottom Sheet`, `Button`, `Cell`, `Checkbox`, `Date picker`, `Dropdown`, `Informer`, `Input Text`, `Keyboard`, `Loader`, `Main Slider`, `Modal Background`, `NavBar`, `Photo Indicator`, `Price tag`, `Product card`, `Product photo`, `Product Slider`, `Property Row`, `QTY`, `Radio Button`, `Search`, `Segmented Controls`, `Snackbar`, `Status Bar`, `Stories`, `Switcher`, `Tabs`, `Upload Photo`.
- Important component sets for product requirements:
  - Buttons: `Button / Primary`, `Button / Secondary`, `Button / Dark`, `Button / Error`, `Button / Outline`, `Button / Minimal`, `Button / QTY`, `Button / Floating`, `Button / Social`.
  - Inputs: `Input / Text`, `Input / Email`, `Input / Phone`, `Input / Password`, `Input / Textarea`.
  - Product and price: `Card / Product card`, `Product card / Catalog`, `Product card / Cart`, `Price / Cart`, `Price / TYP`, `Price / BPC / Prices variants`.
  - Media: `Product photo / Catalog`, `Product photo / Cart`, `Product photo / Slider`, `Product Photo`.
  - Search: `Search Bar / App`, `Search Bar / Default`, `Search Bar / Shops`.
  - Navigation: `navBar / set`, `navBar / icons`, `navBar / profile icon`, `navBar / Bar`, `navBar / Cart dinamic`.
  - Bottom sheets: `Bottom Sheet Header`, `Bottom Sheet Actions`, `Bottom sheet / text content`, `Bottom sheet master`.
- There is a page named `❌ удалить после внедрения`; do not treat it as the target source for new work unless a needed component exists only there and DS owner approves.
- Known issue: some component sets throw Figma API errors when reading variant properties. For affected components, validate states manually in Figma/showcase before freezing requirements.

## Android Templates

- File has `36` pages.
- Component sets: `235`.
- Components: `1219`.
- Use this as scenario/product pattern layer, above UI-kit.
- Main scenario areas:
  - `Общие организмы`.
  - `Общие темплейты`.
  - `Главная`.
  - `Первый запуск / Локализация`.
  - `Stories`.
  - `Обновление приложения`.
  - `Отзывы покупателей`.
  - `Регистрация, Вход, Восстановление`.
  - `Профиль`.
  - `Любимые категории`.
  - `Центр уведомлений`.
  - `Настройки`.
  - `Выбор СПЗ`.
  - `Каталог`.
  - `Корзина`.
  - `Чекаут`.
  - `Магазины`.
  - `Акции`.
- Important template/organism examples:
  - Error and feedback: `Template / Error Screen`, `Organism / Error screen content`, `Template / App rate`, `Template / Order Feedback / Rate 5`, `Template / Order Feedback / Rate 3`.
  - Auth: `Template / Login`, `Template / Registration`, `Template / Registration Data`, `Template / Card Registration`, `Template / Password Recovery`.
  - Profile: `Organism / Profile header`, `Organism / Profile / block row`, `Organism / Profile / block rows set`, `Organism / Profile / Navbar`, `Organism / Profile / Login`.
  - Checkout/cart: `Cart Summary`, `Payment Options`, `Shipping templates`, `Recipient`, checkout bottom/button patterns.
  - SPZ/store choice: `Org / Выбор СПЗ / Табы`, `Delivery Option`, `Address List`, `SPZ Info`, `Adress card`, map pointers/controls, filters.
  - Bottom sheets: `Bottom sheet / info variants`, `Bottom sheet / Sort`, `Bottom sheet / Date time`.
- Analyst rule: before creating a new requirement for a screen block, check whether a corresponding template/organism already exists. Requirements should reference reuse rather than inventing a duplicate pattern.

## Android UI Elements Showcase

- File has `43` pages, aligned with UI-kit component pages.
- Purpose: state validation and visual examples, not source components.
- Pages include `Changelog`, `Alert & Action`, `Button`, `Input Text`, `Bottom Sheet`, `NavBar`, `Search`, `Loader`, `Product card`, `Product photo`, `QTY`, `Tabs`, etc.
- Analyst rule: when requirement involves a component state, validate against showcase and include the needed states in acceptance criteria.

## Android v2.0 Current App

- File has `43` pages.
- Many top-level app pages are empty or structural placeholders.
- Populated/meaningful areas found:
  - `Профиль`: sections for user data hiding, profile blocks `Покупки`, `Прогр.лояльности`, `Адрес`, feedback block, confirm email, favorite addresses.
  - `Центр уведомлений`: Light and Dark sections.
  - `Настройки`: personal data editing, settings, password change.
  - `Любимые категории`: Light and Dark.
  - `Выбор СПЗ`: delivery, pickup, pickup point, intermediate SPZ selection, city change.
  - `Дополнение профиля`: Light and Dark.
  - `Подтверждение почты`: Light and Dark.
  - `Промокоды`: Light sections.
  - `Правовая информация`: Light and Dark.
  - `Чекаут`: Light and Dark sections with nested blocks `Самовывоз`, `Пункт выдачи`, `Доставка`, `Частные кейсы`, `Быстрый заказ`.
- Empty or nearly empty target areas include:
  - `Ошибки`, `Главная`, `Поиск`, `Первый запуск / Локализация`, `Onboarding`, `Анимации`, `Stories`, `Обновление приложения`, `Карта Fix Price`, `Попапы`, `Отзывы покупателей`, `Регистрация, Вход`, `Восстановление пароля`, `Ошибки подтверждения`, `Оценка приложения`, `Избранные адреса`, `Подтверждение аккаунта`, `Мои покупки`, `Помощь`, `Избранные товары`, `Подписки`, `Удаление аккаунта`, `Каталог`, `Карта товара`, `Корзина`, `TYP`, `Магазины`, `Акции`.
- Analyst rule: when creating BFT/requirements, identify whether the target section is already populated, partially populated, or empty. This changes whether the task is a refinement, extension, or new screen design request.

## Analytical Checklist For Any Feature

Capture these points before writing requirements:

1. Target page in `Android v2.0`.
2. Related template in `Android templates`.
3. Base UI-kit components.
4. Required component states: default, loading, empty, error, disabled, success, selected, pressed/focus where applicable.
5. Light/Dark mode impact.
6. Data entities and attributes shown on screen.
7. Validation rules and error texts.
8. Entry points and exit points.
9. Navigation/back behavior.
10. Analytics events, if measurable behavior exists.
11. Permissions/authorization differences.
12. Network/offline/slow response behavior.
13. Duplicated action prevention and idempotency.
14. Reuse requirement: no detached/local component unless justified.

## Requirement Wording Pattern

Use this pattern when converting mockups into implementation specs:

- `SA-FR-###`: The system shall ...
- `Source`: Figma file/page/section/component.
- `Actor`: user/system/admin/external service.
- `Preconditions`: required state and data.
- `Trigger`: user action or system event.
- `Behavior`: exact system response.
- `Data`: fields read/written.
- `States`: loading/empty/error/success/disabled.
- `Acceptance criteria`: Given/When/Then or checklist.
- `Design references`: template, UI-kit component, tokens.
- `Open questions`: owner and decision needed.
