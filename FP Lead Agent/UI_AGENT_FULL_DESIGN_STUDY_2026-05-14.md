# UI Agent Full Design Study - 2026-05-14

Рабочая карта UI Agent по дизайн-системе, Figma-источникам, legacy-приложению и `Android v2.0`.

## Главный Вывод

Проект устроен как миграция старого Android-приложения в новый Figma-файл `Android v2.0`.

Правильный процесс:

1. Понять пользовательский и продуктовый сценарий в `Mobile App - Android`.
2. Найти готовые foundations, components и templates в DS-файлах.
3. Пересобрать весь flow в `Android v2.0`.
4. Не копировать legacy-стили и не рисовать вручную аналоги DS-компонентов.
5. Если DS-компонент отсутствует или дефектный, фиксировать DS-gap, а не обходить его ручной отрисовкой.

## Источники И Роли Файлов

| Уровень | Figma file | Key | Роль |
| --- | --- | --- | --- |
| Colors | `DS - Colors` | `xrrrRVKXHqifNnhd3cC1bN` | Цветовые variables и paint styles |
| Typography | `DS - Android typography` | `ScDQwwKHyWya2YaKFpClWa` | Android text styles |
| Spacing | `DS - Gaps` | `1zQbV2SN44caC80Ib5eDMZ` | Gap и breakpoint variables |
| Effects | `DS - effects` | `pxURPtXGNxQPl2X6ZNn7fr` | Radius, shadows, blur |
| Icons | `DS - Icons` | `fgeRWdjJlsH7uBcFJcadjY` | Icon component sets |
| UI Kit | `Android Ui-kit` | `8eyN4wOGRSWnqqxEGXhheB` | Базовые компоненты |
| Showcase | `Android ui elements showcase` | `PlMyc3INhqfVp2I7hDvInA` | Витрина/проверка состояний, сейчас частично пустая |
| Templates | `Android templates` | `GVjBHX6TemLKrZWKnOpfKm` | Организмы, экранные templates, продуктовые паттерны |
| Legacy app | `Mobile App - Android` | `oOt1o1Ln0lxhbb3ZSvoOWg` | Источник сценариев и edge cases |
| Target app | `Android v2.0` | `w6fzp4MqBpWjgSMGrZK0XD` | Новый рабочий файл макетов |

## Правильный Приоритет Использования

1. `DS - Colors`, `DS - Android typography`, `DS - Gaps`, `DS - effects`, `DS - Icons`.
2. `Android Ui-kit`.
3. `Android templates`.
4. `Android ui elements showcase` или уже собранные app sections для проверки состояний.
5. `Android v2.0` как target.
6. `Mobile App - Android` только как reference сценария.

## Foundations

### Colors

Файл `DS - Colors`.

- Pages: `Project cover`, separator, `🎨 Colors`.
- Variables collection: `Theme Colors`.
- Modes: `Light`, `Dark`.
- Variables: `140`.
- Groups: `brand`, `background`, `text`, `button`, `icon`, `divider-border`, `opacity`, `app preloader`, `shades`, `support colors`.
- Paint styles: `13`, в основном gradients и preloader styles.

Ключевое правило: для новых Android-макетов использовать variables, не локальные hex.

### Typography

Файл `DS - Android typography`.

- Text styles: `46`.
- Groups: `Heading`, `Body`, `Caps`, `etc`, `Frame naming`.
- Основной UI-шрифт: `Roboto`.
- `Frame naming` использует `Inter` и нужен для служебной разметки, не для пользовательского UI.

Ключевые стили:

- `Heading/H1`, `H2`, `H3`, `H4`.
- `Body/body-17..13` с regular, sb, b, st, und.
- `Caps/caps-*`.
- `etc/button`.
- `etc/bpc-price`.

### Gaps

Файл `DS - Gaps`.

- Variables collection: `Dimensions`.
- Variables: `15`.
- Groups: `Breakpoint`, `Gap`.
- Breakpoints: `desktop 1400`, `tablet 768`, `adaptive 375`.
- Gap scale: `2`, `4`, `8`, `12`, `16`, `20`, `24`, `32`, `40`, `48`, `56`, `64`.

### Effects

Файл `DS - effects`.

- Pages: `Shadow`, `Radius`, `Blur`.
- Radius variables: `radius-XS 4`, `radius-S 8`, `radius-M 16`, `radius-L 24`, `radius-XL 32`.
- Effect styles: `8`.
- Shadow styles: `Shadow-down S/M/L`, `Shadow-up S/M/L`, `header-shadow`.
- Blur style/variable в файле называется `ageBlur`; в локальной карте было указано `appBlur`, это нужно сверить с DS Agent.

### Icons

Файл `DS - Icons`.

- Page: `Icons`.
- Component sets: `10`.
- Components: `182`.
- Основные sets: `Icon / Outline`, `Icon / Filled`, `Icon / Catalog`, `Icon / Placeholder`, `Icon / Pickup Point`, `Icon / Map pins`, `Icon / Map pins / Наличие`, `Icon / fav`, `Checkout Icons`, `Иконки СПЗ`.

