---
name: threejs-3d
description: Builds and improves interactive web 3D experiences with Three.js, React Three Fiber, shaders, cameras, lighting, materials, loaders, controls, animation, and responsive canvas layout. Use when the user asks for 3D on a website or app, WebGL, Three.js, React Three Fiber, product viewers, configurators, hero scenes, games, or interactive 3D UI.
---

# Three.js 3D

Use this skill for web-based 3D: Three.js, React Three Fiber, WebGL scenes, product viewers, configurators, interactive hero scenes, small games, and canvas performance fixes.

## Workflow

1. Inspect the existing app stack before choosing plain Three.js or React Three Fiber.
2. Make the 3D scene the actual usable experience, not a decorative placeholder.
3. Define stable canvas dimensions and responsive constraints.
4. Set camera, lighting, controls, animation loop, and resize behavior deliberately.
5. Prefer proven loaders and helpers for GLTF/GLB, environment maps, orbit controls, postprocessing, and physics.
6. Keep animation meaningful and performant; avoid excessive particles or visual noise.
7. Verify that the canvas is nonblank, framed correctly, and interactive at desktop and mobile sizes.

## Implementation Standards

- Use Three.js for vanilla apps and `@react-three/fiber` only when the project already uses React or benefits from it.
- Use `requestAnimationFrame` cleanup or React cleanup to avoid leaking render loops.
- Dispose geometry, materials, textures, and renderers when unmounting.
- Handle device pixel ratio with a reasonable cap, usually `Math.min(window.devicePixelRatio, 2)`.
- Use `ResizeObserver` or container-aware sizing when the canvas is embedded in UI.
- Use named groups and functions for complex scenes.
- Add fallbacks for failed asset loading.
- Keep UI overlays outside the canvas but avoid blocking core interactions.

## Visual Direction

- Use real or generated assets when the user needs to inspect a product, place, object, or character.
- For abstract 3D, make the motion and shape communicate state or purpose.
- Avoid one-note palettes and purely decorative gradient backgrounds.
- Use shadows, ambient occlusion, bevels, and material roughness to improve depth.

## Verification

Before finalizing, check:

- The canvas renders nonblank.
- The camera frames the primary subject.
- Assets load from correct paths.
- Controls work with mouse and touch.
- Text and overlays do not collide with the canvas.
- Mobile layout preserves the subject and interaction area.
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

