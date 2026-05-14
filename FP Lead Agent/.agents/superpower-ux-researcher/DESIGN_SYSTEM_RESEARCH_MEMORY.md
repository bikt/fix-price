# Design System Research Memory

Контекст для роли `superpower-ux-researcher`. Использовать как рабочую память при UX-исследованиях, CustDev, usability-аудитах, UX-дайджестах и аргументации продуктовых решений для Android-приложения Fix Price.

## Источники

- Локальная карта: `design-system-map.md`.
- Локальное описание: `design-system.md`.
- Полное исследование приложения и дизайн-системы: `SUPERPOWER_UX_RESEARCHER_FULL_APP_DS_STUDY_2026-05-14.md`.
- Design System agent: `.agents/design-system/SKILL.md`.
- Figma `Android v2.0`: `w6fzp4MqBpWjgSMGrZK0XD`.
- Figma `Android Ui-kit`: `8eyN4wOGRSWnqqxEGXhheB`.
- Figma `Android templates`: `GVjBHX6TemLKrZWKnOpfKm`.
- Foundation-файлы: colors, typography, gaps, effects, icons.
- Legacy reference: `Mobile App - Android`, использовать только для понимания старых сценариев и edge cases.

## Продуктовая рамка

Fix Price Android — e-commerce / retail-приложение с частыми покупками, каталогом, поиском, корзиной, чекаутом, профилем, программой лояльности, СПЗ, магазинами, акциями и отзывами.

Для исследований и UX-аудитов главный фокус:

- быстро найти товар;
- понять цену, скидку, цену по карте и выгоду;
- доверять наличию, городу, магазину, способу получения и итоговой цене;
- без трения пройти корзину и чекаут;
- управлять профилем, адресами, уведомлениями, промокодами и лояльностью;
- не потеряться в мобильных bottom sheets, модалках, формах и ошибках.

## Приоритет источников дизайна

1. Foundations: colors, typography, gaps, effects, icons.
2. Base components: `Android Ui-kit`.
3. Complex patterns: `Android templates`.
4. State validation: `Android ui elements showcase`.
5. New layouts: `Android v2.0`.
6. Legacy app: только reference, не источник токенов и компонентов.

## Важные Figma-наблюдения

### Android v2.0

Живые макеты сейчас сильнее всего покрывают:

- профиль;
- центр уведомлений;
- настройки и редактирование данных;
- любимые категории;
- выбор СПЗ: доставка, самовывоз, пункт выдачи, смена города;
- дополнение профиля;
- подтверждение почты;
- промокоды;
- правовую информацию;
- чекаут в Light/Dark.

Многие разделы в `Android v2.0` пока пустые или выступают как структура под будущие сценарии: главная, поиск, первый запуск, onboarding, stories, отзывы, регистрация, каталог, карточка товара, корзина, магазины, акции. Для этих областей нужно идти в `Android templates` и legacy reference.

### Android Ui-kit

Ключевые компоненты для UX-аудитов и исследований:

- Accordion.
- Alert / ActionSheet.
- AppBar.
- Badge.
- Bottom Sheet.
- Button: primary, secondary, dark, error, outline, minimal, QTY, floating, social.
- Cell.
- Checkbox.
- Date picker.
- Divider.
- Dropdown.
- Informer.
- Input Text / Email / Phone / Password / Textarea.
- Product card / product photo.
- Search.
- Tabs.
- NavBar.
- Snackbar.
- Switcher.

У многих компонентов есть состояния `normal`, `pressed`, `loading`, `disabled`, `focus`, `filled`, `error`. При исследовательских рекомендациях обязательно проверять, покрыты ли эти состояния в сценарии.

### Android templates

Важные шаблоны и организмы:

- СПЗ варианты.
- Keyboard.
- Registration card number.
- Promo code.
- Continue / legal consent block.
- Snackbar appearance.
- Error screen content.
- App rate.
- Template / Error Screen.
- Bottom sheet info variants.
- Bottom sheet sort.
- Bottom sheet date time.
- Profile navbar.
- Notification.
- Title block.
- Overlay banner.
- Account confirmation.
- Profile completion: region, city.
- Verify code buttons, get new code.
- Main screen components: order notification, open card, barcode, СПЗ block, header, technical banner, categories, loyalty block, product sliders, tiles.
- First launch / localization: country, city, first screen, error states.
- Stories: share, favorite, mute, footer, QA, comment.
- Order feedback: default screen, thank you, order number, emoji rating, questions, textarea, rate 3/5 states.
- Login / registration / recovery templates.
- Cart summary, filters, breadcrumbs, stock, product order history.

Для UX research это значит: многие каналы пользовательского мнения уже можно встроить в существующие паттерны App rate, Order feedback, Stories QA/comment, Bottom sheets, Snackbar/Informer, Error screens, Profile/Help.

## Foundation-память

### Android DS tokens

