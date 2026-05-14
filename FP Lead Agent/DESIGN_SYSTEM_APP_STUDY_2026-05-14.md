# Design System & App Architecture Study

Дата: 2026-05-14

Задача: изучить дизайн-систему Fix-Price, связи артефактов, токенов, стилей,
компонентов, legacy-макетов и новых Android v2.0 макетов.

## Источники

- `design-system-map.md`
- `design-system.md`
- `LEGACY_TO_NEW_MIGRATION_TEMPLATE.md`
- Figma: `DS - Colors` (`xrrrRVKXHqifNnhd3cC1bN`)
- Figma: `DS - Android typography` (`ScDQwwKHyWya2YaKFpClWa`)
- Figma: `DS - Gaps` (`1zQbV2SN44caC80Ib5eDMZ`)
- Figma: `DS - effects` (`pxURPtXGNxQPl2X6ZNn7fr`)
- Figma: `DS - Icons` (`fgeRWdjJlsH7uBcFJcadjY`)
- Figma: `Android Ui-kit` (`8eyN4wOGRSWnqqxEGXhheB`)
- Figma: `Android templates` (`GVjBHX6TemLKrZWKnOpfKm`)
- Figma: `Android ui elements showcase` (`PlMyc3INhqfVp2I7hDvInA`)
- Figma: `Mobile App - Android` (`oOt1o1Ln0lxhbb3ZSvoOWg`)
- Figma: `Android v2.0` (`w6fzp4MqBpWjgSMGrZK0XD`)

## Общая модель

```text
Foundations
  -> DS - Colors
  -> DS - Android typography
  -> DS - Gaps
  -> DS - effects
  -> DS - Icons

Base components
  -> Android Ui-kit

Complex patterns
  -> Android templates
  -> Android ui elements showcase for state validation

App files
  -> Mobile App - Android as legacy reference
  -> Android v2.0 as target app mockup file
```

Новые экраны должны собираться в `Android v2.0`. Старый файл
`Mobile App - Android` используется для понимания сценариев, состояний,
edge cases и исторических решений, но не как источник актуальных стилей или
компонентов.

## Foundations

### Colors

Файл `DS - Colors` содержит:

- collection `Theme Colors`;
- modes `Light`, `Dark`;
- 140 color variables;
- 13 paint styles, в основном gradients и preloader.

Ключевые группы:

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

Правило: новые макеты используют variables, а не локальные hex.

### Typography

Файл `DS - Android typography` содержит 46 text styles.

Основной UI-шрифт: `Roboto`.

Ключевые группы:

- `Heading/H1-H4`
- `Body/body-17`, `body-16`, `body-15`, `body-14`, `body-13`
- body variants: regular, `-sb`, `-b`, `-st`, `-und`
- `Caps/*`
- `etc/button`
- `etc/bpc-price`

Правило: пользовательский текст должен брать Android text styles. `Frame naming/*`
служат для организации макетов, а не для продуктового UI.

### Gaps

Файл `DS - Gaps` содержит collection `Dimensions` с 15 variables:

- `Gap/2`, `Gap/4`, `Gap/8`, `Gap/12`, `Gap/16`, `Gap/20`, `Gap/24`
- `Gap/32`, `Gap/40`, `Gap/48`, `Gap/56`, `Gap/64`
- `Breakpoint/adaptive = 375`
- `Breakpoint/tablet = 768`
- `Breakpoint/desktop = 1400`

Правило: padding, item spacing и spacer frames собирать на этом scale.

### Effects

Файл `DS - effects` содержит:

- radius variables: `radius-XS`, `radius-S`, `radius-M`, `radius-L`, `radius-XL`;
- blur variable/style с фактическим неймингом `ageBlur`;
- effect styles `Shadows/Shadow-down/*`, `Shadows/Shadow-up/*`,
  `Shadows/Shadow custom/header-shadow`.

Нюанс: в локальной карте встречается `appBlur`, а в Figma фактически виден
`ageBlur`. Перед использованием blur нужно сверять актуальный token name.

### Icons

Файл `DS - Icons` содержит:

- 182 components;
- 10 component sets.

Основные sets:

