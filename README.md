# 🦠 SIR Epidemic Simulator

[![PyPI version](https://badge.fury.io/py/sir-epidemic.svg)](https://pypi.org/project/sir-epidemic/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sir-epidemic)](https://pypi.org/project/sir-epidemic/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/test.yml/badge.svg)](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/test.yml)
[![Security](https://img.shields.io/badge/security-tests-brightgreen)](SECURITY_TESTS.md)
[![Code Coverage](https://img.shields.io/badge/coverage-51%25-orange)](coverage_html_report/index.html)
[![GitHub stars](https://img.shields.io/github/stars/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/network)
[![GitHub issues](https://img.shields.io/github/issues/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/commits/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Streamlit](https://img.shields.io/badge/streamlit-app-red)](https://streamlit.io)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)]()

**A Complete Epidemic Modeling Suite with 6 Integrated Features**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Documentation](#-documentation)
- [Project Structure](#-project-structure)
- [Usage Guide](#-usage-guide)
- [Testing](#-testing)
- [Security](#-security)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)


---

<div dir="ltr" align="center">
  <br>
  <strong style="font-size: 1.2rem;">🌐 Languages / زبان‌ها:</strong>
  <br><br>
  <strong style="font-size: 1.1rem;">
    <a href="README.md" style="text-decoration: none;">🇬🇧 English (انگلیسی)</a> &nbsp;|&nbsp;
    <a href="README.fa.md" style="text-decoration: none;">🇮🇷 فارسی (Persian)</a>
  </strong>
  <br><br>
</div>

---

## 🔭 Overview

The **SIR Epidemic Simulator** is a comprehensive epidemic modeling toolkit combining classical compartmental models with modern machine learning. It provides researchers, students, and public health professionals with tools to simulate, analyze, and predict epidemic dynamics.

| Capability | Description |
|:---|:---|
| 📈 **SIR Model** | Basic Susceptible-Infected-Recovered dynamics |
| 🧬 **SEIR Model** | Adds Exposed/incubation compartment |
| 🌐 **Network Simulation** | Fake news spread on social graphs |
| 🎯 **Parameter Optimization** | Fit models to real-world data |
| 🤖 **ML Prediction** | Forecast future cases with XGBoost/Random Forest |
| ⚖️ **Scenario Comparison** | Evaluate quarantine vs vaccination |

---

## ✨ Features

### Core Models
- ✅ SIR model with ODE solver
- ✅ SEIR model with exposed compartment
- ✅ Population conservation verification
- ✅ Configurable simulation parameters

### Network Simulation
- ✅ Scale-free network (Barabási-Albert)
- ✅ Small-world network (Watts-Strogatz)
- ✅ Random network (Erdos-Renyi)
- ✅ SIR spread simulation on social graphs
- ✅ Network statistics calculator

### Advanced Features
- ✅ Parameter optimization using differential evolution
- ✅ Curve fitting for real-world epidemic data
- ✅ ML prediction with Random Forest & XGBoost
- ✅ Scenario comparison (Baseline, Quarantine, Vaccination, Combined)

### User Interface
- ✅ Streamlit web dashboard
- ✅ Command-line interface (CLI)
- ✅ Interactive menu system
- ✅ CSV export functionality

### Testing & Security
- ✅ 35+ unit tests
- ✅ 22 security tests (DoS, Memory, Unicode, XSS)
- ✅ GitHub Actions CI/CD
- ✅ Pre-commit hooks for code quality

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install from PyPI (Recommended)

```bash
pip install sir-epidemic
```

### Install from Source (for development)

```bash
git clone https://github.com/miladrezanezhad/sir_simulator.git
cd sir_simulator
pip install -e .
```

### Verify Installation

```bash
python -c "import sir_simulator; print('✅ Success!')"
```

---

## 🎮 Quick Start

### 1️⃣ Launch Streamlit Dashboard (Recommended)

```bash
streamlit run src/sir_simulator/user_interface/app.py
```

Then open http://localhost:8501 in your browser.

### 2️⃣ Run CLI

```bash
sir-simulator --beta 0.5 --gamma 0.2 --tmax 100
```

### 3️⃣ Run Interactive Menu

```bash
python main.py
```

### 4️⃣ Run All Tests

```bash
python run_all_tests.py
python -m unittest discover tests/security
```

---

## 📚 Documentation

### Complete Wiki

For detailed tutorials, API reference, and FAQs, visit our [GitHub Wiki](https://github.com/miladrezanezhad/sir_simulator/wiki):

| Wiki Page | Description |
|:---|:---|
| [🏠 Home](https://github.com/miladrezanezhad/sir_simulator/wiki) | Wiki home page |
| [🚀 Getting Started](https://github.com/miladrezanezhad/sir_simulator/wiki/Getting-Started) | Installation and first steps |
| [📈 SIR Model Tutorial](https://github.com/miladrezanezhad/sir_simulator/wiki/SIR-Model-Tutorial) | Complete SIR model guide |
| [🧬 SEIR Model Tutorial](https://github.com/miladrezanezhad/sir_simulator/wiki/SEIR-Model-Tutorial) | Complete SEIR model guide |
| [🌐 Network Simulation Tutorial](https://github.com/miladrezanezhad/sir_simulator/wiki/Network-Simulation-Tutorial) | Social network spread guide |
| [🤖 ML Prediction Tutorial](https://github.com/miladrezanezhad/sir_simulator/wiki/ML-Prediction-Tutorial) | Machine learning forecasting |
| [⚖️ Scenario Comparison Tutorial](https://github.com/miladrezanezhad/sir_simulator/wiki/Scenario-Comparison-Tutorial) | Intervention strategies |
| [❓ FAQ](https://github.com/miladrezanezhad/sir_simulator/wiki/FAQ) | Frequently asked questions |
| [📚 API Reference](https://github.com/miladrezanezhad/sir_simulator/wiki/API-Reference) | Complete function documentation |
| [🤝 Contributing Guide](https://github.com/miladrezanezhad/sir_simulator/wiki/Contributing-Guide) | How to contribute |

### Local Documentation

| File | Description |
|:---|:---|
| [TESTING.md](TESTING.md) | Complete testing guide |
| [SECURITY_TESTS.md](SECURITY_TESTS.md) | Security testing documentation |
| [SECURITY.md](SECURITY.md) | Security policy |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contributing guidelines |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Code of conduct |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

---

## 📁 Project Structure

```
sir_simulator/
│
├── src/sir_simulator/          # Source code
│   ├── core_models/            # Core mathematical models
│   │   ├── sir_model.py        # Basic SIR implementation
│   │   ├── seir_model.py       # SEIR with exposed compartment
│   │   └── network_model.py    # Social network spread simulation
│   │
│   ├── advanced_features/      # Advanced capabilities
│   │   ├── parameter_optimization.py  # Curve fitting
│   │   ├── ml_prediction.py           # ML forecasting
│   │   └── scenario_comparison.py     # Intervention analysis
│   │
│   └── user_interface/         # UI applications
│       ├── app.py              # Streamlit dashboard
│       └── cli.py              # Command-line interface
│
├── tests/                      # Test suite (57+ tests)
│   ├── test_seir.py            # SEIR model tests
│   ├── test_network.py         # Network simulation tests
│   ├── test_optimization.py    # Parameter optimization tests
│   ├── test_ml.py              # ML prediction tests
│   ├── test_scenarios.py       # Scenario comparison tests
│   └── security/               # Security test suite
│       ├── test_dos_attack.py
│       ├── test_memory_exhaustion.py
│       ├── test_unicode_attacks.py
│       └── test_xss_prevention.py
│
├── docs/                       # Documentation
│   └── notebook.ipynb          # Educational Jupyter notebook
│
├── screenshots/                # Application screenshots (7 images)
│
├── .github/workflows/          # CI/CD pipelines
│   ├── test.yml                # Test automation
│   └── security.yml            # Security scan pipeline
│
├── README.md                   # This file
├── TESTING.md                  # Testing guide
├── SECURITY_TESTS.md           # Security testing guide
├── SECURITY.md                 # Security policy
├── CONTRIBUTING.md             # Contributing guide
├── CODE_OF_CONDUCT.md          # Code of conduct
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT License
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python dependencies
├── requirements_dev.txt        # Development dependencies
├── Makefile                    # Common tasks automation
├── main.py                     # Interactive menu
└── run_all_tests.py            # Master test runner
```

---

## 📊 Usage Guide

### 1. SIR Model

```python
from sir_simulator.core_models.sir_model import run_sir_simulation

df = run_sir_simulation(
    beta=0.5, gamma=0.2,
    S0=990, I0=10, R0=0,
    t_max=100, steps=500
)
```

### 2. SEIR Model

```python
from sir_simulator.core_models.seir_model import run_seir_simulation

df = run_seir_simulation(
    beta=0.5, sigma=0.2, gamma=0.1,
    S0=990, E0=5, I0=5, R0=0,
    t_max=100, steps=500
)
```

### 3. Network Simulation

```python
from sir_simulator.core_models.network_model import SocialNetworkSimulator

sim = SocialNetworkSimulator(num_nodes=200, network_type='scale_free')
df = sim.simulate_spread(transmission_prob=0.4, recovery_prob=0.1)
```

### 4. Parameter Optimization

```python
from sir_simulator.advanced_features.parameter_optimization import ParameterOptimizer

optimizer = ParameterOptimizer(model_type='sir')
results = optimizer.fit(observed_data, t, [990, 10, 0])
print(f"β={results['beta']:.3f}, γ={results['gamma']:.3f}, R0={results['R0']:.3f}")
```

### 5. ML Prediction

```python
from sir_simulator.advanced_features.ml_prediction import EpidemicPredictor

predictor = EpidemicPredictor(model_type='random_forest')
metrics, predictions, _ = predictor.train(historical_data)
future = predictor.predict_future(historical_data, days=30)
```

### 6. Scenario Comparison

```python
from sir_simulator.advanced_features.scenario_comparison import ScenarioComparator

comp = ScenarioComparator(beta=0.25, gamma=0.1)
scenarios, metrics = comp.compare_all_scenarios(days=120)
print(metrics)
```

---

## 🧪 Testing

### Run All Tests

```bash
python run_all_tests.py
python -m unittest discover tests/security
```

### Test Coverage

| Module | Tests | Status |
|:---|:---:|:---:|
| SEIR Model | 7 | ✅ |
| Network Model | 10 | ✅ |
| Parameter Optimization | 6 | ✅ |
| ML Prediction | 2 (active) + 2 (skip) | ✅ |
| Scenario Comparison | 8 | ✅ |
| Security (DoS, Memory, Unicode, XSS) | 22 | ✅ |
| **Total** | **57** | **✅ All Passing** |

### Run Individual Tests

```bash
python tests/test_seir.py
python tests/test_network.py
python tests/test_optimization.py
python tests/test_ml.py
python tests/test_scenarios.py
python tests/security/test_dos_attack.py
```

For detailed testing documentation, see [TESTING.md](TESTING.md).

---

## 🔒 Security

This project includes comprehensive security testing:

| Test Category | Tests | Status |
|:---|:---:|:---:|
| DoS Attack Prevention | 5 | ✅ |
| Memory Exhaustion Protection | 4 | ✅ |
| Unicode/UTF-8 Attack Mitigation | 6 | ✅ |
| XSS Prevention for Streamlit | 7 | ✅ |
| **Total** | **22** | **✅ All Passing** |

All security tests pass with no vulnerabilities detected.

For security issues, please see [SECURITY.md](SECURITY.md).

---

## 📸 Screenshots

| SIR Model | SEIR Model |
|:---:|:---:|
| ![SIR](screenshots/SIR%20Epidemic%20Model.png) | ![SEIR](screenshots/SEIR%20Model%20with%20Exposed%20Compartment.png) |

| Network Simulation | Parameter Optimization |
|:---:|:---:|
| ![Network](screenshots/Fake%20News%20Spread%20on%20Social%20Network.png) | ![Optimization](screenshots/Parameter%20Optimization.png) |

| ML Prediction | Scenario Comparison |
|:---:|:---:|
| ![ML](screenshots/Machine%20Learning%20Prediction.png) | ![Scenarios](screenshots/Scenario%20Comparison.png) |

### 📊 Streamlit Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Steps

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python run_all_tests.py`
5. Submit a Pull Request

### Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/sir_simulator.git
cd sir_simulator
pip install -e .
pip install -r requirements_dev.txt
pre-commit install
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Classical SIR/SEIR models from Kermack-McKendrick theory
- Network science algorithms from NetworkX library
- Machine learning models from scikit-learn and XGBoost
- Streamlit for the interactive dashboard framework

---

## 📞 Contact & Support

| Channel | Link |
|:---|:---|
| **GitHub Issues** | [Report bug](https://github.com/miladrezanezhad/sir_simulator/issues) |
| **GitHub Discussions** | [Ask questions](https://github.com/miladrezanezhad/sir_simulator/discussions) |
| **Email** | miladvf2014@gmail.com |
| **PyPI** | [sir-epidemic](https://pypi.org/project/sir-epidemic/) |

---

## ⭐ Star the Project

If you find this project useful, please consider **starring** it on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/miladrezanezhad/sir_simulator?style=social)](https://github.com/miladrezanezhad/sir_simulator/stargazers)

---

**Built with ❤️ for epidemic modeling and public health research**

[⬆ Back to Top](#-sir-epidemic-simulator)