- Colors live in `Theme Colors`, Light/Dark modes, about 140 variables.
- Main brand/action tokens from map:
  - `brand/color-01`: `#91C30F`.
  - `brand/color-02`: `#0F4193`.
  - `background/bg-accent`: `#81BB3C`.
  - `background/bg-info`: Light `#3C7BE0`, Dark `#528AE3`.
  - `background/bg-negative`: Light `#E81B0C`, Dark `#F3291A`.
  - `button/button-primary`: `#81BB3C`.
  - `button/button-dark`: Light `#0F4193`, Dark `#114CAA`.
- Typography: Roboto for Android UI; key styles `Heading/H1-H4`, `Body/body-17..13`, caps, button, price.
- Spacing scale: `Gap/2`, `4`, `8`, `12`, `16`, `20`, `24`, `32`, `40`, `48`, `56`, `64`.
- Radius: XS 4, S 8, M 16, L 24, XL 32.
- Icons: use DS icons, not local vectors; sizes 40, 32, 24, 20, 16, 12.

### Web/product notes from `design-system.md`

The file appears to describe a broader/web Fix Price design system and may not match Android tokens one-to-one. Treat it as product language and UX principles, not as the Android source of truth.

Useful principles:

- Search, catalog, categories and price should be understood first.
- Promotions and card price should be visible without visual noise.
- Availability, city, delivery/pickup method and total price should stay close to action.
- Dense retail UI is acceptable, but it must stay scannable.
- Product cards need image, promo/card-price badge, name, price, old price/card price, availability, cart action, favorite action.
- If out of stock, replace cart CTA with notification action.
- Product page mobile should prioritize gallery, title, price, CTA, characteristics, with sticky purchase area when relevant.
- Filters on mobile should be bottom-sheet based.
- Empty/error/loading states need clear next action.
- CTA copy should be verb + object.

## Research Implications

### High-value scenarios to investigate first

1. Search and catalog discovery.
2. Product card comprehension: price, card price, promo, availability.
3. Product details and decision confidence.
4. Cart summary and quantity changes.
5. Checkout: recipient, delivery/pickup, payment, final price.
6. СПЗ selection: delivery, self pickup, pickup point, city change.
7. Login, registration, account confirmation, password recovery.
8. Profile: personal data, addresses, favorites, loyalty, subscriptions.
9. Promocodes.
10. Order feedback and app rating.
11. Notifications center.
12. Error, empty, loading and offline states.

### Good places to collect user opinion in app/site

- After search with no result: "Что вы пытались найти?"
- After search with result but no product open/add-to-cart: "Нашли нужный товар?"
- Product card or product page: "Достаточно ли информации для выбора?"
- Out-of-stock state: "Хотите узнать о поступлении?" plus optional demand signal.
- Cart abandonment: "Что мешает оформить заказ?"
- Checkout error/drop-off: "Что сейчас непонятно?"
- СПЗ selection: "Удобно ли выбрать способ получения?"
- City/store change: "Нашли свой город/магазин?"
- Promo code error: "Промокод не подошел: что ожидали?"
- Order completion: CES/CSAT for checkout.
- After order pickup/delivery: order feedback template.
- Profile/help: "Удалось решить вопрос?"
- Error screen: one-tap reason tagging plus free text.
- Stories QA/comment: lightweight pulse checks for promotions, loyalty and content.

### Audit lens

For every screen or flow, check:

- user goal;
- business metric;
- primary action;
- source of trust: price, availability, delivery/pickup, city/store, payment;
- unnecessary steps;
- unclear copy;
- missing states: loading, empty, error, disabled, pressed/focus;
- bottom sheet clarity;
- mobile touch target and reachability;
- Light/Dark parity;
- DS compliance: tokens, typography, gaps, radius, icons, components.

### Metrics language

Translate UX findings into:

- search success rate;
- zero-result search rate;
- product detail view rate;
- add-to-cart conversion;
- cart-to-checkout conversion;
- checkout completion;
- delivery/pickup selection success;
- promocode success/error rate;
- registration/login completion;
- profile completion;
- support contacts per scenario;
- order feedback score;
- CSAT/CES after key flows.

## Risks And Watchouts

- `Android v2.0` is not fully populated; do not assume absence of a screen means absence of a pattern.
- Some UI-kit component sets may have Figma API variant-property issues; verify variants in showcase or component page before making precise implementation claims.
- There is mixed Russian/English naming and some typos in components/properties.
- Templates contain many complex local components; check if they duplicate newer UI-kit components before recommending reuse.
- `design-system.md` color/token values differ from Android DS map; Android map wins for Android макеты.
- Light/Dark pairs exist for several flows; research notes should mention theme parity when relevant.

## Default Role Behavior

When using this memory:

- ask for or infer the target scenario before recommendations;
- ground recommendations in existing DS components and templates;
- propose research methods that can be embedded into existing screens and patterns;
- avoid generic UX advice;
- state which evidence is from Figma/DS and which is a research hypothesis;
- prefer short artifacts that product teams can use immediately.
