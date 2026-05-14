# Sync для FP Lead agent

Агент: UI/Design System execution agent, текущий sidebar-thread

Задача: стартовый sync-пинг для подключения к оркестрации FP Lead agent

Цель: передать FP Lead agent, что этот агент принял правила командной работы и готов получать задачи напрямую через общий orchestration-flow.

Scope:

- признаю FP Lead agent главным оркестратором команды Fix-Price;
- при прямых задачах в sidebar-чате сначала отдаю стартовый sync;
- после выполнения отдаю финальный sync;
- при постановке от FP Lead agent выполняю задачу в рамках своей роли и возвращаю sync;
- без sync не считаю работу включенной в общий командный план.

Статус: взял в работу

Ожидаемый результат: FP Lead agent видит этот агент/thread как доступного исполнителя для задач по Fix-Price design system, UI migration, Figma QA и связанным артефактам.

Блокеры: явный machine-readable `agent_path/thread id` в интерфейсе не отображается; идентификация зафиксирована как текущий sidebar-thread через этот sync-файл.
