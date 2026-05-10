
# 🤝 Contributing to SIR Epidemic Simulator

First off, thank you for considering contributing to this project! 🎉

This document provides guidelines and instructions for contributing to the SIR Epidemic Simulator. Following these guidelines helps maintain the quality and consistency of the project.

---

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Improving Documentation](#improving-documentation)
  - [Writing Code](#writing-code)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic understanding of:
  - Python programming
  - Git workflows
  - Unit testing (unittest)

### Fork & Clone
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/sir_simulator.git
   cd sir_simulator
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/miladrezanezhad/sir_simulator.git
   ```

---

## 💡 How Can I Contribute?

### 🐛 Reporting Bugs

**Before submitting a bug report:**
- Check if the bug has already been reported in [Issues](https://github.com/miladrezanezhad/sir_simulator/issues)
- Check if it's already fixed in the latest version

**When submitting a bug report, include:**
- Clear, descriptive title
- Steps to reproduce the bug
- Expected behavior vs actual behavior
- Screenshots if applicable
- Environment details (OS, Python version, package versions)

**Template:**
```markdown
## Bug Description
[Clear description of the bug]

## Steps to Reproduce
1. Run `python ...`
2. Execute `...`
3. See error

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Python Version: [e.g., 3.10]
- Package Versions: [from pip freeze]

## Additional Context
[Screenshots, logs, etc.]
```

### 💎 Suggesting Features

**Before suggesting a feature:**
- Check existing [Issues](https://github.com/miladrezanezhad/sir_simulator/issues) for similar suggestions
- Consider if the feature aligns with the project's scope

**When suggesting a feature, include:**
- Clear, descriptive title
- Detailed description of the feature
- Use case / problem it solves
- Any alternative solutions you've considered

### 📖 Improving Documentation

Documentation improvements are always welcome! This includes:
- Fixing typos or grammar
- Clarifying unclear sections
- Adding examples or use cases
- Translating documentation (if applicable)

### 💻 Writing Code

**Good first issues:** Look for labels like `good-first-issue` or `help-wanted` in the Issues section.

**Types of contributions:**
- Bug fixes
- New features
- Performance improvements
- Test coverage improvements
- Security enhancements

---

## 🔧 Development Setup

### 1. Create a virtual environment
```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements_full.txt
```

### 3. Install development dependencies
```bash
pip install pytest pytest-cov black flake8 mypy pre-commit
```

### 4. Run tests to verify setup
```bash
python run_all_tests.py
python -m unittest discover tests/security
```

### 5. Install pre-commit hooks (optional but recommended)
```bash
pre-commit install
```

---

## 📝 Coding Guidelines

### Python Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use 4 spaces for indentation (not tabs)
- Maximum line length: 88 characters (Black default)
- Use descriptive variable names

### Type Hints
Always include type hints for function definitions:
```python
def run_sir_simulation(
    beta: float,
    gamma: float,
    S0: int,
    I0: int,
    R0: int,
    t_max: int,
    steps: int = 500
) -> pd.DataFrame:
    """Run SIR simulation and return DataFrame."""
    pass
```

### Docstrings
Use Google-style docstrings:
```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param1 is empty

    Examples:
        >>> function_name("test", 42)
        True
    """
    pass
```

### Imports Order
1. Standard library imports
2. Third-party imports
3. Local application imports
4. Add blank line between groups

```python
import json
import os
from typing import List, Optional

import numpy as np
import pandas as pd

from core_models.sir_model import run_sir_simulation
```

---

## 🧪 Testing Guidelines

### When to Write Tests
- ✅ All new features must include tests
- ✅ Bug fixes should include regression tests
- ✅ Refactoring shouldn't break existing tests

### Test Structure
Each test should follow the **AAA pattern**:
```python
def test_something():
    # Arrange - Set up test data
    input_data = create_test_data()

    # Act - Execute the code being tested
    result = function_to_test(input_data)

    # Assert - Verify the result
    self.assertEqual(result, expected)
```

### Test Naming
```python
# Good - describes behavior
test_run_seir_returns_dataframe()
test_calculates_peak_infected_correctly()

# Bad - vague
test_seir()
test_function()
```

### Run Tests Before Committing
```bash
# Run all tests
python run_all_tests.py

# Run specific test file
python tests/test_seir.py

# Run security tests
python -m unittest discover tests/security
```

---

## 📝 Commit Guidelines

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
| Type | Description |
|:---|:---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes (formatting, missing semicolons, etc.) |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks (dependencies, configs, etc.) |
| `security` | Security-related changes |

### Examples
```bash
feat(network): add small-world network generator

fix(optimization): handle edge case when beta is zero

docs(readme): update installation instructions

test(seir): add population conservation test

security(xss): add input sanitization for streamlit dashboard
```

### Keep Commits
- **Atomic**: One commit per logical change
- **Descriptive**: Clear subject line (max 50 chars)
- **Complete**: Tests pass, code works

---

## 🔄 Pull Request Process

### Before Submitting
1. Update your fork with upstream/main
2. Run all tests locally
3. Ensure code follows style guidelines
4. Write/update tests for your changes
5. Update documentation if needed

### PR Template
When you submit a pull request, please fill out the template:

```markdown
## Description
[Describe what you changed and why]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Tests
- [ ] Other (please describe)

## Testing
- [ ] All existing tests pass
- [ ] New tests added for changes
- [ ] Manual testing performed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated

## Related Issues
Closes #[issue_number]

## Screenshots (if applicable)
[Add screenshots here]
```

### PR Workflow
1. Push changes to your fork
2. Create pull request from your branch to `main`
3. Wait for CI/CD checks to pass
4. Request review from maintainers
5. Address review feedback
6. Once approved, maintainer will merge

### After Your PR is Merged
- Delete your feature branch (if desired)
- Pull the latest changes to your local clone

---

## 🎨 Style Guide

### Naming Conventions
| Type | Convention | Example |
|:---|:---|:---|
| Variables | snake_case | `infected_count` |
| Functions | snake_case | `run_simulation()` |
| Classes | PascalCase | `SocialNetworkSimulator` |
| Constants | UPPER_SNAKE | `MAX_POPULATION` |
| Private members | _leading_underscore | `_internal_method()` |

### Code Organization
```python
# 1. Module docstring
"""Module description."""

# 2. Imports
import ...

# 3. Constants
MAX_ITERATIONS = 100

# 4. Classes
class MyClass:
    pass

# 5. Functions
def my_function():
    pass

# 6. Main guard
if __name__ == "__main__":
    pass
```

---

## ❓ Getting Help

- **Issues**: Check [existing issues](https://github.com/miladrezanezhad/sir_simulator/issues)
- **Discussions**: Open a [discussion](https://github.com/miladrezanezhad/sir_simulator/discussions)
- **Email**: [[miladvf2014@gmail.com](miladvf2014@gmail.com)]

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

---

**Thank you for contributing to make this project better!** 🙏

[⬆ Back to Top](#-contributing-to-sir-epidemic-simulator)
