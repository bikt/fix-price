# Design System Agent Mentor Handoff

Этот документ фиксирует best-practice handoff от sidebar `Design System Agent`
для `FP Lead agent`. Использовать как наставническую рамку при постановке задач
фоновым агентам, особенно для Figma-сборки, миграций legacy-flow и проверки
экранов на дизайн-систему.

## Назначение

Для фонового агента по задаче X нужно передать рамку: он не "рисует экран", а
восстанавливает продуктовый сценарий на дизайн-системе.

## Подход

### 1. Понять задачу

- source: откуда берем сценарий;
- target: куда собираем;
- пользовательская цель;
- обязательные состояния;
- связанные разделы, которые нельзя дублировать.

### 2. Построить карты до сборки

- `legacy frame/state -> new frame/state`;
- `legacy block -> DS component/template`;
- `screen -> user goal`;
- `transition -> destination`;
- `state -> trigger`.

### 3. Использовать источники по приоритету

- foundations: Colors, Typography, Gaps, Effects, Icons;
- `Android Ui-kit`;
- `Android templates`;
- `Android ui elements showcase`;
- существующие экраны в `Android v2.0`;
- legacy только как reference сценария.

## Правила

- Не копировать legacy-стили.
- Не делать ручной аналог, если есть DS-компонент.
- Не дублировать существующий flow, а связывать вход/выход.
- Все состояния должны быть покрыты: default, loading, error, empty, disabled,
  success, edge cases.
- Все переходы должны быть видимыми и подписанными.
- Любой placeholder в финале запрещен или фиксируется как DS debt.
- Закрытие возможно только при `100% flow coverage + DS pass + QA pass`.

## Чеклист

### Перед стартом

- [ ] Source и target ясны.
- [ ] Scope не размыт.
- [ ] Список экранов и состояний составлен.
- [ ] Существующие связанные разделы найдены.
- [ ] DS-компоненты и templates найдены.
- [ ] Риски и gaps записаны.

### Во время работы

- [ ] Используются variables, text styles, spacing/effects/icons из DS.
- [ ] Компоненты берутся из `Android Ui-kit`.
- [ ] Организмы и сценарные блоки берутся из `Android templates`.
- [ ] Состояния сверяются через showcase.
- [ ] Имена frames понятные и трассируемые.
- [ ] Связи между экранами явно показаны.

### Перед сдачей

- [ ] Нет orphan frames.
- [ ] Нет локальных цветов/типографики без причины.
- [ ] Нет detached components без причины.
- [ ] Нет видимых placeholders.
- [ ] Все состояния legacy покрыты или осознанно вынесены в другой flow.
- [ ] Есть migration map, DS reuse map, linkage map и QA verdict.

## Формат ответа фонового агента

```text
Задача:
Source:
Target:
Что собрано:
Migration map:
DS reuse map:
Linkage map:
Покрытые состояния:
Непокрытые состояния:
DS gaps:
QA findings:
Verdict:
Что нужно решить FP Lead agent:
```

## Ключевая установка

Фоновый агент должен быть системным сборщиком, а не автором нового дизайна.
Цель: сохранить полный пользовательский сценарий и пересобрать его на новой
дизайн-системе максимально чисто.