- `Icon / Outline`
- `Icon / Filled`
- `Icon / Catalog`
- `Icon / Placeholder`
- `Icon / Pickup Point`
- `Icon / Map pins`
- `Icon / Map pins / Наличие`
- `Icon / fav`
- `Checkout Icons`
- `Иконки СПЗ`

Правило: не рисовать локальные векторы, если иконка уже есть в библиотеке.

## Component Layer

### Android Ui-kit

Файл `Android Ui-kit` содержит:

- 44 pages;
- 663 components;
- 98 component sets;
- локальных text styles нет;
- локальных paint styles почти нет.

Это означает, что визуальный язык UI-kit должен приходить из foundation-файлов:
colors, typography, gaps, effects, icons.

Ключевые страницы и sets:

- `🏠 Accordion 🟢`: `Accordion`, `Accordion image`
- `🏠 Alert & Action 🟡`: `Alert`, `ActionSheet`
- `🏠 AppBar 🟢`: `AppBar / Default`, `AppBar / Accent`
- `🏠 Badge 🟢`: `Badge / Navbar`, filter badges
- `🏠 Bottom Sheet 🟡`: header, handler, actions, text content
- `🏠 Button 🟢`: primary, secondary, dark, error, outline, minimal, QTY, floating, social
- `🏠 Input Text 🟢`: text, email, phone, password, textarea
- `🏠 NavBar`: nav set, icons, cart states
- `🏠 Product card`: catalog/cart/product variants
- `🏠 Product photo`: catalog, cart, slider, placeholder states
- `🏠 Search 🟡`: app/default/shops search bars
- `🏠 Tabs`: filter, small, big, horizontal
- `🏠 QTY`, `Radio Button`, `Switcher`, `Status Bar`, `Snackbar`, `Upload Photo`

Назначение: базовый строительный слой для Android v2.0. Если компонент есть
здесь, новый экран должен использовать instance из UI-kit, а не ручной аналог.

### Android ui elements showcase

Файл `Android ui elements showcase` содержит:

- 43 pages;
- 0 локальных components/component sets.

Это витрина и проверочный слой. Он повторяет структуру UI-kit и показывает,
какие элементы готовы/требуют внимания через статусы `🟢` и `🟡`.

Назначение:

- проверка states;
- демонстрация поведения;
- сверка компонента перед использованием;
- changelog/quality reference.

## Template Layer

### Android templates

Файл `Android templates` содержит:

- 36 pages;
- 1213 components;
- 234 component sets.

Это слой сложных organisms, templates и сценарных блоков. Он не заменяет UI-kit,
а собирает более крупные паттерны из базовых компонентов.

Ключевые группы:

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

Примеры важных patterns:

- `Cart Summary`
- `Add to Cart`
- `Payment Options`
- `Shipping templates`
- `Recipient`
- `Template / Error Screen`
- `Template / Login`
- `Template / Registration`
- `Template / Card Registration`
- `Template / Password Recovery`
- `Template / App rate`
- `Template / Order Feedback`
- `Organism / Profile header`
- `Organism / Profile / block rows set`
- `Org / Выбор СПЗ/*`
- `Tempalate / Catalog / Main`
- `Tempalate / Catalog / Search`
- `Subscrptions / Switchers`
- `Template / Удаление аккаунта`

Правило: для сложного блока сначала искать template/organism здесь. Только если
его нет или он устарел, собирать из UI-kit.

## Legacy App: Mobile App - Android

Роль: источник пользовательских и продуктовых сценариев.

Файл содержит 43 pages и почти не должен использоваться как актуальная
библиотека стилей.

Ключевые legacy-сценарии:

- старт, локализация, onboarding;
- stories;
- карта Fix Price;
- регистрация и вход:
  - первичный/вторичный вход через MTS ID;
  - первичный/вторичный вход через VK ID;
  - loader;
  - недоступность вариантов входа;
  - ошибки;
  - обычная форма регистрации;
- профиль и настройки;
- выбор СПЗ:
  - доставка;
  - самовывоз;
  - пункт выдачи;
  - промежуточный экран перехода;
  - смена города;
