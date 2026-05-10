# 🦠 SIR Epidemic Simulator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/test.yml/badge.svg)](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/test.yml)
[![Security](https://img.shields.io/badge/security-tests-brightgreen)](SECURITY_TESTS.md)
[![Tests Status](https://img.shields.io/badge/tests-57%20passing-brightgreen)](TESTING.md)
[![Streamlit](https://img.shields.io/badge/streamlit-app-red)](https://streamlit.io)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)]()

**A Complete Epidemic Modeling Suite with 5 Integrated Features**

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [Testing](#testing)
- [Security](#security)
- [Screenshots](#screenshots)
- [Documentation](#documentation)
- [License](#license)

---

## 🔭 Overview

The **SIR Epidemic Simulator** is a comprehensive epidemic modeling toolkit combining classical compartmental models with modern machine learning. It provides researchers, students, and public health professionals with tools to simulate, analyze, and predict epidemic dynamics.

### Key Capabilities

| Feature | Description |
|:---|:---|
| **SIR Model** | Basic Susceptible-Infected-Recovered dynamics |
| **SEIR Model** | Adds Exposed/incubation compartment |
| **Network Simulation** | Fake news spread on social graphs |
| **Parameter Optimization** | Fit models to real-world data |
| **ML Prediction** | Forecast future cases with XGBoost/Random Forest |
| **Scenario Comparison** | Evaluate quarantine vs vaccination |

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

```bash
# Clone repository
git clone https://github.com/miladrezanezhad/sir_simulator.git
cd sir_simulator

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import streamlit, numpy, pandas; print('✅ Success!')"
```

---

## 🎮 Quick Start

### Launch Web Dashboard (Recommended)
```bash
streamlit run user_interface/app.py
```

### Run CLI
```bash
python user_interface/cli.py --beta 0.5 --gamma 0.2 --tmax 100
```

### Run All Tests
```bash
python run_all_tests.py
```

### Interactive Menu
```bash
python main.py
```

---

## 📁 Project Structure

```
sir_simulator/
│
├── core_models/              # Core mathematical models
│   ├── sir_model.py          # Basic SIR implementation
│   ├── seir_model.py         # SEIR with exposed compartment
│   └── network_model.py      # Social network spread simulation
│
├── advanced_features/        # Advanced capabilities
│   ├── parameter_optimization.py  # Curve fitting
│   ├── ml_prediction.py           # ML forecasting
│   └── scenario_comparison.py     # Intervention analysis
│
├── user_interface/           # UI applications
│   ├── app.py                # Streamlit dashboard
│   └── cli.py                # Command-line interface
│
├── tests/                    # Test suite (57+ tests)
│   ├── test_seir.py          # SEIR model tests
│   ├── test_network.py       # Network simulation tests
│   ├── test_optimization.py  # Parameter optimization tests
│   ├── test_ml.py            # ML prediction tests
│   ├── test_scenarios.py     # Scenario comparison tests
│   └── security/             # Security test suite
│       ├── test_dos_attack.py
│       ├── test_memory_exhaustion.py
│       ├── test_unicode_attacks.py
│       └── test_xss_prevention.py
│
├── docs/                     # Documentation
│   └── notebook.ipynb        # Educational Jupyter notebook
│
├── screenshots/              # Application screenshots
│   ├── SIR Epidemic Model.png
│   ├── SEIR Model with Exposed Compartment.png
│   ├── Fake News Spread on Social Network.png
│   ├── Parameter Optimization.png
│   ├── Machine Learning Prediction.png
│   ├── Scenario Comparison.png
│   └── dashboard.png
│
├── .github/workflows/        # CI/CD pipelines
│   ├── test.yml              # Test automation
│   └── security.yml          # Security scan pipeline
│
├── config/                   # Configuration files
├── outputs/                  # CSV export folder
│
├── README.md                 # This file
├── TESTING.md                # Testing guide
├── SECURITY_TESTS.md         # Security testing guide
├── LICENSE                   # MIT License
├── requirements.txt     # Python dependencies
├── run_all_tests.py          # Master test runner
└── .gitignore
```

---

## 📊 Usage Guide

### 1. SIR Model
```python
from core_models.sir_model import run_sir_simulation

df = run_sir_simulation(
    beta=0.5, gamma=0.2,
    S0=990, I0=10, R0=0,
    t_max=100, steps=500
)
```

### 2. SEIR Model
```python
from core_models.seir_model import run_seir_simulation

df = run_seir_simulation(
    beta=0.5, sigma=0.2, gamma=0.1,
    S0=990, E0=0, I0=10, R0=0,
    t_max=100, steps=500
)
```

### 3. Network Simulation
```python
from core_models.network_model import SocialNetworkSimulator

sim = SocialNetworkSimulator(num_nodes=200, network_type='scale_free')
df = sim.simulate_spread(transmission_prob=0.4, recovery_prob=0.1)
```

### 4. Parameter Optimization
```python
from advanced_features.parameter_optimization import ParameterOptimizer

optimizer = ParameterOptimizer(model_type='sir')
results = optimizer.fit(observed_data, t, [990, 10, 0])
print(f"β={results['beta']:.3f}, γ={results['gamma']:.3f}, R0={results['R0']:.3f}")
```

### 5. ML Prediction
```python
from advanced_features.ml_prediction import EpidemicPredictor

predictor = EpidemicPredictor(model_type='random_forest')
metrics, predictions, _ = predictor.train(historical_data)
future = predictor.predict_future(historical_data, days=30)
```

### 6. Scenario Comparison
```python
from advanced_features.scenario_comparison import ScenarioComparator

comp = ScenarioComparator()
scenarios, metrics = comp.compare_all_scenarios(days=120)
print(metrics)
```

---

## 🧪 Testing

Run all tests (35 unit tests + 22 security tests):

```bash
python run_all_tests.py
python -m unittest discover tests/security
```

Or run individual test files:
```bash
python tests/test_seir.py
python tests/test_network.py
python tests/test_optimization.py
python tests/test_ml.py
python tests/test_scenarios.py
python tests/security/test_dos_attack.py
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

For detailed testing documentation, see:
- [Testing Guide](TESTING.md) - Complete testing documentation
- [Security Testing Guide](SECURITY_TESTS.md) - Security test suite documentation

---

## 🔒 Security

This project includes comprehensive security testing:
- ✅ DoS attack prevention
- ✅ Memory exhaustion protection
- ✅ Unicode/UTF-8 attack mitigation
- ✅ XSS prevention for Streamlit dashboard

All security tests pass with no vulnerabilities detected.

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

## 📚 Documentation

- [Testing Guide](TESTING.md) - How to run and understand tests
- [Security Testing Guide](SECURITY_TESTS.md) - Security test suite documentation
- [Jupyter Notebook](docs/notebook.ipynb) - Interactive educational notebook

---

## 🔧 Requirements

```
numpy>=1.21.0
scipy>=1.7.0
pandas>=1.3.0
matplotlib>=3.4.0
streamlit>=1.20.0
networkx>=2.8
scikit-learn>=1.0.0
xgboost>=1.6.0
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure all tests pass before submitting:
```bash
python run_all_tests.py
python -m unittest discover tests/security
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Classical SIR/SEIR models from Kermack-McKendrick theory
- Network science algorithms from NetworkX library
- Machine learning models from scikit-learn and XGBoost

---

**Built with ❤️ for epidemic modeling and public health research**

[⬆ Back to Top](#-sir-epidemic-simulator)
