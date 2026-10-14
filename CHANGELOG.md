# Changelog

All notable changes to the SIR Epidemic Simulator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Real-time data integration from WHO/CDC APIs
- Interactive parameter tuning with real-time graph updates
- Multi-language UI support

---

## [1.1.0] - 2026-10-15

### ✨ Added
- **SEIRD Model**: New compartmental model with mortality dynamics (`seird_model.py`), tracking Susceptible, Exposed, Infected, Recovered, and Deceased populations.
- **SIRS Model**: New model with waning immunity (`sirs_model.py`) supporting cyclical outbreaks and endemic steady-state analyses.
- **ML Prediction in Streamlit Dashboard**: Complete interactive UI for Random Forest and XGBoost time-series forecasting with performance metrics ($R^2$, RMSE) and forecast exports.
- **Streamlit Caching**: Added `@st.cache_data` decorators to eliminate redundant simulation recalculations.
- **Docker & Docker Compose**: Added containerization support with production-ready `Dockerfile` and `docker-compose.yml`.
- **New Unit & Security Tests**: Added `test_seird.py`, `test_sirs.py`, and `test_input_validation.py`.
- **Python 3.11 Support**: Re-enabled and verified Python 3.11 in GitHub Actions CI/CD workflows.

### 🐛 Fixed
- **Peak Day Calculation in UI**: Fixed calculation bug where row indices were reported instead of actual simulation time points.
- **SEIR Parameter Optimization in Streamlit**: Fixed bug where optimization was hardcoded to SIR and ignored user's SEIR selection.
- **CSV Upload Error Handling**: Resolved `UnboundLocalError` when optimizing parameters without an uploaded CSV file.
- **Data Leakage in ML Forecasting**: Switched from random shuffle `train_test_split` to sequential time-series splitting (`shuffle=False`).
- **Autoregressive Feature Loop**: Fixed frozen `day_of_week` and `week` features in `predict_future` autoregressive loop.
- **Optimization Parameter Boundary Check**: Bounds checking is now enforced prior to ODE solver execution to prevent invalid parameter crashes.
- **Division by Zero Protection**: Hardened ODE equations against $N \le 0$ edge cases.
- **CI/CD Dependency Path**: Fixed missing `requirements_full.txt` reference in GitHub Actions workflows.
- **README Alt Text Typo**: Corrected image alt text from "Web Security Scanner Pro" to "SIR Epidemic Simulator".

---

## [1.0.1] - 2026-05-10

### ✨ Added
- Comprehensive badges to README (PyPI downloads, GitHub stats, code style)
- Security test suite with 22 tests (DoS, memory exhaustion, Unicode attacks, XSS prevention)
- Project documentation files:
  - `CONTRIBUTING.md` - Guide for contributors
  - `CODE_OF_CONDUCT.md` - Community guidelines
  - `SECURITY.md` - Security policy and vulnerability reporting
  - `SECURITY_TESTS.md` - Security testing documentation
  - `TESTING.md` - Complete testing guide
  - `CHANGELOG.md` - Version history
- GitHub Issue templates:
  - Bug report template
  - Feature request template
  - Documentation improvement template
  - Performance issue template
- GitHub Pull Request template
- GitHub Actions workflows:
  - `test.yml` - Automated testing on push/PR
  - `security.yml` - Security scanning pipeline with Bandit, Safety, and TruffleHog
- Pre-commit configuration (`.pre-commit-config.yaml`) for code quality
- Coverage configuration (`.coveragerc`)
- `.gitattributes` for consistent line endings
- Emojis to CLI and Streamlit dashboard for better user experience

### 🔄 Changed
- Restructured project to `src/` layout for better packaging (PEP 621 compliant)
- Renamed PyPI package from `sir-epidemic-simulator-milad` to `sir-epidemic` (cleaner name)
- Improved README with:
  - Better documentation structure
  - More badges (downloads, stats, code style)
  - Clearer installation instructions
  - Comprehensive usage examples
- Updated Streamlit dashboard with emojis and better UI
- Updated CLI with emojis and better output formatting
- Upgraded `pyproject.toml` to use SPDX license expression (PEP 639 compliant)
- Removed invalid classifier `Topic :: Scientific/Engineering :: Medical Science Apps`

