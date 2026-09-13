# Python Pytest CI/CD Template

A production-ready boilerplate for Python projects featuring an automated **CI/CD pipeline** with **Pytest**, **Code Coverage**, and **Linting** integrations.

## 🚀 Key Features

*   **Automated Testing**: Runs unit tests automatically via `pytest` on every push and pull request.
*   **Multi-Version Matrix**: Tests code compatibility against Python versions `3.10`, `3.11`, and `3.12`.
*   **Linting & Style Checks**: Automatically audits code quality using `flake8`.
*   **Coverage Reporting**: Tracks line coverage via `pytest-cov` and outputs performance directly to workflow logs.
*   **Artifact Retention**: Saves test results (`.xml` format) as downloadable pipeline artifacts.

---

## 📁 Repository Blueprint

```text
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions pipeline workflow
├── src/
│   └── calculator.py       # Core application code
├── tests/
│   └── test_calculator.py  # Pytest test suites
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Testing & development dependencies
└── README.md               # Repository documentation
```

---

## 🛠️ Local Development & Setup

Follow these quick steps to set up and run tests locally before pushing to the repository.

### 1. Set Up Environment
```bash
# Clone the repository
git clone https://github.com
cd YOUR-REPO-NAME

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Run Tests and Quality Audits
```bash
# Execute unit tests with a coverage breakdown
pytest --cov=src --cov-report=term-missing

# Run code style checking
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

---

## 🤖 CI/CD Pipeline Workflow

The workflow file `.github/workflows/ci-cd.yml` handles automated validation:

1.  **Triggers**: Fires on every `push` to branches `main` or `develop`, and on any open `pull_request` targeting `main`.
2.  **Environment Setup**: Spins up fresh Ubuntu runners across specified Python matrices.
3.  **Caching**: Caches `pip` packages to cut consecutive workflow runtime in half.
4.  **Enforcement**: Pipeline fails early if `flake8` encounters syntax errors or if any `pytest` assertions fail.