- любимые категории;
- избранные товары: MVP и POST MVP;
- каталог;
- карточка товара;
- чекаут:
  - самовывоз;
  - пункт выдачи;
  - доставка;
  - частные кейсы;
  - быстрый заказ;
- TYP:
  - ПВЗ;
  - курьер;
  - экспресс-доставка;
  - заказы в обработке;
- эпики/частные темы: алкоголь, товары 18+, промокод на заказ.

Как читать legacy:

- искать весь flow, а не отдельный экран;
- фиксировать все states: default, loading, error, empty, disabled, success;
- переносить branching и возвраты;
- не копировать устаревшие локальные стили;
- сверять каждый блок с UI-kit/templates.

## Target App: Android v2.0

Роль: целевой файл новых макетов, пересобранных на новых компонентах,
styles и variables.

Файл содержит 43 pages, локальных text/paint styles нет. Это хороший сигнал:
новый app-file должен опираться на библиотеки, а не на локальный style drift.

Структура:

- `ℹ️ Project cover`
- `ℹ️ Info`
- `ℹ️ Песочница`
- `ℹ️ Sitemap`
- `📁 Ошибки`
- `📁 Главная`
- `↪️ Поиск`
- `↪️ Первый запуск / Локализация`
- `↪️ Onboarding`
- `↪️ Stories`
- `↪️ Обновление приложения`
- `↪️ Карта Fix Price`
- `📁 Отзывы покупателей`
- `📁 Регистрация, Вход`
- `📁 Оценка приложения`
- `📁 Профиль`
- `↪️ Центр уведомлений`
- `↪️ Настройки`
- `↪️ Любимые категории`
- `↪️ Выбор СПЗ`
- `↪️ Дополнение профиля`
- `↪️ Подтверждение почты`
- `↪️ Промокоды`
- `↪️ Правовая информация`
- `↪️ Подписки`
- `📁 Каталог`
- `↪️ Карта товара`
- `📁 Корзина`
- `📁 Чекаут`
- `↪️ TYP`
- `📁 Магазины`
- `📁 Акции`

Текущее наполнение:

- `Главная`: есть `Главная / Light` и `Главная / Dark`;
- `Профиль`: несколько больших task sections, включая блоки покупок,
  программы лояльности, адресов, отзывов, подтверждения почты и избранных адресов;
- `Выбор СПЗ`: delivery/self pickup/pickup point/intermediate/city change,
  продублировано в light/dark или paired sections;
- `Подтверждение почты`: есть light/dark sections;
- `Промокоды`, `Правовая информация`, `Центр уведомлений`, `Любимые категории`,
  `Дополнение профиля`, `Обновление приложения`: уже имеют light/dark sections;
- `Подписки`: есть section `Подписки / DS-only restart / 2026-05-14`;
- `Чекаут`: есть `Чекаут / Light` и `Чекаут / Dark`, внутри:
  `Самовывоз`, `Пункт выдачи`, `Доставка`, `Частные кейсы`, `Быстрый заказ`;
- `Каталог`, `Корзина`, `Магазины`, `Акции` пока пустые или без верхних секций.

## Основные продуктовые сценарии приложения

### Discovery / старт

- первый запуск;
- локализация;
- выбор страны/города;
- onboarding;
- stories;
- обновление приложения;
- карта Fix Price.

### Shopping journey

- главная;
- поиск;
- каталог;
- категории;
- карточка товара;
- избранное;
- корзина;
- checkout;
- TYP / результат заказа.

### Fulfillment / СПЗ

- выбор способа получения;
- доставка;
- самовывоз;
- пункт выдачи;
- смена города;
- адреса;
- избранные адреса.

### Account / profile

- регистрация;
- вход;
- восстановление;
- подтверждение аккаунта/почты;
- профиль;
- настройки;
- смена пароля;
- промокоды;
- подписки;
- удаление аккаунта;
- правовая информация.

### Feedback / support / retention

- отзывы покупателей;
- оценка приложения;
- центр уведомлений;
- помощь;
- любимые категории;
- push/subscriptions;
- stories/comment/QA.

### Risk / restricted scenarios

- алкоголь и товары 18+;
- ошибки подтверждения;
- недоступность входа;
- отсутствие интернета;
- частные checkout кейсы;
- заказы в обработке.

