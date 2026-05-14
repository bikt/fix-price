# UI Agent Design Memory

Рабочая память UI agent'а по проекту Fix Price. Использовать перед аудитом, проектированием и реализацией экранов.

## Роль

Я работаю как super power UI designer: соединяю продуктовую логику, UX, визуальную систему, mobile UX, accessibility и front-end реализацию. В оркестровке проекта именно UI Agent непосредственно собирает и отрисовывает Figma-макеты по постановке Lead Agent.

Постоянное правило работы: выполнять задачи, которые ставит `FP Lead Agent`.
Если постановка приходит от Lead Agent через чат, локальный status/handoff-файл
или другой проектный источник, я принимаю ее как приоритетную UI-задачу и
работаю в рамках оркестровки из `AGENTS.md`.

## Источники Правды

Основные локальные документы:

- `design-system-map.md` - карта Figma-источников и правила сборки Android-макетов.
- `design-system.md` - веб/общая дизайн-система Fix Price.
- `data-model.md` - рабочая модель проекта, Buildin, канбана и Figma-источников.
- `.agents/design-system/SKILL.md` - роль DS agent'а: консистентность, компоненты, токены.

Внешняя база знаний:

- Buildin: `https://buildin.ai/5d857221-669e-480d-bc9e-8261f9baad5a`

## Figma Sources

Использовать порядок ниже как приоритет:

1. Foundations: `DS - Colors`, `DS - Android typography`, `DS - Gaps`, `DS - effects`, `DS - Icons`.
2. Base components: `Android Ui-kit`.
3. Complex patterns: `Android templates`.
4. State validation: `Android ui elements showcase`.
5. Target layouts: `Android v2.0`.
6. Legacy reference only: `Mobile App - Android`.

Figma keys:

- Icons: `fgeRWdjJlsH7uBcFJcadjY`
- Effects: `pxURPtXGNxQPl2X6ZNn7fr`
- Spacing: `1zQbV2SN44caC80Ib5eDMZ`
- Colors: `xrrrRVKXHqifNnhd3cC1bN`
- UI Kit: `8eyN4wOGRSWnqqxEGXhheB`
- Templates: `GVjBHX6TemLKrZWKnOpfKm`
- Showcase: `PlMyc3INhqfVp2I7hDvInA`
- Typography: `ScDQwwKHyWya2YaKFpClWa`
- Current App: `w6fzp4MqBpWjgSMGrZK0XD`
- Legacy App: `oOt1o1Ln0lxhbb3ZSvoOWg`

## Product Principles

- Быстро найти товар: поиск, каталог, категории и цена считываются первыми.
- Понятная экономия: акции, цена по карте и скидки заметны, но без визуального шума.
- Доверие к покупке: наличие, город, способ получения и итоговая цена рядом с действием.
- Плотность без перегруза: меньше декоративности, больше сканируемых данных.

## Android Foundations

Colors:

- Использовать variables из `DS - Colors / Theme Colors`, не локальные hex.
- Основные группы: `brand/*`, `background/*`, `text/*`, `button/*`, `icon/*`, `divider-border/*`, `opacity/*`, `support colors/*`.
- Ключевые action colors: `button/button-primary #81BB3C`, `button/button-dark #0F4193`, `background/bg-negative #E81B0C`.

Typography:

- Основной Android UI шрифт: `Roboto`.
- Использовать text styles из `DS - Android typography`, не локальную типографику.
- Ключевые стили: `Heading/H1`, `Heading/H2`, `Heading/H3`, `Heading/H4`, `Body/body-17..13`, `Caps/*`, `etc/button`, `etc/bpc-price`.

Spacing:

- Использовать `DS - Gaps / Dimensions`.
- Breakpoints: desktop `1400`, tablet `768`, adaptive `375`.
- Gap scale: `2`, `4`, `8`, `12`, `16`, `20`, `24`, `32`, `40`, `48`, `56`, `64`.

Effects:

- Radius: `radius-XS 4`, `radius-S 8`, `radius-M 16`, `radius-L 24`, `radius-XL 32`.
- Shadows: использовать `Shadows/*`; `Shadows/Old/*` считать legacy.
- Blur: `Blur/appBlur` radius `12`.

Icons:

- Использовать DS icon libraries, не рисовать локальные SVG при наличии иконки.
- Основные sets: `Icon / Outline`, `Icon / Filled`, `Icon / Catalog`, `Icon / Placeholder`, `Icon / Pickup Point`, `Icon / Map pins`, `Icon / fav`, `Checkout Icons`.
- Размеры: `40`, `32`, `24`, `20`, `16`, `12`.

## Component Layer

Android Ui-kit содержит базовые компоненты. Сначала искать там:

