# Low Level Design — Per Module Pipelines

Detailed flow for each module showing exactly what happens at each step.

---

## Module 01 — Git & GitHub Fundamentals

```mermaid
flowchart LR
    A["🖊️ Write Code\n(feature branch)"] --> B["git add\ngit commit"]
    B --> C["git push origin\nfeature/my-feature"]
    C --> D["Open Pull Request\non GitHub"]
    D --> E["Code Review\n(comments / approvals)"]
    E -->|approved| F["Merge to main"]
    F --> G["git tag v0.1.0"]
    G --> H["GitHub Release\ncreated"]

    style A fill:#e3f2fd
    style F fill:#e8f5e9
    style H fill:#fff3e0
```

**Key files:** `.gitignore`, `CHANGELOG.md`, branch protection rules

---

## Module 02 — GitHub Actions CI Pipeline

```mermaid
flowchart TD
    PUSH["git push / PR opened"] --> TRIGGER["GitHub Actions triggered\n(.github/workflows/ci.yml)"]

    TRIGGER --> CHECKOUT["actions/checkout\n(clone repo)"]
    CHECKOUT --> SETUP["actions/setup-python\n(3.10, 3.11, 3.12)"]
    SETUP --> CACHE["Cache pip dependencies\n(faster reruns)"]
    CACHE --> INSTALL["pip install -r requirements.txt"]

    INSTALL --> LINT["flake8\n(style + syntax check)"]
    INSTALL --> TEST["pytest\n(unit tests + coverage)"]

    LINT -->|pass| MERGE_OK["✅ All checks passed\nPR ready to merge"]
    LINT -->|fail| BLOCK["❌ PR blocked\nfix lint errors first"]
    TEST -->|pass| MERGE_OK
    TEST -->|fail| BLOCK

    style MERGE_OK fill:#e8f5e9
    style BLOCK fill:#ffebee
```

**Key files:** `.github/workflows/ci.yml`, `requirements.txt`, `tests/`

---

## Module 03 — SonarCloud Code Quality Gate

```mermaid
flowchart TD
    PR["Pull Request opened"] --> ACTIONS["GitHub Actions CI runs"]
    ACTIONS --> COVERAGE["pytest --cov\n(generate coverage report)"]
    COVERAGE --> SONAR["SonarCloud Scanner\n(upload results)"]

    SONAR --> ANALYSIS["SonarCloud Analysis"]
    ANALYSIS --> BUGS["Bug Detection"]
    ANALYSIS --> SMELLS["Code Smells"]
    ANALYSIS --> DUPL["Duplication Check"]
    ANALYSIS --> COV["Coverage %"]

    BUGS --> GATE{"Quality Gate"}
    SMELLS --> GATE
    DUPL --> GATE
    COV --> GATE

    GATE -->|pass| BADGE["✅ Badge: passed\nPR can merge"]
    GATE -->|fail| FAIL["❌ Badge: failed\nPR blocked"]

    style BADGE fill:#e8f5e9
    style FAIL fill:#ffebee
```

**Key files:** `sonar-project.properties`, `.github/workflows/sonar.yml`

---

## Module 04 — Jenkins Pipeline (Self-hosted)

```mermaid
flowchart TD
    DEV["Developer pushes to GitHub"] --> WEBHOOK["GitHub Webhook\n→ notifies Jenkins"]
    WEBHOOK --> QUEUE["Jenkins build queue"]
    QUEUE --> AGENT["Jenkins Agent\n(Docker container)"]

    AGENT --> JFILE["Read Jenkinsfile"]

    JFILE --> S1["Stage: Checkout\ngit clone"]
    S1 --> S2["Stage: Install\npip install"]
    S2 --> S3["Stage: Lint\nflake8"]
    S3 --> S4["Stage: Test\npytest"]
    S4 --> S5["Stage: Report\npublish test results"]

    S5 -->|all green| SUCCESS["✅ Build SUCCESS\nBlue Ocean dashboard"]
    S3 -->|fail| FAILED["❌ Build FAILED\nemail notification"]
    S4 -->|fail| FAILED

    style SUCCESS fill:#e8f5e9
    style FAILED fill:#ffebee
```

**Key files:** `Jenkinsfile`, `docker-compose.yml` (local Jenkins)

---

## Module 05 — Full CI/CD Pipeline (Code to Live)

```mermaid
flowchart TD
    PUSH["Push to main branch"] --> CI["CI: lint + test + quality gate"]

    CI -->|all pass| BUILD["Build Stage\npython -m build"]
    BUILD --> DEV_DEPLOY["Deploy to DEV\n(auto, every push)"]
    DEV_DEPLOY --> SMOKE["Smoke Test\n(basic health check)"]

    SMOKE -->|pass| STAGING["Deploy to STAGING\n(auto, every push to main)"]
    STAGING --> MANUAL["Manual Approval\n(GitHub environment protection)"]
    MANUAL -->|approved| PROD["Deploy to PROD\n(Render / Railway)"]
    PROD --> MONITOR["🌐 Live URL\nmonitoring active"]

    CI -->|any fail| STOP["🛑 Pipeline stopped\nno deploy"]

    style PROD fill:#e8f5e9
    style MONITOR fill:#e8f5e9
    style STOP fill:#ffebee
```

**Key files:** `.github/workflows/deploy.yml`, `render.yaml` or `railway.json`

---

## Module 06 — Release Management

```mermaid
flowchart TD
    COMMIT["Conventional Commits\nfeat: / fix: / chore:"] --> MAIN["Merge to main"]
    MAIN --> TAG["Developer pushes tag\ngit tag v1.2.0\ngit push --tags"]

    TAG --> RELEASE_WF["GitHub Actions\nrelease.yml triggered"]

    RELEASE_WF --> CHANGELOG["Auto-generate CHANGELOG\nfrom commit messages"]
    CHANGELOG --> GH_RELEASE["Create GitHub Release\nwith release notes"]
    GH_RELEASE --> ARTIFACT["Attach build artifacts\n(.zip / .whl)"]
    ARTIFACT --> NOTIFY["Notify team\n(optional Slack / email)"]

    style GH_RELEASE fill:#e8f5e9
    style NOTIFY fill:#fff3e0
```

**Versioning rules:**
- `feat:` commit → bumps **minor** version (1.0.0 → 1.1.0)
- `fix:` commit → bumps **patch** version (1.0.0 → 1.0.1)
- `BREAKING CHANGE` → bumps **major** version (1.0.0 → 2.0.0)

**Key files:** `.github/workflows/release.yml`, `CHANGELOG.md`, `.commitlintrc`
