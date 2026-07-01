# Module 01 — Git & GitHub Fundamentals

## What you will learn
- How branching strategies work (Git Flow vs trunk-based)
- How to open and review Pull Requests
- How to resolve merge conflicts
- Tagging releases with semantic versioning
- Useful everyday Git commands (stash, rebase, cherry-pick)

## Mini-project
A Python calculator app used to practice the full Git workflow —
feature branches → PR → review → merge → tag → release.

---

## Theory

### 1. Why Git?
Git tracks every change you make to code. If something breaks, you can go back
to any previous state. It also lets multiple developers work on the same codebase
without overwriting each other's work.

### 2. Branching Strategies

**Git Flow** — used in teams with scheduled releases
```
main        → stable production code only
develop     → integration branch (all features merge here first)
feature/*   → one branch per feature
hotfix/*    → emergency fix directly off main
release/*   → prep branch before merging to main
```

**Trunk-based development** — used by fast-moving teams (Google, Meta)
```
main        → everyone pushes here frequently (multiple times a day)
feature/*   → short-lived branches, merged within 1-2 days
```

> This project uses a simplified Git Flow.

### 3. The Pull Request (PR) Workflow
```
1. Create a branch        git checkout -b feature/add-division
2. Make changes           (edit files)
3. Stage changes          git add .
4. Commit                 git commit -m "feat: add division operation"
5. Push branch            git push origin feature/add-division
6. Open PR on GitHub      (compare & pull request button)
7. Review + approve       (teammate reviews, leaves comments)
8. Merge to main          (squash merge or merge commit)
9. Delete branch          git branch -d feature/add-division
```

### 4. Semantic Versioning
Format: `MAJOR.MINOR.PATCH` — e.g. `v1.3.2`

| Change type | Example | Version bump |
|-------------|---------|-------------|
| Breaking change | Removed a function | MAJOR: 1.0.0 → 2.0.0 |
| New feature (backward compatible) | Added division | MINOR: 1.0.0 → 1.1.0 |
| Bug fix | Fixed crash on divide by zero | PATCH: 1.0.0 → 1.0.1 |

### 5. Useful Git Commands

| Command | What it does |
|---------|-------------|
| `git stash` | Temporarily save uncommitted changes |
| `git stash pop` | Restore the stashed changes |
| `git log --oneline` | Compact commit history |
| `git diff main` | See what changed vs main |
| `git rebase main` | Replay your commits on top of latest main |
| `git cherry-pick <hash>` | Apply a single commit from another branch |
| `git bisect` | Binary search through history to find a bug |
| `git blame <file>` | See who last changed each line |

---

## Hands-on Walkthrough

### Step 1 — Clone the repo
```bash
git clone https://github.com/msandeep89/devops-learning.git
cd devops-learning
```

### Step 2 — Create a feature branch
```bash
git checkout -b feature/add-multiply
```

### Step 3 — Make a change
Open `module-01-git/calculator/calculator.py` and add a `multiply` function.

### Step 4 — Commit with a conventional commit message
```bash
git add module-01-git/calculator/calculator.py
git commit -m "feat: add multiply operation to calculator"
```

### Step 5 — Push and open a PR
```bash
git push origin feature/add-multiply
```
Then go to GitHub → open a Pull Request from `feature/add-multiply` → `main`.

### Step 6 — Simulate a merge conflict
```bash
# On main, edit the same line someone else edited
git checkout main
# Edit calculator.py line 1 comment
git commit -am "docs: update module description"

# Switch back to feature branch
git checkout feature/add-multiply
git rebase main   # conflict will appear here

# Resolve the conflict in your editor, then:
git add calculator.py
git rebase --continue
```

### Step 7 — Tag a release after merging
```bash
git checkout main
git pull
git tag -a v0.1.0 -m "Initial calculator release"
git push origin v0.1.0
```

---

## Project Structure
```
module-01-git/
├── README.md               ← you are here
└── calculator/
    ├── calculator.py       ← the app
    ├── requirements.txt    ← dependencies
    └── tests/
        └── test_calculator.py  ← unit tests
```
