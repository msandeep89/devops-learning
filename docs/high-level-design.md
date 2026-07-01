# High Level Design — DevOps Learning Project

This diagram shows how all 6 modules connect together into a single end-to-end DevOps pipeline.
A developer writes code locally, pushes to GitHub, and automated tools take it all the way to a live deployment.

```mermaid
flowchart TD
    DEV["👨‍💻 Developer\n(Local Machine)"]

    subgraph MOD01["Module 01 — Git & GitHub"]
        GIT["Git\n(version control)"]
        GH["GitHub Repository\n(remote)"]
        PR["Pull Request\n+ Code Review"]
    end

    subgraph MOD02["Module 02 — GitHub Actions"]
        CI["CI Workflow\nflake8 lint + pytest"]
        MATRIX["Matrix Build\n(Python 3.10 / 3.11 / 3.12)"]
    end

    subgraph MOD03["Module 03 — SonarCloud"]
        SCAN["Static Analysis\n(bugs, smells, coverage)"]
        GATE["Quality Gate\n(pass / fail)"]
        BADGE["README Badge"]
    end

    subgraph MOD04["Module 04 — Jenkins"]
        JFILE["Jenkinsfile\n(declarative pipeline)"]
        JAGENT["Jenkins Agent\n(Docker)"]
        JREPORT["Build + Test Report"]
    end

    subgraph MOD05["Module 05 — CI/CD Automation"]
        BUILD["Build Stage"]
        TEST["Test Stage"]
        DEPLOY["Deploy Stage\n(Render / Railway)"]
        ENV["dev → staging → prod"]
    end

    subgraph MOD06["Module 06 — Release Management"]
        TAG["Git Tag\n(v1.0.0)"]
        RELEASE["GitHub Release\n+ Changelog"]
        SEMVER["Semantic Versioning"]
    end

    LIVE["🌐 Live Application\n(public URL)"]

    DEV -->|git commit + push| GIT
    GIT -->|git push| GH
    GH -->|open PR| PR
    PR -->|triggers| CI
    CI --> MATRIX
    CI -->|triggers| SCAN
    SCAN --> GATE
    GATE -->|badge| BADGE
    GATE -->|if pass, merge to main| BUILD
    BUILD --> TEST
    TEST --> DEPLOY
    DEPLOY --> ENV
    ENV --> LIVE
    GH -->|parallel pipeline| JFILE
    JFILE --> JAGENT
    JAGENT --> JREPORT
    LIVE -->|tag release| TAG
    TAG --> SEMVER
    TAG --> RELEASE
```

---

## Tool Roles at a Glance

| Tool | Role | When it runs |
|------|------|-------------|
| **Git** | Track every code change locally | Continuously while coding |
| **GitHub** | Host code, PRs, Actions, Releases | On push / PR |
| **GitHub Actions** | Automate lint, test, deploy | On push / PR / tag |
| **SonarCloud** | Enforce code quality standards | On every PR |
| **Jenkins** | Enterprise-grade pipeline (self-hosted) | On push (via webhook) |
| **Render / Railway** | Host the deployed application | After CI passes |
| **Semantic Versioning** | Structure releases predictably | On tag push |