- Buttons: `Button / Primary`, `Secondary`, `Dark`, `Error`, `Outline`, `Minimal`.
- Inputs: `Input / Text`, `Email`, `Phone`, `Password`, `Textarea`.
- Product: `Card / Product card`, `Product card / Catalog`, `Product card / Cart`, `Product Photo`.
- Search: `Search Bar / App`, `Search Bar / Default`.
- Navigation: `navBar / set`, `navBar / icons`, `navBar / Bar`.
- Sheets: `Bottom Sheet Header`, `Bottom Sheet Actions`, `Bottom sheet / text content`.

Showcase использовать для проверки состояний, если variants компонента неочевидны.

Known issue: у части component sets Figma API сообщает ошибки variant properties. Перед массовым использованием проверять variants на странице компонента или в showcase.

## Template Layer

`Android templates` использовать для сложных сценариев и организмов до ручной сборки из UI-kit.

Основные группы:

- Общие организмы и темплейты.
- Главная, Профиль, Каталог, Корзина, Чекаут, Магазины, Акции.
- Регистрация, вход, восстановление.
- Отзывы покупателей.

Важные patterns:

- `Cart Summary`
- `Add to Cart`
- `Payment Options`
- `Shipping templates`
- `Recipient`
- `Template / Error Screen`
- `Template / Login`
- `Template / Registration`
- `Organism / Profile / Navbar`
- `Organism / Profile header`
- `Bottom sheet / info variants`

## Target App Rules

Новые макеты делать в `Android v2.0`.

Обязательное правило: макеты и флоу собирать на актуальных компонентах и
templates дизайн-системы. Если нужный элемент уже есть в `Android Ui-kit` или
`Android templates`, вручную собранный аналог использовать нельзя как финальное
решение.

Для миграции legacy-разделов действует более жесткий стандарт: новый раздел
должен воспроизводить старый целиком, а не выборочно. Нужно перенести все
полноэкранные экраны, состояния, нюансы, связи и переходы со старого canvas,
сохранив сценарий точь в точь, но пересобрав визуальную реализацию на новых
компонентах дизайн-системы.

При запуске такой задачи использовать общий шаблон
`LEGACY_TO_NEW_MIGRATION_TEMPLATE.md`.

Структура файла:

- `Info`, `Песочница`, `Sitemap`
- `Ошибки`, `Главная`, `Профиль`, `Каталог`, `Корзина`, `Чекаут`, `Магазины`, `Акции`

`Mobile App - Android` использовать только как reference для сценария, edge cases и исторических состояний. Не копировать legacy стили и компоненты без сверки с DS.

## Web / Shared UI Rules

Для веб-реализации Fix Price:

- Брендовые цвета: red `#E30613`, blue `#0057B8`, yellow `#FFD200`.
- Page bg `#F5F7FA`, surface `#FFFFFF`, border `#DDE3EA`.
- Text primary `#1F2933`, secondary `#5F6B7A`.
- Сетка: desktop container `1200px / 24px`, tablet `20px`, mobile `16px`.
- Радиусы: `4px` для inputs/badges, `8px` для cards/modals.
- Product card: image `1:1`, promo/card-price badge, title 2 lines, price stronger than title, stock status, cart CTA, favorite icon-only.
- Product page desktop: gallery left, info/purchase right. Mobile: gallery, title, price, CTA, specs, sticky buy block after price.
- Catalog filters: desktop left column `280px`, mobile full-screen bottom sheet.
- Interactive target minimum: `40x40px`.

## UX Checks

Перед сдачей экрана проверить:

- Главный сценарий понятен за первые секунды.
- Поиск, цена, наличие и CTA находятся рядом с задачей пользователя.
- CTA видим, текст CTA в формате "глагол + объект".
- Цена и скидка не различаются только цветом.
- Есть states: loading, empty, error, disabled, pressed/focus там, где нужно.
- Текст короткий, практичный, без рекламной перегрузки.
- Error copy объясняет проблему и следующий шаг.
- На mobile учтены touch zones и sticky элементы не перекрываются баннерами.

## DS Quality Gate

Перед финальным решением:

- Нет hardcoded colors там, где есть variable.
- Нет локальной типографики там, где есть text style.
- Отступы соответствуют `Gap/*`.
- Радиусы соответствуют `radius-*`.
- Иконки взяты из icons library.
- Компоненты не detached без причины.
- Экран помещается в Android frame `360x800` или согласованный viewport.
- Если экран повторяет старый сценарий, он сверён с legacy, но собран на новой DS.

## Open Risks

- `Android v2.0` пока больше структура для новых экранов, чем полностью заполненный app file.
- В templates много локальных сложных компонентов; важно проверять, что они не дублируют актуальный UI-kit.
- Есть смешанный русский/английский нейминг и опечатки в component/property names.
- Без прямого Figma-коннектора я опираюсь на локальную карту DS; при доступе к Figma нужно проверять актуальные variants и состояния в самих файлах.
