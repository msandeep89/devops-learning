# Learning Progress Tracker

Daily log of what has been implemented and what is remaining.
Update the status and log section each day you work on a module.

---

## Module Status

| Module | Topic | Status | Started | Completed |
|--------|-------|--------|---------|-----------|
| 01 | Git & GitHub Fundamentals | ✅ Done | 2026-07-01 | 2026-07-01 |
| 02 | GitHub Actions | 🔲 Not started | — | — |
| 03 | SonarQube / SonarCloud | 🔲 Not started | — | — |
| 04 | Jenkins | 🔲 Not started | — | — |
| 05 | CI/CD Automation | 🔲 Not started | — | — |
| 06 | Release Management | 🔲 Not started | — | — |

**Overall progress: 1 / 6 modules complete**

---

## What is Implemented

### ✅ Module 01 — Git & GitHub Fundamentals
- [x] Theory: branching strategies (Git Flow vs trunk-based)
- [x] Theory: pull requests and code reviews
- [x] Theory: merge conflict resolution
- [x] Theory: semantic versioning and tagging
- [x] Theory: useful Git commands (stash, rebase, cherry-pick, bisect)
- [x] Mini-project: Python calculator (`add`, `subtract`, `multiply`, `divide`)
- [x] Unit tests: 15 tests with pytest covering all operations and edge cases
- [x] README: purpose, implementation details, how to run

---

## What is Remaining

### 🔲 Module 02 — GitHub Actions
- [ ] CI workflow: lint with flake8 on every PR
- [ ] CI workflow: run pytest on every PR
- [ ] Matrix build: test across Python 3.10, 3.11, 3.12
- [ ] Dependency caching for faster runs
- [ ] README: theory + step-by-step guide

### 🔲 Module 03 — SonarQube / SonarCloud
- [ ] SonarCloud account setup
- [ ] `sonar-project.properties` config file
- [ ] Integrate SonarCloud scan into GitHub Actions pipeline
- [ ] Coverage report upload
- [ ] Quality gate (block PR if gate fails)
- [ ] README badge

### 🔲 Module 04 — Jenkins
- [ ] Local Jenkins via Docker (`docker-compose.yml`)
- [ ] `Jenkinsfile` with declarative pipeline stages
- [ ] Replicate lint + test pipeline from Module 02
- [ ] Jenkins credentials management
- [ ] README: setup guide

### 🔲 Module 05 — CI/CD Automation
- [ ] Flask web app (simple to-do or API)
- [ ] Multi-stage pipeline: build → test → deploy
- [ ] Deploy to Render or Railway (free tier)
- [ ] Environment promotion (dev → staging → prod)
- [ ] Rollback strategy
- [ ] README: end-to-end flow

### 🔲 Module 06 — Release Management
- [ ] Conventional commits setup (`.commitlintrc`)
- [ ] Semantic versioning with Git tags
- [ ] GitHub Actions release workflow (trigger on tag push)
- [ ] Auto-generated changelog from commit messages
- [ ] GitHub Release with artifacts
- [ ] README: versioning rules and workflow

---

## Daily Log

### 2026-07-01
- Initialized the project and pushed to GitHub
- Created high-level and low-level design diagrams (Mermaid)
- Completed Module 01: Git & GitHub Fundamentals
  - Python calculator with 4 operations
  - 15 unit tests (all passing)
  - Full README with purpose and implementation details
- Set up daily progress reminder via GitHub Actions

---

> **Tip:** Each time you finish a task above, check it off `[x]` and add an entry to the Daily Log.
> Commit the update with: `git commit -m "docs: update progress for YYYY-MM-DD"`
