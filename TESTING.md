
# 🧪 Testing Guide for SIR Epidemic Simulator

This document explains how to run the test suite and what each test verifies.

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Test Structure](#test-structure)
- [Test Coverage](#test-coverage)
  - [SEIR Model Tests](#seir-model-tests)
  - [Network Model Tests](#network-model-tests)
  - [Parameter Optimization Tests](#parameter-optimization-tests)
  - [Scenario Comparison Tests](#scenario-comparison-tests)
  - [ML Prediction Tests](#ml-prediction-tests)
- [Adding New Tests](#adding-new-tests)

---

## 🚀 Quick Start

Run all tests with a single command:

```bash
python run_all_tests.py
```

Expected output:
```
Ran 35 tests in X.XXs
OK (skipped=2)
```

### Run individual test files:

```bash
python tests/test_seir.py
python tests/test_network.py
python tests/test_optimization.py
python tests/test_ml.py
python tests/test_scenarios.py
```

---

## 📁 Test Structure

```
tests/
├── test_seir.py          # SEIR model mathematical correctness
├── test_network.py       # Social network spread simulation
├── test_optimization.py  # Parameter fitting algorithms
├── test_ml.py            # Machine learning predictions
└── test_scenarios.py     # Intervention strategy comparison

run_all_tests.py          # Master test runner
```

---

## 📊 Test Coverage

### 🦠 SEIR Model Tests (7 tests)

| Test | Description |
|:---|:---|
| `test_run_seir_infected_peak_occurs` | Verifies infected count reaches a peak then decreases |
| `test_run_seir_simulation_has_required_columns` | Checks output has `time, Susceptible, Exposed, Infected, Recovered` columns |
| `test_run_seir_simulation_non_empty` | Ensures simulation returns data |
| `test_run_seir_simulation_returns_dataframe` | Verifies output is a pandas DataFrame |
| `test_run_seir_total_population_conserved` | Confirms S+E+I+R remains constant over time |
| `test_run_seir_with_different_beta_values` | Tests that higher beta causes higher peak |
| `test_run_seir_with_zero_initial_infected` | Verifies no outbreak when I0 = 0 |

### 🌐 Network Model Tests (10 tests)

| Test | Description |
|:---|:---|
| `test_different_network_types_initializable` | Tests scale_free, small_world, random networks |
| `test_network_simulation_eventually_recovers` | Verifies all nodes eventually recover (I=0) |
| `test_network_simulation_infected_increases_initially` | Checks infected count rises in early steps |
| `test_network_simulation_respects_max_steps` | Ensures simulation stops at max_steps |
| `test_network_simulation_with_high_recovery` | Tests high recovery rate ends outbreak quickly |
| `test_network_simulation_zero_transmission` | Verifies only initial 5 infected when transmission=0 |
| `test_network_stats_returns_dict` | Checks network statistics return proper dictionary |
| `test_social_network_simulator_has_required_columns` | Verifies output has `step, susceptible, infected, recovered` |
| `test_social_network_simulator_initialization` | Tests simulator creates graph correctly |
| `test_social_network_simulator_returns_dataframe` | Verifies output is a pandas DataFrame |

### 📈 Parameter Optimization Tests (6 tests)

| Test | Description |
|:---|:---|
| `test_R0_positive` | Verifies calculated R0 is positive |
| `test_fit_returns_expected_keys` | Checks output contains `beta, gamma, R0, r_squared` |
| `test_fit_returns_numeric_values` | Ensures beta and gamma are numeric values |
| `test_optimizer_initialization_seir` | Tests SEIR optimizer initializes correctly |
| `test_optimizer_initialization_sir` | Tests SIR optimizer initializes correctly |
| `test_r_squared_between_0_and_1` | Verifies R² score is between 0 and 1 |

### 🎯 Scenario Comparison Tests (8 tests)

| Test | Description |
|:---|:---|
| `test_comparator_initialization` | Tests ScenarioComparator initializes correctly |
| `test_compare_all_scenarios_has_expected_keys` | Verifies scenarios: Baseline, Quarantine, Vaccination, Combined |
| `test_compare_all_scenarios_returns_tuple` | Checks output is (scenarios_dict, metrics_df) |
| `test_metrics_dataframe_has_required_columns` | Verifies metrics has `scenario, peak_infected, peak_day, reduction` |
| `test_metrics_has_four_scenarios` | Ensures exactly 4 scenarios are compared |
| `test_quarantine_reduces_peak_infected` | Confirms quarantine reduces peak infections |
| `test_scenario_dataframe_has_required_columns` | Checks each scenario has `day, susceptible, infected, recovered` |
| `test_vaccination_reduces_peak_infected` | Confirms vaccination reduces peak infections |

### 🤖 ML Prediction Tests (4 tests - 2 active, 2 skipped by default)

| Test | Status | Description |
|:---|:---|:---|
| `test_predictor_initialization_random_forest` | ✅ Active | Tests Random Forest predictor creation |
| `test_predictor_initialization_xgboost` | ✅ Active | Tests XGBoost predictor creation |
| `test_train_returns_metrics_with_proper_data` | ⏭️ Skipped | Needs real epidemiological data |
| `test_predict_future_returns_series_with_proper_data` | ⏭️ Skipped | Needs real epidemiological data |

> **Note:** ML tests are skipped by default because they require real outbreak data. To run them, provide a CSV file with 'day' and 'cases' columns.

---

## ✅ Test Summary

```
Total Tests: 35
Active Tests: 33 (2 skipped by design)
Pass Rate: 100% (when run with default settings)
```

### What gets tested:
- ✅ Mathematical correctness of ODE models
- ✅ Population conservation (mass balance)
- ✅ Parameter bounds and constraints
- ✅ Edge cases (zero transmission, zero initial infected)
- ✅ Network graph generation and simulation
- ✅ Intervention strategy effectiveness
- ✅ Data structure integrity (DataFrame columns, types)

---

## 🛠 Adding New Tests

To add a new test:

1. Locate the appropriate file in `tests/`
2. Add a method starting with `test_`
3. Use `self.assertXXX()` for assertions
4. Run `python run_all_tests.py` to verify

Example:
```python
def test_my_new_feature(self):
    result = my_function()
    self.assertEqual(result, expected_value)
```

---

## 📝 Requirements for Testing

All dependencies are in `requirements_full.txt`:
- `unittest` (built-in)
- `pandas`
- `numpy`
- `scipy`
- `networkx`

Install with:
```bash
pip install -r requirements_full.txt
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|:---|:---|
| `ModuleNotFoundError` | Run tests from project root directory |
| `ImportError` | Check that all dependencies are installed |
| Tests take too long | Reduce `t_max` or `steps` in test parameters |
| ML tests fail | They are intentionally skipped - ignore |

---

**All tests pass? Your model is mathematically sound!** 🎉

