# Designer Skill Profile

Professional skill stack for developing and maintaining the Fix Price Android design system.

## Core Skills

Use these skills by default for design-system work:

| Skill | Role in DS work |
| --- | --- |
| `design-system` | Token, component, variant, state, and consistency governance. |
| `design-leadership` | Design quality bar, review process, ownership, maturity, and contribution model. |
| `senior-product-designer` | Product logic, UX/UI audit, scenario quality, prioritization, and trade-offs. |
| `mobile-ux` | Android ergonomics, touch targets, mobile flow structure, bottom sheets, navigation. |
| `interaction-designer` | Component behavior, transitions, gesture logic, feedback, loading and error interactions. |
| `design-grids` | Layout grid, rhythm, spacing systems, alignment rules, density and hierarchy. |
| `visual-enhancer` | Visual hierarchy, typography, spacing, color balance, polish. |
| `ui-critic` | Practical UI critique and concrete fixes for screens and components. |
| `heuristic-eval` | Nielsen-style checks: feedback, consistency, control, error prevention, recognition. |
| `usability-tester` | User-perspective walkthroughs and friction detection. |
| `ux-research` | Hypotheses, validation questions, research framing, usability test plans. |
| `ux-writing` | Interface copy, labels, empty states, errors, short and useful microcopy. |

## Supporting Skills

Use these only when the task needs them:

| Skill | Use when |
| --- | --- |
| `front-end` | Preparing implementation notes, design-to-code handoff, CSS/token mapping, QA with engineering. |
| `system-analyst-superpower` | Clarifying requirements, data/state logic, edge cases, business rules. |
| `conversion-optimizer` | Optimizing funnel screens, sign-in, checkout, cart, promo and retention flows. |
| `humanize-copy` | Making long-form product or support text feel more natural. |
| `design-superpower` | Broad design exploration when a task is conceptually open. |
| `superpower-ux-researcher` | Deeper research synthesis or larger discovery work. |

## Usually Out Of Scope

Do not use these for normal Android DS work unless explicitly requested:

- `blender-3d`
- `threejs-3d`

## Operating Mode

For every design-system task:

1. Start with `design-system` and `senior-product-designer`.
2. Add `mobile-ux` for screens, flows, Android patterns, and touch behavior.
3. Add `design-grids` and `visual-enhancer` for layout, spacing, hierarchy, and polish.
4. Add `interaction-designer` when states, gestures, transitions, feedback, or component behavior matter.
5. Add `ui-critic`, `heuristic-eval`, and `usability-tester` for review and QA.
6. Add `ux-writing` when labels, messages, navigation text, errors, or empty states are involved.
7. Add `ux-research` when assumptions need validation or a task needs research questions.
8. Add `design-leadership` when the work affects process, governance, contribution rules, or team standards.

## Fix Price Android DS Rules

Use `design-system-map.md` as the source of truth for the Figma file structure.

New Android layouts should be created in `Android v2.0`.

Use:

- `DS - Colors` for color variables.
- `DS - Android typography` for text styles.
- `DS - Gaps` for spacing variables.
- `DS - effects` for radius, shadows, and blur.
- `DS - Icons` for icons.
- `Android Ui-kit` for base components.
- `Android templates` for complex organisms and screen templates.
- `Android ui elements showcase` to verify states.
- `Mobile App - Android` only as legacy reference.

## Quality Gate

Before considering a DS task complete, check:

- No avoidable local colors, local typography, detached icons, or ad hoc spacing.
- Components use actual DS instances where available.
- Variants and slots are set intentionally.
- Loading, empty, error, disabled, selected, pressed, and default states are covered when relevant.
- Android touch targets and navigation patterns are respected.
- Screen/frame naming is clear and traceable to the source task.
- Handoff notes are specific enough for design and engineering review.
