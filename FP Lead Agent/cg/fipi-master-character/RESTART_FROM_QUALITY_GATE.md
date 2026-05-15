# Restart From Quality Gate

Статус: новый старт после отклонения scripted/blockout попыток.

## Что Остановлено

- Все scripted Blender primitive попытки.
- Все доработки отклоненного `master candidate v0.1`.
- Все доработки `manual-sculpt-blockout` как production direction.

## Почему

Результаты не сохраняют facial identity Фипи и дают другого персонажа. Это
противоречит приоритету:

```text
character consistency > scene quality > stylization changes
```

## Новый Первый Шаг

Не моделить. Не рендерить. Не анимировать.

Сначала выполнить `Feasibility Gate`:

```text
FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md
```

## Ожидаемый Output Следующего Агента

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

## Решение FP Lead

Если агент подтверждает, что без manual sculpt / image-to-3D + manual cleanup
1:1 невозможно, задача не должна уходить в Blender primitives. Нужно выбирать
production route, который реально может сохранить персонажа.
