---
name: front-end
description: Builds, fixes, and improves front-end applications, websites, UI components, layouts, styling, responsive behavior, accessibility, state handling, forms, animations, and browser bugs. Use when the user asks for frontend work with HTML, CSS, JavaScript, TypeScript, React, Next.js, Vite, Tailwind, design implementation, UI polish, adaptive layouts, or client-side product features.
---

# Front-End

Use this skill for practical front-end engineering: building usable interfaces, implementing designs, fixing UI bugs, improving layouts, adding interactions, and making apps feel polished across desktop and mobile.

## Project Memory

For Fix Price work, read `fix-price-design-memory.md` in this folder before implementing UI. It captures the Design System Agent handoff: product principles, web tokens, responsive rules, component requirements, Android/Figma source priority, states, accessibility, and frontend quality gates.

Also read the project orchestration context:

- `../../AGENTS.md`
- `../AGENT_ORCHESTRATION.md`

In the Fix-Price team you are `Frontend Agent`. Your role starts when UI or flow
work needs to become application code: routing, state, data flow, API
integration, build behavior, tests, and technical verification. Keep the UI
implementation aligned with `UX Agent`, `Design System Agent`, and `UI Agent`
handoffs.

## Workflow

1. Inspect the existing stack, scripts, routing, styling system, and component conventions before editing.
2. Prefer the project's current patterns over adding new libraries or abstractions.
3. Build the actual usable screen or feature, not a marketing placeholder.
4. Keep edits scoped to the relevant components, styles, and tests.
5. Make responsive behavior explicit with stable layout constraints.
6. Ensure loading, empty, error, disabled, hover, focus, and active states exist when the workflow needs them.
7. Verify the result with the project's available checks and, when useful, a browser/dev server.

## UI Implementation Standards

- Use semantic HTML and accessible labels where appropriate.
- Use existing design tokens, utilities, components, and icon libraries.
- Keep cards, modals, toolbars, buttons, inputs, and nav patterns consistent with the app.
- Avoid nested cards and decorative UI that does not support the workflow.
- Use icons for familiar actions when an icon library exists.
- Keep text inside buttons and compact UI from overflowing.
- Do not scale font sizes directly with viewport width.
- Make fixed-format UI stable with `aspect-ratio`, grid tracks, min/max sizes, or container constraints.

## React Standards

- Keep components small enough to read, but avoid premature abstraction.
- Use controlled state where it improves predictability.
- Clean up event listeners, timers, subscriptions, animation frames, and observers.
- Memoize only when there is a clear performance reason.
- Keep client/server boundaries clear in Next.js.
- Avoid duplicating source of truth across local state, URL state, and server data.

## Styling Standards

- Prefer the existing styling approach: CSS modules, Tailwind, global CSS, styled components, or design-system classes.
- Use layout primitives deliberately: flex for one-dimensional alignment, grid for two-dimensional layouts.
- Keep spacing, typography, and color hierarchy consistent.
- Avoid one-note palettes and excessive gradients.
- Ensure focus states are visible and contrast is usable.

## Verification

Before finalizing, check:

- Does the app build or typecheck if a script exists?
- Does the changed screen work on mobile and desktop widths?
- Are interactive states visible and stable?
- Is there any text overflow or layout shift?
- Do browser console errors appear during the main workflow?
- Did the change avoid unrelated refactors?
