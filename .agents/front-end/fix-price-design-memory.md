# Fix Price Frontend Design Memory

Use this as the Front-End agent's compact handoff from Design System Agent.

## Product Principles

- Prioritize finding products fast: search, catalog, categories, and price must read first.
- Make savings clear without noise: promos, card price, and discounts should be visible but controlled.
- Keep trust signals close to actions: availability, city, delivery/pickup mode, and final price should sit near CTA.
- Prefer dense, scannable commerce UI over decorative composition.

## Web Design Tokens

- Brand red: `#E30613` for primary CTA and discounts.
- Brand blue: `#0057B8` for navigation, secondary accents, and Fix Price card-related actions.
- Brand yellow: `#FFD200` for promos and price highlights.
- Text primary: `#1F2933`; secondary: `#5F6B7A`; inverse: `#FFFFFF`.
- Page background: `#F5F7FA`; surface: `#FFFFFF`; border: `#DDE3EA`.
- Success: `#15803D`; warning: `#B45309`; error: `#D92D20`.
- Font stack: `Inter`, `Arial`, `Helvetica`, `sans-serif`.
- Type scale: `display 32/40 700`, `h1 28/36 700`, `h2 22/30 700`, `h3 18/26 600`, `body 16/24`, `body-sm 14/20`, `caption 12/16`, `price 28/34 800`.
- Spacing step is `4px`; use `4, 8, 12, 16, 20, 24, 32, 40, 48`.
- Container: desktop `1200px` with `24px` gutters; tablet `20px`; mobile `16px`.
- Radius: `4px` for inputs/badges, `8px` for cards/modals.
- Card shadow: `0 2px 8px rgba(31, 41, 51, 0.08)`.

## Responsive Rules

- Mobile `< 768px`: 2 product columns, compact two-row header, bottom sheets.
- Tablet `768-1023px`: 3 product columns, filters in panel.
- Desktop `>= 1024px`: 4-5 product columns, filters in left column.
- Catalog filters: desktop left column `280px`; mobile fullscreen bottom sheet.
- Product page desktop: breadcrumbs, gallery left, product info/purchase right.
- Product page mobile: gallery, title, price, CTA, characteristics; purchase block becomes sticky at bottom after scrolling below price.
- Cookie banner sits at page bottom and must not cover mobile sticky CTA; lift CTA above the banner.

## Core Components

- Header top row: city, fulfillment method, store addresses, careers, promos, Fix Price card.
- Header main row: logo, catalog button, search, login, favorites, cart.
- Search height: `48px` desktop, `44px` mobile; icon left, clear button right when filled; placeholder `Начните поиск товара`.
- Buttons: primary red for add/confirm, secondary blue for catalog/map/important navigation, tertiary transparent blue for lower-priority actions, promo yellow for promo transitions.
- Button heights: `48px` primary actions, `40px` secondary, `32px` compact.
- Product card must include square image, promo/card-price badge when applicable, two-line clamped title, price/old price/card price, availability, cart CTA, and favorite icon button.
- Product card rule: price is visually stronger than title.
- Out-of-stock CTA becomes `Сообщить о поступлении`.
- Favorite action is icon-only with accessible label.
- Badges: promo red/white, card price yellow/dark, new blue/white, available green on light green, unavailable gray on light gray.

## States And Accessibility

- Required states where relevant: default, hover, focus, filled, selected, disabled, loading, empty, error.
- Hover: subtle background darkening or border change.
- Focus: visible `2px` blue outline with `2px` offset.
- Disabled: opacity `0.5`, default cursor, no action.
- Loading: card skeletons and button spinner.
- Empty: short message plus action back to catalog.
- Error: clear problem explanation plus retry/next step.
- Text contrast must meet WCAG AA.
- Icon buttons need `aria-label`.
- Interactive targets must be at least `40x40px`.
- Form errors must be connected via `aria-describedby`.
- Price and discount cannot rely on color alone.

## Android/Figma Source Of Truth

Use this when translating Android mockups or Design System Agent notes into implementation.

- New mockups live in `Android v2.0` (`w6fzp4MqBpWjgSMGrZK0XD`).
- Legacy `Mobile App - Android` (`oOt1o1Ln0lxhbb3ZSvoOWg`) is reference only, not a source for tokens/components.
- Foundations priority: `DS - Colors`, `DS - Android typography`, `DS - Gaps`, `DS - effects`, `DS - Icons`.
- Component priority: `Android Ui-kit`, then `Android templates`, then state validation in `Android ui elements showcase`.
- Android brand/action tokens differ from web summary: `brand/color-01 #91C30F`, `brand/color-02 #0F4193`, `button/button-primary #81BB3C`, `button/button-dark #0F4193`.
- Android typography uses Roboto for UI; key styles include `Heading/H1 24/27 ExtraBold`, `Heading/H2 21/22 SemiBold`, `Heading/H3 19/23 Medium`, `Heading/H4 16/20 Medium`, body `17/16/15/14/13`, and price styles.
- Android spacing variables: `Gap/2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64`.
- Android radius variables: `radius-XS 4`, `radius-S 8`, `radius-M 16`, `radius-L 24`, `radius-XL 32`.
- Android shadow styles: use `Shadows/*`; treat `Shadows/Old/*` as legacy.
- Use DS icon libraries instead of drawing local vectors when an icon exists.

## Frontend Quality Gate

Before shipping frontend changes for this project:

- Reuse existing project patterns, components, and styling approach.
- Map styles to tokens or existing CSS variables instead of local magic values where practical.
- Preserve commerce density and scanability.
- Confirm responsive behavior for mobile, tablet, and desktop.
- Cover loading, empty, error, disabled, selected/focus states when the workflow needs them.
- Check text overflow, sticky CTA/cookie banner interaction, and product-card stability.
- Run available build/typecheck/test scripts and browser-check the changed screen when feasible.