### 🐛 Fixed
- UnicodeEncodeError in Windows terminal when running tests
- Import issues after project restructuring
- Classifier validation error for PyPI upload (400 Bad Request)
- Module path resolution in `main.py`
- Coverage data collection issues

### 🔒 Security
- Added 22 security tests (all passing):
  - DoS attack prevention (5 tests)
  - Memory exhaustion protection (4 tests)
  - Unicode/UTF-8 attack mitigation (6 tests)
  - XSS prevention for Streamlit dashboard (7 tests)
- Added Bandit SAST scanning in CI/CD
- Added Safety dependency vulnerability scanning
- Added TruffleHog secret scanning
- All security tests pass with no known vulnerabilities

### 📦 Development
- Added `requirements_dev.txt` for development dependencies
- Added `Makefile` for common tasks (test, security, coverage, build, upload)
- Added pre-commit hooks for automated code formatting
- Added Black, isort, flake8, mypy configurations

---

## [1.0.0] - 2026-05-10

### 🎉 First Stable Release

### Added

#### Core Models
- SIR model implementation with ODE solver
- SEIR model with exposed compartment
- Population conservation verification
- Configurable simulation parameters (beta, gamma, sigma)

#### Network Simulation
- Scale-free network generator (Barabási–Albert)
- Small-world network generator (Watts–Strogatz)
- Random network generator (Erdos–Renyi)
- SIR spread simulation on social graphs
- Network statistics calculator (nodes, edges, avg degree, density)

#### Advanced Features
- Parameter optimization using differential evolution
- Curve fitting for real-world epidemic data
- Machine learning prediction with Random Forest
- Machine learning prediction with XGBoost
- Scenario comparison (Baseline, Quarantine, Vaccination, Combined)
- Intervention effectiveness metrics

#### User Interface
- Streamlit web dashboard (`app.py`)
- Command-line interface (`cli.py`)
- Interactive menu system (`main.py`)
- Real-time visualization of epidemic curves
- CSV export functionality

#### Testing
- 7 SEIR model unit tests
- 10 network simulation tests
- 6 parameter optimization tests
- 8 scenario comparison tests
- 2 active ML prediction tests
- Test coverage: 35 total unit tests, all passing

#### Documentation
- Complete README with installation and usage guide
- Basic project structure documentation

#### CI/CD
- Basic GitHub Actions for automated testing
- Python 3.8, 3.9, 3.10 test matrix

### Changed
- Initial release - no previous changes

### Fixed
- Initial release - no previous fixes

---

## [0.1.0] - 2026-05-01

### Added (Pre-release)
- Basic SIR model implementation
- Streamlit dashboard prototype
- Command-line interface
- Initial test structure

---

## 📝 Change Categories

| Type | Description |
|:---|:---|
| **Added** | New features, modules, or functionality |
| **Changed** | Changes to existing functionality |
| **Deprecated** | Features that will be removed in future |
| **Removed** | Features that have been removed |
| **Fixed** | Bug fixes |
| **Security** | Security-related changes |

---

## 🔖 Version History

| Version | Date | Status | Highlights |
|:---:|:---:|:---:|:---|
| **1.0.1** | 2026-05-10 | ✅ Stable | Security tests, documentation, restructuring |
| **1.0.0** | 2026-05-10 | ✅ Stable | First production release |
| 0.1.0 | 2026-05-01 | ⚠️ Pre-release | Initial prototype |

---

## 🚀 Roadmap (Future Versions)

### v1.1.0 (Planned)
- Real-world data import (CSV, Excel, JSON)
- More ML models (LSTM, GRU)
- Interactive parameter dashboard
- PDF report generation

### v1.2.0 (Planned)
- Age-structured models
- Geographic spread simulation
- Real-time data APIs
- Docker deployment

### v2.0.0 (Future)
- Agent-based modeling
- Parallel processing for large simulations
- Web API (RESTful)
- Database integration

---

## 🙏 Acknowledgments

This changelog format is adapted from [Keep a Changelog](https://keepachangelog.com/).

---

**For contributors:** When submitting a pull request, please update this file with your changes under the appropriate version and category.

[⬆ Back to Top](#changelog)
