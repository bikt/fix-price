# Fix-Price Data Model

Визуализированная модель данных проекта Fix-Price. Использовать как карту сущностей для базы знаний, Buildin-канбана и дизайн-системных источников.

Кликабельная версия графа: [`data-model-graph.html`](data-model-graph.html).

## Scope

Модель описывает не продуктовую backend-БД, а рабочие данные проекта:

- локальный проект и его документацию;
- внешнюю базу знаний Buildin;
- канбан Fix-Price;
- задачи и страницы;
- источники дизайн-системы в Figma;
- правила сборки Android-макетов.

## Entity Relationship Model

```mermaid
erDiagram
    PROJECT ||--|| LOCAL_WORKSPACE : "stored in"
    PROJECT ||--o{ PROJECT_DOCUMENT : "documents"
    PROJECT ||--|| BUILDIN_SPACE : "uses knowledge base"
    PROJECT ||--o{ FIGMA_SOURCE : "references"
    PROJECT ||--o{ BUILD_RULE : "defines"

    LOCAL_WORKSPACE ||--o{ AGENT_FOLDER : "contains"

    BUILDIN_SPACE ||--|| BUILDIN_PAGE : "contains"
    BUILDIN_PAGE ||--|| KANBAN_BOARD : "contains"
    KANBAN_BOARD ||--o{ KANBAN_COLUMN : "groups"
    KANBAN_COLUMN ||--o{ KANBAN_CARD : "contains"
    KANBAN_CARD ||--o{ CARD_NOTE : "may include"

    FIGMA_SOURCE ||--o{ DESIGN_ASSET : "provides"
    DESIGN_ASSET ||--o{ BUILD_RULE : "constrains"

    PROJECT {
        string name "fix-price"
        string currentPath "C:\\Users\\mrbik\\Desktop\\AI projects\\projects\\fix-price"
        string previousRoot "C:\\Users\\mrbik\\Desktop\\claude"
        string currentRoot "C:\\Users\\mrbik\\Desktop\\AI projects"
    }

    LOCAL_WORKSPACE {
        string rootPath
        string projectPath
        string agentsPath
    }

    PROJECT_DOCUMENT {
        string filename
        string role
        string format
    }

    BUILDIN_SPACE {
        string url
        string accessType "invite/cooperate"
    }

    BUILDIN_PAGE {
        string title "Работа"
        string purpose "project knowledge base"
    }

    KANBAN_BOARD {
        string title "Fix-Price"
        string view "Kanban"
    }

    KANBAN_COLUMN {
        string name
        int visibleCount
    }

    KANBAN_CARD {
        string title
        string column
        string type "page/task"
    }

    CARD_NOTE {
        string contentType
        string body
    }

    FIGMA_SOURCE {
        string role
        string fileName
        string figmaKey
    }

    DESIGN_ASSET {
        string layer
        string assetType
        string sourceFile
    }

    BUILD_RULE {
        string name
        string description
        string priority
    }

    AGENT_FOLDER {
        string path
        string skillFile "SKILL.md"
        string metadataFile "agents\\openai.yaml"
    }
```

## Knowledge Flow

```mermaid
flowchart LR
    Buildin["Buildin page<br/>Работа / Fix-Price"] --> Context["PROJECT_CONTEXT.md"]
    Buildin --> Kanban["Kanban board<br/>Work"]
    Map["design-system-map.md"] --> Sources["Figma source files"]
    Sources --> Foundations["Foundations<br/>Colors, Typography, Gaps, Effects, Icons"]
    Sources --> Components["Components<br/>Android Ui-kit"]
    Sources --> Templates["Templates<br/>Android templates"]
    Foundations --> Rules["Build rules"]
    Components --> Rules
    Templates --> Rules
    Rules --> Mockups["New Android mockups<br/>Android v2.0"]
    Context --> Work["Project work"]
    Kanban --> Work
```

## Kanban Model

```mermaid
flowchart TB
    Board["Fix-Price Kanban"] --> Backlog["Backlog"]
    Board --> Today["Today"]
    Board --> Progress["In progress"]
    Board --> Done["Done"]

    Backlog --> B1["FPDS Страницы"]
    Backlog --> B2["Из ретро"]
    Backlog --> B3["тест1"]

    Today --> T1["fpds магазины"]
    Today --> T2["fpds главная"]
    Today --> T3["codex-test"]

    Progress --> P1["fpds поиск"]
    Progress --> P2["fpds акции"]
```

## Design Source Taxonomy

```mermaid
mindmap
  root((Fix-Price Design Data))
    Foundations
      DS - Colors
        Theme Colors
        Light mode
        Dark mode
      DS - Android typography
        Roboto text styles
        Heading
        Body
        Caps
      DS - Gaps
        Dimensions
        Breakpoints
        Gap scale
      DS - effects
        Radius
        Shadows
        Blur
      DS - Icons
        Outline
        Filled
        Catalog
    Component Layer
      Android Ui-kit
        Button
        Input
        Product card
        Search
        NavBar
        Bottom Sheet
      Android ui elements showcase
        Component states
        Validation reference
    Template Layer
      Android templates
        Главная
        Профиль
        Каталог
        Корзина
        Чекаут
        Магазины
        Акции
    App Layout
      Android v2.0
        Target file
        New screens
      Mobile App - Android
        Legacy reference
```

## Current Seed Data

| Entity | Value | Notes |
| --- | --- | --- |
| Project | `fix-price` | Current local project |
| Local project path | `C:\Users\mrbik\Desktop\AI projects\projects\fix-price` | Current source of local knowledge files |
| Buildin URL | `https://buildin.ai/5d857221-669e-480d-bc9e-8261f9baad5a` | External knowledge base |
| Buildin page | `Работа` | Contains Fix-Price kanban |
| Board | `Fix-Price` | Kanban view under `Work` |
| Column | `Backlog` | Contains `тест1` |
| Column | `Today` | Contains `codex-test` |
| Test card | `codex-test` | Has lorem ipsum in description |
| Test page | `тест1` | Created in Backlog |

## Cardinality Rules

| Rule | Meaning |
| --- | --- |
| One project has one current local workspace | The active path is fixed in `PROJECT_CONTEXT.md` and `design-system-map.md`. |
| One project can reference many Figma source files | Design data is split across foundation, component, template, and app files. |
| One Buildin page can contain one or more project boards | Current known board is Fix-Price. |
| One kanban board contains many columns | Known columns include Backlog, Today, In progress, Done. |
| One kanban column contains many cards/pages | Cards represent project tasks or knowledge pages. |
| One design source provides many design assets | Assets become constraints for build rules and new mockups. |

## Maintenance Rules

- When a new Buildin card/page is created, add it to `Current Seed Data` if it becomes meaningful project context.
- When a new Figma file becomes a source of truth, add it to `design-system-map.md` first, then reflect it here.
- Keep this model conceptual. Product API schemas, database tables, or analytics events should get separate models if they appear later.
