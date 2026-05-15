# CG Character Quality Gate

Статус: mandatory gate  
Дата фиксации: 2026-05-15  
Область: все задачи с каноничным 3D-персонажем Фипи

## Главная Причина

Предыдущие попытки через scripted Blender primitives дали другого персонажа.
Такой метод не сохраняет facial identity, силуэт и органику Фипи. Поэтому для
каноничного персонажа 1:1 вводится обязательный quality gate до начала
производства.

## Базовое Правило

CG-agent не имеет права сразу моделить, рендерить, ригать или анимировать
каноничного персонажа. Сначала он обязан пройти `Feasibility Gate` и вернуть
план производства, риски и допустимый метод.

## Запрещено Для Canonical Character

- procedural Blender из шаров, капсул, цилиндров и лепестков как финальный путь;
- "еж по мотивам";
- улучшение отклоненной болванки;
- новый персонаж в похожих цветах;
- переход в texture/rig/animation до approval формы и лица;
- Figma insertion до approval render;
- утверждение `ready`, если facial identity не совпадает.

## Разрешенные Методы Для 1:1 Character

Допустимые production routes:

1. **Manual Sculpt**
   - Blender/ZBrush sculpt;
   - ручная проработка лица, тела, иголок, рук, стоп;
   - retopo, UV, textures, rig.

2. **Image-To-3D Base + Manual Cleanup**
   - генерация базовой формы специализированным image-to-3D инструментом;
   - ручная чистка в Blender;
   - обязательная доработка лица, silhouette, spines, hands.

3. **Professional Character Modeling**
   - моделинг по reference pack;
   - отдельные passes: blockout, sculpt, retopo, lookdev, rig.

Недопустимый route:

```text
scripted primitives -> "almost mascot" -> details -> rig
```

## Feasibility Gate

Перед любой работой агент должен вернуть:

```text
Task:
Target similarity:
Available references:
Missing references:
Recommended method:
Rejected methods:
Risks:
Expected failure signs:
Required approvals:
First output:
Verdict:
```

Допустимые verdict:

- `can proceed to reference/silhouette planning`;
- `blocked, needs more references`;
- `blocked, requires manual sculpt/human artist`;
- `blocked, current tools cannot deliver 1:1`.

## Stage Approval

Работа идет только по стадиям:

1. Reference pack approval.
2. Feasibility gate approval.
3. Silhouette blockout approval.
4. Face blockout approval.
5. Spines/hands/feet approval.
6. Sculpt detail approval.
7. Retopo/UV approval.
8. Material/lookdev approval.
9. Rig approval.
10. Animation/scene approval.

Нельзя переходить к следующей стадии без явного approval предыдущей.

## Stop-Loss Rule

Если первый preview не похож:

- не детализировать;
- не делать "еще чуть-чуть";
- не ригать;
- не текстурить;
- остановиться;
- зафиксировать mismatch;
- предложить другой production route.

## Comparison Standard

Каждый visual preview должен иметь:

- слева canonical reference;
- справа результат;
- одинаковый масштаб персонажа;
- фронтальный ракурс;
- нейтральный фон;
- список расхождений;
- честный verdict.

## Acceptance Standard

Preview не проходит, если:

- персонаж без контекста не узнается как Фипи;
- лицо выглядит как другой персонаж;
- глаза не совпадают по форме/характеру;
- рот не совпадает по настроению и форме;
- силуэт другой;
- иголки выглядят как пластиковые листья;
- руки/кисти не похожи на reference;
- belly patch уходит на лицо;
- цветовая схема нарушена;
- метод не даст reusable mesh/UV/rig.

## FP Lead Rule

FP Lead agent принимает решение по методу до старта production. Если задача
содержит "1 в 1", "каноничный", "тот же персонаж", "master character", то
быстрый scripted generation автоматически запрещен.

## Current Decision

Все предыдущие scripted/blockout результаты по Фипи отклонены как visual
master. Они остаются только как negative examples и technical artifacts.

Новый старт начинается с Feasibility Gate, а не с Blender render.
