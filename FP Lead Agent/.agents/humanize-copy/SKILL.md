---
name: humanize-copy
description: Rewrites Russian or English text so it sounds natural, clear, warm, and human. Use when the user asks to humanize copy, make text less robotic, simplify wording, rewrite UI text, marketing text, messages, emails, onboarding copy, errors, empty states, CTA labels, product descriptions, posts, or any text that should feel more alive and understandable without losing meaning.
---

# Humanize Copy

Use this skill to rewrite text so it feels like a real person wrote it: clear, specific, concise, and appropriate for the audience.

## Workflow

1. Preserve the original meaning and factual claims.
2. Identify the context: interface, landing page, email, chat message, post, product copy, support text, or documentation.
3. Remove bureaucratic, generic, inflated, and AI-like phrasing.
4. Prefer concrete verbs, active voice, shorter sentences, and natural rhythm.
5. Keep the tone useful and alive, not overly casual unless the user asks for it.
6. Match the user's language. If the source is Russian, answer in Russian; if English, answer in English.
7. If the text is for UI, make it shorter, scannable, and action-oriented.
8. If the text is for conversion, keep the promise specific and make the next action obvious.

## Output

For a direct rewrite request, return the improved version first.

When useful, add 2-3 alternatives with different tone labels:

- `Нейтрально`
- `Теплее`
- `Смелее`
- `Короче`
- `Премиальнее`

Only explain changes when the user asks or when the text has a meaningful product risk.

## Style Rules

- Replace vague claims like "innovative solution" with the concrete value.
- Replace formal phrases like "осуществляется", "является", "в рамках" with simpler wording.
- Avoid fake enthusiasm, hype, and overpromising.
- Avoid filler intros such as "Мы рады сообщить", unless the context truly needs it.
- Keep CTA labels short: verb + object when possible.
- Keep error text calm: state what happened, why it matters, and what to do next.
- Keep empty states helpful: name the state, then offer a clear next step.

## Product Copy Checks

Before finalizing, check:

- Does the user instantly understand what is being offered?
- Is the sentence something a real person could say out loud?
- Are there any abstract nouns that can become concrete?
- Is the tone appropriate for trust, price point, and user stress level?
- Can any sentence be shorter without losing meaning?