Правило: не рисовать локальные иконки, если аналог есть в icon library.

## UI Kit

Файл `Android Ui-kit`.

- Pages: около `45`.
- Component sets: `98`.
- Components: `663`.
- Есть legacy/temporary page `❌ удалить после внедрения`, но активные страницы идут с `🏠`.

Ключевые страницы:

- `🏠 Alert & Action`
- `🏠 AppBar`
- `🏠 Badge`
- `🏠 Bottom Sheet`
- `🏠 Button`
- `🏠 Cell`
- `🏠 Informer`
- `🏠 Input Text`
- `🏠 Loader`
- `🏠 NavBar`
- `🏠 Product card`
- `🏠 Product photo`
- `🏠 Search`
- `🏠 Snackbar`
- `🏠 Switcher`
- `🏠 Tabs`

Важные component keys, подтвержденные при работе:

- `Alert Wrap`: `983b540a17fcc0f68d1bf98045aeca0f2a566d11`
- `Loader / Full Screen`: `83a44e6958fd3c4027d99dcd8fe030fb8c4df78f`
- `Informer / Floating`: `37092a50218906a17fe4bbff7ae723af527f8a92`
- `Bottom sheet master`: `67fb55727f44501916d39fbff73c4303d51b535d`

Правило: при сборке screens контейнер может быть новым, но интерактивные элементы и системные паттерны должны быть instances из UI-kit/templates.

## Showcase

Файл `Android ui elements showcase`.

- Pages повторяют UI-kit pages.
- Сейчас многие страницы showcase пустые.
- Поэтому для проверки состояний использовать:
  - сам UI-kit component page;
  - existing app sections в `Android v2.0`;
  - templates в `Android templates`.

Showcase не должен быть единственным источником истины, если страница пустая.

## Templates

Файл `Android templates`.

- Pages: продуктовая структура приложения.
- Component sets: `234`.
- Components: `1213`.
- Основные группы:
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

Важные template/organism families:

- `Template / Error Screen`
- `Bottom sheet / info variants`
- `Organism / Profile / Navbar`
- `Notification`
- `Template / App rate`
- `Payment Options`
- `Shipping templates`
- `Recipient`
- `Add to Cart`
- `Cart Summary`
- `Product Order History`

Для `Подписок` найден правильный DS-source:

- Page: `↪️ Подписки`
- Component set: `Subscrptions / Switchers`
- Node: `1477:2457`
- Key: `6d0a03a8ea75e0558ba80dd66dc68f85ddcfb003`
- Variants: `user=true`, `user=false`

DS debt: имя `Subscrptions` содержит typo; внутри variants есть placeholder layers. Финальный макет должен использовать instance + overrides, а DS Agent должен почистить source component.

## Legacy App: Mobile App - Android

Файл `Mobile App - Android`.

Назначение: источник сценариев, edge cases, старых состояний и связей.

Структура страниц почти совпадает с `Android v2.0`, что подтверждает migration-модель:

- `Ошибки`
- `Главная`
- `Поиск`
- `Первый запуск / Локализация`
- `Onboarding`
- `Stories`
- `Обновление приложения`
- `Карта Fix Price`
- `Попапы`
- `Отзывы покупателей`
- `Регистрация, Вход`
- `Восстановление пароля`
- `Ошибки подтверждения`
- `Оценка приложения`
- `Профиль`
- `Центр уведомлений`
- `Настройки`
- `Выбор СПЗ`
- `Избранные адреса`
- `Дополнение профиля`
- `Мои покупки`
- `Промокоды`
- `Любимые категории`
- `Помощь`
- `Избранные товары`
- `Правовая информация`
- `Подписки`
- `Удаление аккаунта`
- `Каталог`
- `Карта товара`
- `Корзина`
- `Чекаут`
- `TYP`
- `Магазины`
- `Акции`
- EPIC pages: алкоголь/18+, промокод.

Выявленные продуктовые сценарии:

- First launch: страна/город/локализация.
- Auth: регистрация, вход, MTS ID, VK ID, ошибки входа, loader states.
- Home: главный экран, stories, order notifications, technical banners.
- Search: recent/frequent queries, categories, brands, result blocks.
- Catalog/product: категории, карточка товара, характеристики, variants, related goods.
- Cart/checkout: доставка, самовывоз, ПВЗ, recipient, payment, fast order, private cases.
- TYP: thank-you page, order processing, pickup/courier/express delivery.
- Profile: личные данные, пароль, профильные блоки, статусы пользователя.
- Notification center.
- Settings.
- Service point selection: delivery, pickup, pickup point, city change.
- Favorite categories/products.
- Promo codes.
- Legal information.
- Subscriptions: push, SMS, email mailing, electronic receipts, email confirmation branch, loaders, errors, bottom sheet.
- Account deletion.
- 18+ products: age confirmation and reservation flow.

