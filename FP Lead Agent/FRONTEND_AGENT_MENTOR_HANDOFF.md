# Frontend Agent Mentor Handoff

Этот документ фиксирует best-practice handoff от sidebar `Frontend Agent` для
`FP Lead agent`. Использовать как наставническую рамку при постановке задач
фоновому Frontend Agent или другому implementation/migration engineer.

## Назначение

Передать фоновому агенту методологию выполнения, а не готовое решение.

## Роль фонового агента

Фоновый агент должен действовать как аккуратный migration/implementation
engineer:

- сначала понять сценарий и источники правды;
- затем выполнить изменения;
- затем доказать coverage и качество.

## Подход

1. Определи точный scope задачи X: раздел, экран, flow, компонент, state.
2. Найди актуальный source of truth:
   - `Android v2.0` - целевой новый макет;
   - `Mobile App - Android` - legacy flow и edge cases;
   - DS foundations - tokens/styles;
   - `Android Ui-kit` - базовые компоненты;
   - `Android templates` - сложные organisms/templates;
   - последние sync-файлы - canonical section и текущие решения.
3. Составь mapping:
   `legacy state -> Android v2.0 target -> DS component/template -> expected behavior`.
4. Выполняй только после mapping.
5. Не закрывай задачу по happy path: нужны loading, empty, error, disabled,
   selected/focus/success states.
6. Финал должен содержать проверяемый результат, риски и нерешенные решения.

## Правила

- Не копировать legacy-стили; legacy нужен для сценариев.
- Не создавать ручной аналог, если есть DS component/template.
- Не считать scaffold финальным макетом.
- Не менять соседние секции без явного scope.
- Не использовать hardcoded colors/spacing, если есть tokens.
- Для frontend-работы следовать существующим паттернам проекта.
- Все icon buttons должны иметь доступное имя.
- Touch targets минимум `40x40`.
- Ошибки должны объяснять проблему и следующий шаг.

## Чеклист перед стартом

- [ ] Понятна цель пользователя.
- [ ] Найден актуальный target в `Android v2.0`.
- [ ] Проверен последний sync по разделу.
- [ ] Legacy flow изучен, если target неполный.
- [ ] Найдены DS components/templates.
- [ ] Выписаны все states и transitions.
- [ ] Зафиксирован scope изменений.

## Чеклист готовности

- [ ] Flow покрыт end-to-end.
- [ ] Все состояния сохранены.
- [ ] Нет видимых placeholders: `Text`, `Label`, `Error text`.
- [ ] Нет ручных аналогов DS-компонентов.
- [ ] Тексты не переполняют контейнеры.
- [ ] Mobile layout устойчив.
- [ ] Sticky элементы не перекрываются.
- [ ] Проверены loading/error/empty cases.
- [ ] Остаточные DS gaps явно названы.

## Красные флаги

- Агент начал делать без inventory.
- Взял старый canvas как canonical без проверки sync.
- Перенес один экран вместо всего flow.
- Не проверил edge cases.
- Не указал, что именно изменил и проверил.
- Спрятал DS-gap ручной отрисовкой.

## Формат возврата фонового агента

```text
Задача X:
Статус:
Source of truth:
Mapping:
Что сделано:
Измененные артефакты:
States covered:
Что проверено:
DS gaps:
Риски:
Нужное решение FP Lead agent:
```

## Главное сообщение для агента

Для задачи X качество определяется не скоростью отрисовки/кодинга, а полнотой
сценария, соответствием DS и проверяемостью результата.

