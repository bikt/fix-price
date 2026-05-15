# Fipi Master Character Bible

Версия: 1.0  
Статус: canonical character bible  
Дата фиксации: 2026-05-15  
Владелец канона: FP Lead Agent  
Персонаж: Фипи, маскот Fix Price

## 1. Главный Принцип

Фипи должен оставаться одним и тем же 3D-персонажем во всех будущих сценах.

Приоритеты:

1. Character consistency
2. Facial identity
3. Mesh, UV, texture, rig consistency
4. Scene quality
5. Styling and artistic variation

Новые сцены не должны переосмыслять дизайн персонажа. Разрешено менять позу,
анимацию, одежду, аксессуары, освещение, окружение, камеру и композицию. Сам
персонаж, его лицо, силуэт, пропорции, материалы и поверхность остаются
каноничными.

## 2. Canonical Reference

Загруженное изображение Фипи на горе является каноническим визуальным
референсом для создания master character asset.

Стабильный путь reference в проекте:

```text
FP Lead Agent/cg/fipi-master-character/reference/fipi_master_reference.png
```

Reference role:

- источник внешности персонажа;
- источник пропорций;
- источник лицевой идентичности;
- источник цветовой палитры;
- источник фактуры поверхности;
- источник формы иголок;
- источник общего эмоционального характера.

Окружение с горой, небом и облаками не является частью постоянного character
asset. Это только сцена из reference.

## 3. Master Character Asset

Первая утвержденная production-ready 3D-модель Фипи становится
`MASTER CHARACTER ASSET`.

Master asset должен включать:

- `master.blend`;
- clean quad-based mesh;
- UV unwrap;
- PBR materials;
- separated materials;
- reusable body rig;
- facial rig или набор facial shape keys;
- texture set;
- character metadata;
- turntable preview;
- neutral pose preview;
- canonical expression preview;
- validation renders.

После утверждения master asset запрещено менять без прямого решения FP Lead
Agent и пользователя.

## 4. Immutable Identity Rules

Всегда сохранять:

- структуру лица;
- форму глаз;
- посадку глаз;
- форму носа;
- форму улыбки;
- пропорции тела;
- общий силуэт;
- форму и направление иголок;
- паттерн поверхности;
- текстуры;
- материалы;
- цвета;
- особенности мимики;
- topology consistency;
- UV layout;
- rig hierarchy;
- facial identity.

Запрещено:

- делать "ежа по мотивам";
- использовать упрощенную версию Фипи;
- заменять mesh новым mesh для каждой сцены;
- менять пропорции головы, тела, рук, ног и иголок;
- переносить светлое пятно с живота на лицо;
- менять зеленое тело на другой оттенок без approval;
- менять синие иголки на другой цвет без approval;
- делать глаза, рот или нос в другом стиле;
- превращать plush/toy-like материал в пластик, металл, резину или clay;
- менять topology ради одной сцены;
- пересоздавать rig, если можно использовать master rig.

## 5. Visual Identity

### 5.1 Силуэт

Фипи - компактный, добрый, округлый маскот.

Канонический силуэт:

- цельный мягкий объем головы и тела;
- широкая верхняя часть головы;
- округлый живот;
- короткие устойчивые ноги;
- мягкие поднятые руки;
- крупные боковые уши;
- плотный гребень синих иголок сверху и по спине;
- дружелюбный, открытый и радостный образ.

Силуэт не должен выглядеть как:

- простой шар с деталями;
- капсула с руками;
- другой еж в тех же цветах;
- персонаж с агрессивной или взрослой пластикой;
- упрощенная игрушечная болванка без узнаваемой формы.

### 5.2 Пропорции

Пропорциональная логика:

- голова и тело воспринимаются как единый мягкий mascot-volume;
- живот крупный, округлый, расположен на torso;
- ноги короткие и широкие;
- руки короткие, мягкие, дружелюбные;
- кисти маленькие, с читаемыми пальцами;
- глаза крупные и выразительные;
- нос небольшой, черный, глянцевый;
- уши круглые, зеленые, с внутренней формой.

В будущих сценах допускаются pose deformation и squash/stretch только в рамках
rig, без изменения базовых пропорций master mesh.

## 6. Face Canon

Лицо - главный источник идентичности Фипи.

Обязательные признаки:

- полностью зеленое лицо без светлой маски;
- крупные овальные глаза;
- белки глаз чистые, светлые;
- зрачки черные, крупные;
- блики на глазах заметные и живые;
- взгляд дружелюбный, направлен к зрителю или в цель действия;
- брови короткие, темно-зеленые/сине-зеленые, мягко изогнутые;
- нос черный, округлый, глянцевый;
- улыбка открытая, радостная;
- рот имеет глубину, темную внутреннюю часть и язык;
- щеки и мордочка мягкие, без резких граней.

Недопустимо:

- плоские иконные глаза;
- рот как простая дуга без объема;
- испуганное выражение;
- агрессивная мимика;
- человеческая мимика, ломающая mascot-identity;
- перенос светлого живота на лицо.

## 7. Body And Belly Patch

Тело Фипи зеленое. На животе есть светло-зеленое округлое пятно.

Правила belly patch:

- находится только на torso;
- не поднимается на лицо;
- форма мягкая, овальная/округлая;
- материал такой же plush/velvety, но светлее;
- граница мягкая, без жесткой наклейки.

Недопустимо:

- светлая маска на лице;
- пятно как плоский стикер;
- пятно неправильной формы, меняющее character identity;
- слишком белый или желтый живот.

## 8. Spines Canon

Иголки - синие, мягкие, крупные, органичные.

Обязательные признаки:

- насыщенный синий цвет;
- плотный гребень сверху головы;
- продолжение по спине и бокам;
- форма похожа на мягкие объемные пряди/иголки;
- разные размеры и легкая вариативность;
- направление назад и наружу;
- материал plush/toy-like, не пластик;
- каждая иголка имеет объем, мягкую форму и читаемый силуэт.

Недопустимо:

- пластиковые листья;
- одинаковые лепестки без вариации;
- тонкие острые шипы;
- слишком темный почти черный синий;
- голубой цвет вместо брендового синего;
- отсутствие иголок по бокам и спине.

## 9. Materials And Textures

Фипи должен выглядеть как premium 3D mascot с мягкой plush/velvety
поверхностью.

Material direction:

- soft velvet/plush;
- тонкая фактура шерсти/ворса;
- мягкое рассеянное отражение;
- без жесткого пластикового блика на теле;
- нос может быть более глянцевым;
- глаза глянцевые;
- рот и язык имеют отдельные материалы.

Separated materials:

- body_green;
- belly_light_green;
- spines_blue;
- eyes_white;
- eyes_black;
- eye_highlights;
- nose_black_glossy;
- mouth_dark;
- tongue_pink;
- inner_ear_green;
- optional_clothes;
- optional_accessories.

Texture consistency:

- текстуры master asset не пересоздаются под каждую сцену;
- UV layout не меняется без approval;
- procedural noise допустим только как часть утвержденного master material;
- scene lighting не должен менять perception цвета до неузнаваемости.

## 10. Color Canon

Цвета фиксируются как perceptual canon относительно reference.

Основные цветовые зоны:

- тело: яркий живой зеленый;
- живот: светло-зеленый, мягкий;
- иголки: насыщенный фирменный синий;
- глаза: белый + черный + белые блики;
- нос: черный глянцевый;
- рот: темный бордово-коричневый/почти черный внутри;
- язык: мягкий розовый.

Новые сцены могут менять освещение, но не базовые material colors.

## 11. Topology And Rig Requirements

Production-ready требования:

- clean topology;
- преимущественно quad-based mesh;
- edge loops вокруг глаз, рта, плеч, кистей, ног;
- deform-friendly topology для рук, ног, головы и лица;
- UV unwrap без хаотичных островов;
- named objects;
- named materials;
- reusable rig;
- scale consistency;
- separated accessories;
- non-destructive modifiers where possible;
- master rig не ломается в сценах.

Rig должен поддерживать:

- neutral pose;
- arms up joyful pose;
- waving;
- jumping;
- walking/simple locomotion;
- head turn;
- eye look controls;
- blinking;
- smile controls;
- mouth open/close;
- basic squash/stretch без потери формы.

## 12. File Structure

Рекомендуемая структура:

```text
FP Lead Agent/cg/fipi-master-character/
  FIPI_CHARACTER_BIBLE.md
  reference/
    fipi_master_reference.png
  master/
    master.blend
    fipi_master_metadata.json
    previews/
      fipi_master_neutral.png
      fipi_master_joy.png
      fipi_master_turntable.mp4
      fipi_master_comparison.png
    textures/
      body_green_basecolor.png
      body_green_roughness.png
      body_green_normal.png
      belly_light_green_basecolor.png
      spines_blue_basecolor.png
      spines_blue_roughness.png
      spines_blue_normal.png
    exports/
      fipi_master.glb
      fipi_master.fbx
    rig/
      rig_notes.md
    validation/
      qa_report.md
      reference_match_notes.md
```

