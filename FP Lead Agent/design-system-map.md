# Android Design System Map

Рабочая карта связей между Figma-файлами. Использовать как источник правды при создании новых Android-макетов.

## Project Folder

`C:\Users\mrbik\Desktop\AI projects\projects\fix-price`

## Knowledge Base

| Роль | Источник | Назначение |
| --- | --- | --- |
| Buildin page | https://buildin.ai/5d857221-669e-480d-bc9e-8261f9baad5a | Внешняя база знаний проекта. Использовать как первичный контекст вместе с этой картой дизайн-системы. |
| Data model | `data-model.md` | Визуализированная модель рабочих данных проекта: Buildin, канбан, задачи, Figma-источники и правила сборки макетов. |
| Clickable data graph | `data-model-graph.html` | Интерактивный кликабельный граф сущностей и связей проекта. |

## Source Files

| Роль | Файл | Figma key | Назначение |
| --- | --- | --- | --- |
| Icons | DS - Icons | `fgeRWdjJlsH7uBcFJcadjY` | Иконки и сервисные пиктограммы |
| Effects | DS - effects | `pxURPtXGNxQPl2X6ZNn7fr` | Скругления, тени, blur |
| Spacing | DS - Gaps | `1zQbV2SN44caC80Ib5eDMZ` | Отступы, gaps, breakpoints |
| Colors | DS - Colors | `xrrrRVKXHqifNnhd3cC1bN` | Light/Dark цветовые variables и gradients |
| UI Kit | Android Ui-kit | `8eyN4wOGRSWnqqxEGXhheB` | Базовые Android-компоненты |
| Templates | Android templates | `GVjBHX6TemLKrZWKnOpfKm` | Сложные компоненты, организмы, экранные шаблоны |
| Showcase | Android ui elements showcase | `PlMyc3INhqfVp2I7hDvInA` | Демонстрация состояний компонентов |
| Typography | DS - Android typography | `ScDQwwKHyWya2YaKFpClWa` | Android text styles |
| Current App | Android v2.0 | `w6fzp4MqBpWjgSMGrZK0XD` | Новый рабочий файл макетов |
| Legacy App | Mobile App - Android | `oOt1o1Ln0lxhbb3ZSvoOWg` | Старый файл макетов, использовать как reference |

## Usage Priority

1. **Foundations first:** Colors, Typography, Gaps, Effects, Icons.
2. **Base components:** Android Ui-kit.
3. **Complex product patterns:** Android templates.
4. **State validation:** Android ui elements showcase.
5. **New layouts:** Android v2.0.
6. **Legacy reference only:** Mobile App - Android.

Новые макеты делать в `Android v2.0`. Старый файл использовать для понимания сценария, но не копировать из него локальные стили и устаревшие компоненты без сверки с DS-файлами.

## Foundations

### Colors

Файл: `DS - Colors`.

- Variables collection: `Theme Colors`.
- Modes: `Light`, `Dark`.
- Всего переменных: `140`.
- Paint styles: `13`, в основном gradients и preloader.

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

Базовые brand/action цвета:

- `brand/color-01`: Light/Dark `#91C30F`
- `brand/color-02`: Light/Dark `#0F4193`
- `background/bg-accent`: Light/Dark `#81BB3C`
- `background/bg-info`: Light `#3C7BE0`, Dark `#528AE3`
- `background/bg-negative`: Light `#E81B0C`, Dark `#F3291A`
- `button/button-primary`: Light/Dark `#81BB3C`
- `button/button-dark`: Light `#0F4193`, Dark `#114CAA`

Правило: цвета в новых макетах задавать через variables из `Theme Colors`, а не локальными hex.

### Typography

Файл: `DS - Android typography`.

- Text styles: `46`.
- Основной шрифт Android UI: `Roboto`.
- Служебная типографика для обложек/разметки: `Inter`.

Ключевые стили:

