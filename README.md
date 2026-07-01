# DevOps Learning Project

A hands-on learning project covering CI/CD tools and practices used in real-world software engineering.
Each module is self-contained with theory, working code, and a mini-project.

---

## Architecture & Design

Before diving into code, understand how everything connects:

- [High Level Design](docs/high-level-design.md) — how all 6 modules form one end-to-end DevOps pipeline
- [Low Level Design](docs/low-level-design.md) — detailed flow diagram for each module

---

## Learning Plan

### Module 01 — Git & GitHub Fundamentals
**Goal:** Understand version control beyond basic commits.

Topics:
- Branching strategies (Git Flow, trunk-based)
- Pull requests and code reviews
- Resolving merge conflicts
- `.gitignore`, tagging, stashing

Mini-project: A simple Python calculator with a proper Git workflow (feature branches, PRs, tags).

---

### Module 02 — GitHub Actions (CI/CD on GitHub)
**Goal:** Automate testing, linting, and builds on every push.

Topics:
- Workflow syntax (triggers, jobs, steps, runners)
- Running tests automatically on pull requests
- Using secrets and environment variables
- Caching dependencies for faster runs
- Matrix builds (test on multiple Python versions)

Mini-project: Python app with automated lint (`flake8`) + test (`pytest`) pipeline that runs on every PR.

---

### Module 03 — SonarQube / SonarCloud (Code Quality)
**Goal:** Detect bugs, vulnerabilities, and code smells automatically.

Topics:
- What static analysis is and why it matters
- Setting up SonarCloud (free for public repos)
- Quality gates — pass/fail criteria
- Reading SonarQube reports (coverage, duplications, smells)
- Adding a quality badge to README

Mini-project: Integrate SonarCloud into the Module 02 GitHub Actions pipeline. Block merges if quality gate fails.

---

### Module 04 — Jenkins (Self-hosted CI/CD)
**Goal:** Understand Jenkins, the most widely used CI/CD tool in enterprises.

Topics:
- Running Jenkins locally with Docker
- Creating a `Jenkinsfile` (declarative pipeline)
- Jenkins agents and executors
- Managing credentials in Jenkins
- Replicating a GitHub Actions pipeline in Jenkins

Mini-project: A `Jenkinsfile` that builds, tests, and reports quality for the same Python app — running on a local Jenkins instance via Docker.

---

### Module 05 — CI/CD Automation (End-to-End Pipeline)
**Goal:** Build a complete automated pipeline from code push to deployment.

Topics:
- What CI vs CD vs CD means (Continuous Integration / Delivery / Deployment)
- Pipeline stages: Build → Test → Quality → Deploy
- Deploying a Python app to a free cloud host (Render / Railway)
- Environment promotion (dev → staging → prod)
- Rollback strategies

Mini-project: A full CI/CD pipeline for a Flask web app — push to main triggers automated deploy to a live URL.

---

### Module 06 — Release Management
**Goal:** Version, package, and release software in a structured way.

Topics:
- Semantic versioning (SemVer: `v1.0.0`, `v1.2.3`)
- Git tags and GitHub Releases
- Auto-generating changelogs from commit messages
- Conventional commits standard
- Automating releases with GitHub Actions

Mini-project: Add automated versioning and release creation to the Flask app — pushing a tag triggers a GitHub Release with changelog.

---

## Progress Tracker

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Git & GitHub Fundamentals | 🔲 Not started |
| 02 | GitHub Actions | 🔲 Not started |
| 03 | SonarQube / SonarCloud | 🔲 Not started |
| 04 | Jenkins | 🔲 Not started |
| 05 | CI/CD Automation | 🔲 Not started |
| 06 | Release Management | 🔲 Not started |

---

## How to use this repo

Each module lives in its own folder (`module-01-git/`, `module-02-github-actions/`, etc.)
with its own `README.md` explaining the theory and step-by-step instructions.

Work through them in order — each module builds on the previous one.