## 13. Scene Reuse Rules

Для любой будущей сцены использовать:

- тот же master mesh;
- те же UV;
- те же textures;
- те же materials;
- тот же rig;
- ту же facial identity;
- тот же character scale.

В сценах можно менять:

- pose;
- animation;
- clothes;
- accessories;
- lighting;
- environment;
- camera;
- composition;
- render style внутри допустимых границ.

Нельзя менять:

- лицо;
- базовый mesh;
- silhouette identity;
- цветовую схему;
- spines pattern;
- belly patch position;
- topology;
- UV layout;
- material identity.

## 14. Character QA Gate

Перед approval master asset должен пройти проверку:

- [ ] Персонаж визуально узнается как Фипи из canonical reference.
- [ ] Лицо совпадает по идентичности.
- [ ] Глаза совпадают по форме, размеру, посадке и характеру.
- [ ] Нос совпадает по форме и материалу.
- [ ] Улыбка совпадает по настроению и форме.
- [ ] Тело не выглядит как простая procedural болванка.
- [ ] Живот находится только на torso.
- [ ] Иголки синие, объемные, мягкие, органичные.
- [ ] Материалы plush/velvety, не пластик.
- [ ] Есть clean mesh и понятная topology.
- [ ] Есть UV unwrap.
- [ ] Есть separated PBR materials.
- [ ] Есть reusable rig.
- [ ] Есть facial controls или shape keys.
- [ ] Есть comparison sheet с reference.
- [ ] Есть turntable или несколько validation renders.
- [ ] Asset можно использовать в будущих сценах без пересоздания персонажа.

## 15. Future Scene QA Gate

Перед сдачей любой новой сцены:

- [ ] Использован `master.blend`, а не заново созданный персонаж.
- [ ] Mesh не заменен.
- [ ] UV не изменены.
- [ ] Textures не пересозданы.
- [ ] Rig не сломан.
- [ ] Facial identity сохранена.
- [ ] Цвета читаются как canon.
- [ ] Сцена меняет только разрешенные элементы.
- [ ] Персонаж не стал другим из-за освещения, камеры или стилизации.
- [ ] Есть preview для approval перед вставкой в Figma или публикацией.

## 16. Approval Policy

Любой новый render, animation или Figma insertion с Фипи проходит через FP Lead
Agent.

Обязательный порядок:

1. Создать или обновить asset/scene.
2. Сохранить реальные preview files в workspace.
3. Вернуть абсолютные пути.
4. FP Lead Agent открывает preview.
5. FP Lead Agent показывает результат пользователю.
6. Только после approval можно вставлять в Figma или продолжать production.

## 17. Mandatory Character Quality Gate

Для всех задач, где требуется каноничный Фипи или сходство 1:1, обязательно
сначала пройти:

```text
FP Lead Agent/cg/fipi-master-character/CG_CHARACTER_QUALITY_GATE.md
```

CG-agent не имеет права начинать моделинг, рендер, rig или animation до
Feasibility Gate. Scripted Blender primitives запрещены как финальный путь для
master character.

## 18. Standard Prompt For CG Execution

```text
Работай как production CG character artist. Используй Fipi master character bible
как обязательный source of truth. Не создавай нового персонажа и не меняй
дизайн. Если master asset уже существует, используй тот же mesh, UV, textures,
materials, rig и facial identity. В сцене можно менять только позу, анимацию,
одежду, аксессуары, свет, окружение, камеру и композицию.

Приоритет: character consistency > scene quality > stylization changes.

Перед сдачей сохрани preview/render/video как реальные файлы в workspace,
верни абсолютные пути и честно укажи, сохранена ли идентичность персонажа.
```

## 19. Current Status

Статус master asset: создан `master candidate v0.1`, отклонен как визуальный
канон. Он остается техническим pipeline/base artifact, но не считается
утвержденным Фипи.  
Статус character bible: создана.  
Текущий `master.blend` фиксирует production pipeline, структуру файлов,
metadata, reusable rig scaffold, separated materials, preview и comparison.

Стабильный путь master candidate:

```text
FP Lead Agent/cg/fipi-master-character/master/master.blend
```

Следующий шаг: manual sculpt/detail pass. Запрещено продолжать через
процедурное улучшение текущей болванки как финальный путь. Нужно вручную
восстановить facial identity, силуэт, органику иголок, руки, стопы, материалы и
clean quad topology по canonical reference.