- `Heading/H1`: Roboto ExtraBold, 24/27
- `Heading/H2`: Roboto SemiBold, 21/22
- `Heading/H3`: Roboto Medium, 19/23
- `Heading/H4`: Roboto Medium, 16/20
- `Body/body-17`, `Body/body-16`, `Body/body-15`, `Body/body-14`, `Body/body-13`
- Варианты body: regular, `-sb`, `-b`, `-st`, `-und`
- `Caps/caps-12`, `Caps/caps-12-sb`, `Caps/caps-10-sb`, `Caps/caps-nav`, `Caps/caps-badge`, `Caps/caps-overline`
- `Caps/price-sub`, `Caps/price-sub-st`
- `etc/button`: Roboto Medium, 16/18
- `etc/bpc-price`: Roboto Black, 24/22

Правило: для пользовательского текста использовать Android typography styles. `Frame naming/*` только для организации страниц и обложек.

### Spacing

Файл: `DS - Gaps`.

Variables collection: `Dimensions`.

Breakpoints:

- `Breakpoint/desktop`: `1400`
- `Breakpoint/tablet`: `768`
- `Breakpoint/adaptive`: `375`

Spacing scale:

- `Gap/2`: `2`
- `Gap/4`: `4`
- `Gap/8`: `8`
- `Gap/12`: `12`
- `Gap/16`: `16`
- `Gap/20`: `20`
- `Gap/24`: `24`
- `Gap/32`: `32`
- `Gap/40`: `40`
- `Gap/48`: `48`
- `Gap/56`: `56`
- `Gap/64`: `64`

Правило: использовать шаги из `Gap/*` для padding, item spacing, spacer frames.

### Effects

Файл: `DS - effects`.

Radius variables:

- `radius-XS`: `4`
- `radius-S`: `8`
- `radius-M`: `16`
- `radius-L`: `24`
- `radius-XL`: `32`

Shadow styles:

- `Shadows/Shadow-down/shadow-down-S`: `0 4 12 rgba(0,0,0,.08)`
- `Shadows/Shadow-down/shadow-down-M`: `0 8 24 rgba(0,0,0,.16)`
- `Shadows/Shadow-down/shadow-down-L`: `0 12 32 rgba(0,0,0,.16)`
- `Shadows/Shadow-up/shadow-up-S`: `0 -4 12 rgba(0,0,0,.08)`
- `Shadows/Shadow-up/shadow-up-M`: `0 -8 24 rgba(0,0,0,.16)`
- `Shadows/Shadow-up/shadow-up-L`: `0 -12 32 rgba(0,0,0,.16)`
- `Shadows/Shadow custom/header-shadow`: `0 2 24 -8 rgba(112,138,176,.20)`

Blur:

- `Blur/appBlur`: background blur radius `12`.

Правило: новые тени брать из `Shadows/*`; `Shadows/Old/*` считать legacy.

### Icons

Файл: `DS - Icons`.

- Component sets: `10`.
- Components: `182`.

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

Размеры есть как компоненты:

- `Size=40`
- `Size=32`
- `Size=24`
- `Size=20`
- `Size=16`
- `Size=12`

Правило: для действий и навигации использовать `Icon / Outline` или специализированный set. Не рисовать локальные SVG/векторы, если иконка уже есть.

## Component Layer

### Android Ui-kit

Файл: `Android Ui-kit`.

- Component sets: `97`.
- Components: `661`.
- Локальные styles почти отсутствуют, поэтому visual language должен приходить из foundation-библиотек.

Ключевые страницы:

- `🏠 Accordion 🟢`
- `🏠 Alert & Action 🟢`
- `🏠 AppBar 🟢`
- `🏠 Badge 🟢`
- `🏠 Bottom Sheet 🟡`
- `🏠 Button 🟢`
- `🏠 Cell 🟢`
- `🏠 Input Text 🟢`
- `🏠 Product card`
- `🏠 Product photo`
- `🏠 Search 🟡`
- `🏠 Tabs`
- `🏠 NavBar`
- `🏠 QTY`
- `🏠 Snackbar`
- `🏠 Switcher`

Важные component sets:

- `Button / Primary`, `Button / Secondary`, `Button / Dark`, `Button / Error`, `Button / Outline`, `Button / Minimal`
- `Input / Text`, `Input / Email`, `Input / Phone`, `Input / Password`, `Input / Textarea`
- `Card / Product card`
- `Product card / Catalog`, `Product card / Cart`
- `Product Photo`, `Product photo / Catalog`, `Product photo / Cart`, `Product photo / Slider`
- `Search Bar / App`, `Search Bar / Default`
- `navBar / set`, `navBar / icons`, `navBar / Bar`
- `Bottom Sheet Header`, `Bottom Sheet Actions`, `Bottom sheet / text content`