Правило: legacy может быть неполным в top-level child counts из-за Figma/API особенностей, поэтому для конкретного раздела нужно открывать page/node напрямую и инвентаризировать frames/text/reactions.

## Android v2.0

Файл `Android v2.0`.

Назначение: новый рабочий app file для пересобранных макетов.

Структура страниц повторяет legacy:

- service pages: `Project cover`, `Info`, `Песочница`, `Sitemap`;
- app domains: `Ошибки`, `Главная`, `Поиск`, `Первый запуск`, `Onboarding`, `Stories`, `Обновление`, `Карта Fix Price`, `Попапы`, `Отзывы`, `Регистрация`, `Профиль`, `Каталог`, `Корзина`, `Чекаут`, `Магазины`, `Акции`.

Заполненные/частично заполненные области:

- `Главная`: Light/Dark sections.
- `Поиск`: component sets `search / search cell`, `search / brand logo`, `search / blocks`.
- `Обновление приложения`: Light/Dark.
- `Профиль`: несколько task sections по профильным блокам.
- `Центр уведомлений`: Light/Dark.
- `Настройки`: личные данные, settings, смена пароля.
- `Любимые категории`: Light/Dark.
- `Выбор СПЗ`: delivery/pickup/PVZ/city change Light/Dark.
- `Дополнение профиля`: Light/Dark.
- `Подтверждение почты`: Light/Dark, уже содержит canonical email confirmation states.
- `Промокоды`: sections.
- `Правовая информация`: Light/Dark.
- `Подписки`: новая DS-only секция `594:696`.
- `Чекаут`: Light/Dark.

Пустые/почти пустые области:

- `Ошибки`
- `Первый запуск / Локализация`
- `Onboarding`
- `Stories`
- `Карта Fix Price`
- `Попапы`
- `Отзывы покупателей`
- `Регистрация, Вход`
- `Восстановление пароля`
- `Ошибки подтверждения`
- `Оценка приложения`
- `Подтверждение аккаунта`
- `Мои покупки`
- `Помощь`
- `Избранные товары`
- `Удаление аккаунта`
- `Каталог`
- `Карта товара`
- `Корзина`
- `TYP`
- `Магазины`
- `Акции`

## Current Subscriptions State

На странице `Android v2.0 / ↪️ Подписки`:

- Canonical section: `594:696`, `Подписки / DS-only restart / 2026-05-14`.
- Ошибочная manual/scaffold section `586:1868` удалена.
- Section использует:
  - imported DS component set `Subscrptions / Switchers`;
  - UI-kit `Alert Wrap`;
  - UI-kit `Loader / Full Screen`;
  - UI-kit `Informer / Floating`;
  - UI-kit `Bottom sheet master`;
  - cloned canonical email states из `↪️ Подтверждение почты / Light`.
- Visible placeholder count после проверки: `0`.
- Остаточный DS debt: source component set содержит hidden placeholder layers и typo.

## Migration Rules For UI Agent

Для любой следующей миграции:

1. Не начинать с рисования UI.
2. Сначала снять inventory legacy: frames, states, texts, reactions.
3. Составить `legacy state -> DS source -> target frame` map.
4. Найти DS component/template source:
   - сначала `Android templates`;
   - затем `Android Ui-kit`;
   - затем existing screen в `Android v2.0`;
   - только потом DS-gap.
5. Если компонент доступен, использовать instance/import/clone.
6. Text overrides допустимы внутри DS instance.
7. Скрытие внутреннего placeholder layer допустимо только как временная мера и должно быть записано как DS debt.
8. Не считать ручной scaffold финальным макетом.
9. Финальный target должен быть в `Android v2.0`.
10. Старый `Mobile App - Android` не является style source.

## DS Quality Gate

Перед сдачей макета проверить:

- Нет видимых `Text`, `Label`, `Text description` placeholder.
- Нет manually drawn analogs для существующих DS components.
- Есть source mapping для каждого экрана/состояния.
- Используются variables/styles из foundation libraries.
- Используются UI-kit/templates для controls, sheets, alerts, loaders, nav, inputs.
- Legacy flow покрыт полностью: screens, states, branches, links/flow annotations.
- Error/loading/empty/success/disabled/pressed states не потеряны.
- Если DS source дефектный, создан DS-gap note.

## Open Risks / DS Debt

- В `DS - effects` blur называется `ageBlur`, а в локальной карте было `appBlur`; требуется сверка.
- В `Android Ui-kit` есть страница `🔴 Ошибки в компонентах`, а также known issue с variant properties.
- `Android ui elements showcase` сейчас часто пустой, поэтому не всегда помогает с states.
- В `Android templates` и UI-kit есть pages `❌ удалить после внедрения`; их нельзя использовать как primary source без проверки.
- Есть смешанный русский/английский нейминг и typo: `Subscrptions`, `Infromer`, `Подверждение`.
- `Android v2.0` заполнен неравномерно: много target pages пока пустые.
- При переносе разделов нельзя ограничиваться одним happy path: надо переносить весь legacy flow.
