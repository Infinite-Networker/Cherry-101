<div align="center">

# 🍒 Contributing to Cherry-101

[![Created by Cherry Computer Ltd.](https://img.shields.io/badge/Created%20by-Cherry%20Computer%20Ltd.-dc143c?style=for-the-badge&labelColor=8b0000)](https://github.com/Infinite-Networker/Cherry-101)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-ff6b9d?style=for-the-badge&logo=github&logoColor=white&labelColor=2d2d2d)](https://github.com/Infinite-Networker/Cherry-101/issues)
[![CherryScript](https://img.shields.io/badge/Language-CherryScript-blueviolet?style=for-the-badge&labelColor=2d2d2d)](https://github.com/Infinite-Networker/CherryScript)

*Thank you for considering a contribution to Cherry-101 — the first program ever written in CherryScript, created by Cherry Computer Ltd. Every contribution, big or small, helps push this project — and the CherryScript language — forward.*

</div>

---

## 🌟 Ways to Contribute

```
┌─────────────────────────────────────────────────────────────────┐
│  How You Can Help Cherry-101 Grow                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   🐛  Report Bugs          — Open a GitHub Issue               │
│   💡  Suggest Features     — Start a Discussion                 │
│   🔧  Fix Issues           — Submit a Pull Request              │
│   📖  Improve Docs         — Edit markdown & examples           │
│   🧪  Write Tests          — Add to the test suite             │
│   🍒  Spread the Word      — Star the repo & share it!         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/Cherry-101.git
cd Cherry-101
```

### 2. Set Up Your Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install all dependencies
pip install -r requirements.txt
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-awesome-feature
# or
git checkout -b fix/the-bug-you-found
```

---

## 🔄 Development Workflow

```
  Fork Repo          Create Branch        Make Changes
  ─────────          ─────────────        ────────────
     │                    │                    │
     ▼                    ▼                    ▼
┌─────────┐          ┌─────────┐          ┌─────────┐
│ GitHub  │─────────▶│feature/ │─────────▶│  Code!  │
│  Fork   │          │ branch  │          │ & Test  │
└─────────┘          └─────────┘          └────┬────┘
                                               │
  PR Merged          Review & CI          Open PR
  ──────────         ───────────          ───────
     │                    │                    │
     ▼                    ▼                    ▼
┌─────────┐          ┌─────────┐          ┌─────────┐
│  Main   │◀─────────│ Review  │◀─────────│   PR    │
│ Branch  │          │  Pass   │          │ to main │
└─────────┘          └─────────┘          └─────────┘
```

---

## ✅ Commit Message Convention

We follow the **Conventional Commits** standard:

```
<type>(scope): <short description>

Types:
  feat     — A new feature
  fix      — A bug fix
  docs     — Documentation changes only
  style    — Formatting, no logic changes
  refactor — Code restructure, no feature/fix
  test     — Adding or updating tests
  chore    — Maintenance tasks

Examples:
  feat(interpreter): add support for nested function calls
  fix(parser): handle empty query results gracefully
  docs(readme): update installation instructions
  test(adapters): add unit tests for MySQL adapter
```

---

## 📋 Pull Request Checklist

Before submitting your PR, please confirm:

- [ ] My code follows the existing style and conventions
- [ ] I've added tests for any new functionality
- [ ] All existing tests pass (`python -m pytest tests/`)
- [ ] I've updated documentation if needed
- [ ] My commit messages follow the Conventional Commits format
- [ ] I've read the [Code of Conduct](./CODE_OF_CONDUCT.md)

---

## 🐛 Reporting Bugs

When filing a bug report, please include:

1. **A clear, descriptive title**
2. **Steps to reproduce** — exactly what you did
3. **Expected behaviour** — what you thought would happen
4. **Actual behaviour** — what actually happened
5. **Environment details** — OS, Python version, CherryScript version
6. **Relevant logs or error output**

---

## 💡 Suggesting Features

Have an idea for Cherry-101 or CherryScript? We want to hear it! Open a GitHub Discussion or Issue with:

1. **A clear description** of the feature
2. **The problem it solves** — what gap does it fill?
3. **Proposed implementation** *(optional but appreciated)*
4. **Alternatives considered**

---

## 📜 Code Style

- Python files follow **PEP 8**
- CherryScript files use **2-space indentation**
- All functions should have **docstrings**
- Keep lines under **100 characters**

---

<div align="center">

*Cherry-101 is a product of **Cherry Computer Ltd.** — we appreciate every contributor who helps make CherryScript the future of ML development.*

[![Created by Cherry Computer Ltd.](https://img.shields.io/badge/%F0%9F%8D%92%20Created%20by-Cherry%20Computer%20Ltd.-dc143c?style=for-the-badge&labelColor=1a0000)](https://github.com/Infinite-Networker/Cherry-101)

</div>