Known issue: Figma API сообщает ошибки у части component sets при чтении variant properties. Перед активным использованием компонента проверять variants на странице компонента или в showcase.

### Showcase

Файл: `Android ui elements showcase`.

Назначение: проверять все состояния компонентов. Сам файл не хранит components/styles, он выступает как витрина и changelog.

Страницы повторяют UI-kit:

- `🏠 Button 🟡`
- `🏠 Input Text 🟡`
- `🏠 NavBar 🟡`
- `🏠 Bottom Sheet 🟡`
- `🏠 Search 🟡`
- и другие базовые элементы.

Правило: если непонятно, какое состояние выбрать, смотреть showcase, затем брать сам component из UI-kit.

## Template Layer

Файл: `Android templates`.

- Component sets: `235`.
- Components: `1219`.
- Styles локально не заведены, значит templates должны наследовать foundations через instances.

Основные группы страниц:

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

Примеры template/organism sets:

- `Cart Summary`
- `Add to Cart`
- `Payment Options`
- `Shipping templates`
- `Recipient`
- `Template / Error Screen`
- `Template / Login`
- `Template / Registration`
- `Template / Card Registration`
- `Organism / Profile / Navbar`
- `Organism / Profile header`
- `Organism / Profile / block rows set`
- `Template / App rate`
- `Template / Order Feedback / Rate 5`
- `Bottom sheet / info variants`

Правило: для экранов приложения сначала искать готовый template/organism здесь, потом собирать недостающее из UI-kit.

## App Layout Files

### Android v2.0

Новый рабочий файл макетов.

Структура:

- `ℹ️ Info`
- `ℹ️ Песочница`
- `ℹ️ Sitemap`
- `📁 Ошибки`
- `📁 Главная`
- `📁 Профиль`
- `📁 Каталог`
- `📁 Корзина`
- `📁 Чекаут`
- `📁 Магазины`
- `📁 Акции`

Особенность: многие страницы пока пустые или почти пустые. Это целевой файл для новых экранов.

### Mobile App - Android

Старый файл макетов.

Использовать как reference для:

- пользовательских сценариев;
- старых экранных состояний;
- edge cases;
- исторических решений.

Не использовать как источник токенов и компонентов, если аналог есть в DS/UI-kit/templates.

## Build Rules For New Mockups

1. Создавать макеты в `Android v2.0`.
2. Брать цвета из `DS - Colors / Theme Colors`.
3. Брать типографику из `DS - Android typography`.
4. Брать отступы из `DS - Gaps / Dimensions`.
5. Брать радиусы и тени из `DS - effects`.
6. Брать иконки из `DS - Icons`.
7. Базовые элементы брать из `Android Ui-kit`.
8. Сложные блоки и готовые сценарные куски брать из `Android templates`.
9. Проверять состояния в `Android ui elements showcase`.
10. Старый `Mobile App - Android` использовать только как reference, не как library.

## Quality Checks

Перед сдачей нового макета проверить:

- Нет локальных hardcoded colors там, где есть переменная.
- Нет локальной типографики там, где есть text style.
- Отступы соответствуют `Gap/*`.
- Радиусы соответствуют `radius-*`.
- Иконки взяты из icons library.
- Компоненты не detached без причины.
- Состояния есть для loading, empty, error, disabled, pressed/focus там, где это нужно.
- Экран помещается в Android frame `360x800` или согласованный актуальный viewport.
- Если экран повторяет старый сценарий, он сверён с legacy-файлом, но собран на новой DS.

## Open Risks

- В `Android Ui-kit` есть component sets с ошибками variant properties. Нужно чинить в Figma перед массовым переиспользованием или обходить конкретные проблемные sets.
- Встречается смешанный нейминг на русском/английском и опечатки в component/property names.
- `Android v2.0` пока больше похож на структуру для новых экранов, чем на полностью заполненный app file.
- В templates много локальных сложных компонентов; при создании новых экранов важно проверять, что они не дублируют актуальные UI-kit components.

