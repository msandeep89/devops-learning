# Calculator — Module 01 Mini Project

## Purpose
This is the hands-on project for **Module 01: Git & GitHub Fundamentals**.

The calculator itself is intentionally simple — the real learning here is not the code,
but how the code is managed using Git. Every feature, fix, and improvement is practiced
through proper Git workflows: feature branches, pull requests, code reviews, conflict
resolution, and versioned releases.

---

## What is Implemented

### Operations
| Operation | Function | Example |
|-----------|----------|---------|
| Addition | `add(a, b)` | `add(2, 3)` → `5` |
| Subtraction | `subtract(a, b)` | `subtract(10, 4)` → `6` |
| Multiplication | `multiply(a, b)` | `multiply(3, 4)` → `12` |
| Division | `divide(a, b)` | `divide(10, 2)` → `5.0` |

Division raises a `ValueError` if the divisor is zero.

### Tests
15 unit tests written with `pytest`, covering:
- Positive and negative numbers
- Float inputs and results
- Edge cases (multiply by zero, divide by zero)

### Project Structure
```
calculator/
├── calculator.py        ← core logic (4 operations)
├── requirements.txt     ← pytest, pytest-cov
├── README.md            ← you are here
└── tests/
    └── test_calculator.py  ← 15 unit tests
```

---

## How to Run

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Run the calculator interactively**
```bash
python calculator.py
```

**Run the tests**
```bash
pytest tests/ -v
```

**Run tests with coverage report**
```bash
pytest tests/ --cov=calculator --cov-report=term-missing
```

---

## Git Workflow Practiced in This Module

```
main
 └── feature/add-multiply     ← new feature branch
 └── feature/add-division     ← another feature branch
 └── hotfix/divide-by-zero    ← bug fix branch
```

Each feature was developed on its own branch, reviewed via a Pull Request,
and merged into `main` following the Git Flow strategy.

Releases are tagged using semantic versioning:
- `v0.1.0` — initial calculator with add and subtract
- `v0.2.0` — added multiply and divide
- `v0.2.1` — fixed divide by zero crash