## Правило migration legacy -> Android v2.0

Раздел считается перенесенным только если выполнены все условия:

```text
100% flow coverage
+ DS pass
+ QA pass
```

Для каждого переносимого раздела нужно:

1. Найти legacy page/section/frame.
2. Выписать все экраны, states, transitions и branching.
3. Сопоставить каждый legacy block с DS component/template.
4. Проверить UI-kit и templates перед ручной сборкой.
5. Собрать в `Android v2.0`.
6. Сохранить light/dark, если сценарий требует обе темы.
7. Связать с уже существующими соседними flows, а не дублировать их.
8. Выполнить QA coverage.

## Карта соответствий legacy -> new

| Legacy source | New target | Комментарий |
| --- | --- | --- |
| `Mobile App - Android / Чекаут` | `Android v2.0 / Чекаут` | В new уже есть light/dark и вложенные delivery/self pickup/PVZ/private/quick order sections. |
| `Mobile App - Android / Выбор СПЗ` | `Android v2.0 / Выбор СПЗ` | Структура почти зеркальная: доставка, самовывоз, пункт выдачи, промежуточный экран, смена города. |
| `Mobile App - Android / Регистрация, Вход` | `Android v2.0 / Регистрация, Вход` + related profile flows | В legacy много MTS/VK/error states; в new часть страниц пока пустая, часть flows вынесена в профиль/подтверждение. |
| `Mobile App - Android / TYP` | `Android v2.0 / TYP` | New page пока без верхних секций; нужно переносить результат заказа по сценариям ПВЗ/курьер/экспресс/обработка. |
| `Mobile App - Android / Избранные товары` | `Android v2.0 / Избранные товары` | New page пока пустая; legacy содержит MVP/POST MVP. |
| `Mobile App - Android / Каталог` | `Android v2.0 / Каталог` | New page пока пустая; templates имеют catalog patterns. |
| `Mobile App - Android / Карта товара` | `Android v2.0 / Карта товара` | New page пока пустая; UI-kit/templates имеют product card/photo/slider/price/property rows. |
| `Mobile App - Android / Подписки` | `Android v2.0 / Подписки` | New уже содержит DS-only restart section; нужно связать с `Подтверждение почты`, не дублировать email-flow. |

## Quality Gates

### DS pass

- Цвета через `Theme Colors`.
- Типографика через `DS - Android typography`.
- Spacing через `DS - Gaps`.
- Radius/shadows/blur через `DS - effects`.
- Иконки из `DS - Icons`.
- Базовые UI через `Android Ui-kit`.
- Сложные блоки через `Android templates`.
- States сверены с showcase.

### Flow pass

- Все legacy states перенесены или осознанно вынесены в связанный раздел.
- Все переходы и возвраты сохранены.
- Все empty/loading/error/success/private cases сохранены.
- Нет orphan frames.
- Нет несвязанных screen states.

### App pass

- Новый раздел живет в правильной странице `Android v2.0`.
- Не дублирует уже существующий соседний flow.
- Light/dark покрыты там, где это принято в новых макетах.
- Нет локального style drift.
- Если компонент отсутствует, gap зафиксирован для Design System Agent.

## Открытые риски

- В `Android Ui-kit` есть страницы/sets со статусом `🟡`; перед reuse нужна проверка variants/states.
- В `DS - effects` есть расхождение нейминга blur token: `ageBlur` vs ожидаемый `appBlur`.
- `Android v2.0` заполнен неравномерно: часть разделов уже пересобрана, часть почти пустая.
- Legacy flows частично разбросаны между страницами и эпиками; нельзя переносить по одному экрану без карты сценария.
- Templates содержат много сложных organisms; перед reuse нужно проверять, не устарели ли они и не дублируют ли UI-kit.
- Встречается смешанный нейминг RU/EN и опечатки (`Tempalate`, `Infromer`, `Подверждение`).

## Короткая рабочая формула

```text
Legacy tells WHAT and WHEN.
Design system tells HOW.
Templates tell WHICH larger patterns already exist.
Showcase tells WHETHER states are valid.
Android v2.0 is WHERE the final app mockups live.
```
