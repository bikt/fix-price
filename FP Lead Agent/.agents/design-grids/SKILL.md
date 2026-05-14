---
name: design-grids
description: Designs, critiques, and improves layout grids, modular systems, progressive grids, asymmetric compositions, force lines, visual rhythm, alignment, spacing, editorial layouts, landing pages, dashboards, portfolios, mobile layouts, and unconventional UI compositions. Use when the user asks about design grids, modular grids, composition, layout structure, non-standard layouts, golden ratio, dynamic grids, Swiss grids, force lines, visual hierarchy, balance, rhythm, or making an interface feel more structured and expressive.
---

# Design Grids

Use this skill to create and critique strong visual structure: grids, modules, rhythm, force lines, alignment systems, and expressive compositions that still remain usable.

## Core Principle

A grid is not decoration. It is a decision system for hierarchy, rhythm, grouping, scanning, and emphasis. Use standard grids for clarity, and break them only with intent.

## Workflow

1. Identify the content type: dashboard, landing page, portfolio, editorial page, product page, mobile flow, tool UI, or presentation.
2. Determine the desired feeling: calm, premium, technical, editorial, dense, cinematic, playful, experimental, or operational.
3. Choose the grid strategy before placing details.
4. Define columns, gutters, margins, modules, baseline rhythm, and key alignment axes.
5. Place primary content on strong structural lines.
6. Use controlled breaks for emphasis: scale shift, asymmetry, overlap, offset, diagonal force, or negative space.
7. Check readability, scanning, adaptive behavior, and implementation feasibility.

## Grid Types

### Column Grid

Use for websites, dashboards, SaaS, product pages, and responsive layouts.

- Define container width, columns, gutters, and margins.
- Use 4 columns on mobile, 8 on tablet, 12 on desktop as a default only when it fits the product.
- Avoid filling every column; use columns to create relationships and controlled empty space.

### Modular Grid

Use for cards, galleries, editorial layouts, catalogs, case studies, dashboards, and dense systems.

- Define both column and row rhythm.
- Keep modules repeatable, but vary spans to create hierarchy.
- Use consistent image ratios, chart heights, and card baselines.

### Baseline Grid

Use for text-heavy, premium, editorial, or documentation experiences.

- Tie headings, body text, captions, and metadata to a shared vertical rhythm.
- Use line height and spacing as the grid, not only visible columns.

### Progressive Grid

Use when the composition should become richer or more expressive as the page unfolds.

- Start with a simple, stable structure.
- Introduce wider spans, offsets, asymmetry, or layered modules in later sections.
- Keep one or two recurring alignment anchors so the page does not feel random.

### Asymmetric Grid

Use for portfolios, hero sections, editorial pages, high-impact product pages, and creative brands.

- Balance visual weight, not equal widths.
- Use unequal columns such as 5/7, 4/8, 3/6/3, or 2/5/5.
- Anchor at least one edge or baseline across elements.

### Force-Line Composition

Use for cinematic, expressive, campaign, hero, and presentation layouts.

- Identify directional energy: horizontal stability, vertical authority, diagonal motion, radial focus, or Z-pattern scanning.
- Place key subject, headline, CTA, and supporting content along the force lines.
- Use lines of sight, object edges, image perspective, motion trails, or whitespace to guide attention.
- Avoid placing all elements at the center unless stillness is intentional.

### Broken Grid

Use sparingly for emphasis, art direction, or premium/editorial expression.

- Break only one or two rules at once.
- Keep typography, spacing, or color disciplined so the broken structure still feels designed.
- Make sure interactive controls remain predictable.

## Practical Layout Recipes

### Premium Landing Page

- Wide container with generous margins.
- 12-column or asymmetric 5/7 grid.
- Large image or product signal aligned to a strong vertical.
- Headline and CTA placed on a stable axis.
- Secondary content peeking below the first viewport.

### SaaS Dashboard

- Dense but calm column grid.
- Fixed sidebar or top nav rhythm.
- Reusable card heights and chart modules.
- Strong table alignment.
- Minimal decorative breaks.

### Portfolio Case Study

- Editorial modular grid.
- Alternate wide media, narrow text, process artifacts, and pull quotes.
- Use progressive variation section by section.
- Keep captions and metadata on consistent rails.

### Mobile Interface

- Use 4-column or spacing-token grid.
- Align controls to thumb-friendly zones.
- Use vertical rhythm more than complex columns.
- Avoid tiny asymmetry that looks accidental on small screens.

## Critique Checklist

Check:

- Where does the eye go first, second, third?
- Are important elements on strong axes?
- Is asymmetry balanced by weight, contrast, or whitespace?
- Are gutters and margins consistent enough to feel intentional?
- Is there a baseline rhythm for text?
- Does the layout still work when content gets longer?
- Does the grid adapt cleanly on mobile?
- Are grid breaks meaningful or just decorative?

## Output

When proposing a layout, include:

1. Recommended grid type.
2. Column/module structure.
3. Margins, gutters, and rhythm guidance.
4. Placement rules for key elements.
5. Where to intentionally break the grid.
6. Mobile adaptation.

When critiquing a layout, lead with the biggest structural issue, then give concrete changes.
## Sidebar-профиль как наставник

Этот `SKILL.md` описывает экспертный профиль sidebar-агента: best practices, правила роли и проектную память.

В новой модели sidebar-агенты используются как галерея наставников и источник качества для `FP Lead agent`. Пользователь может прокачивать этот профиль и консультироваться с ним напрямую, но основной execution-flow идет через `FP Lead agent` и фоновых агентов.

Если `FP Lead agent` запускает тебя как фонового исполнителя под задачу, работай в рамках назначенной роли и верни sync:

```text
Sync для FP Lead agent
Агент:
Задача:
Статус:
Что сделано:
Измененные артефакты:
Ссылки:
Что проверено:
Блокеры:
Нужное решение FP Lead agent:
```

Если пользователь обращается к sidebar-агенту напрямую, это считается консультацией или прокачкой профиля. Такой вывод входит в общий процесс только когда пользователь передает его обратно `FP Lead agent` или просит учесть его в текущей задаче.

