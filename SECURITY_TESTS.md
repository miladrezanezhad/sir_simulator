# 🔒 Security Testing Guide for SIR Epidemic Simulator

This document explains the security test suite and how to run it.

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Security Test Categories](#security-test-categories)
  - [DoS Attack Tests](#dos-attack-tests)
  - [Memory Exhaustion Tests](#memory-exhaustion-tests)
  - [Unicode Attack Tests](#unicode-attack-tests)
  - [XSS Prevention Tests](#xss-prevention-tests)
- [Running Security Tests](#running-security-tests)
- [Interpreting Results](#interpreting-results)
- [Security Best Practices](#security-best-practices)

---

## 🚀 Quick Start

Run all security tests with a single command:

```bash
python -m unittest discover tests/security
```

Expected output:
```
Ran 22 tests in 0.400s
OK
```

---

## 🛡️ Security Test Categories

### 1. DoS Attack Tests (`test_dos_attack.py`)

Tests that the simulator can handle extreme inputs without crashing.

| Test | Description | What it verifies |
|:---|:---|:---|
| `test_extreme_time_steps` | 10,000 time units with 50,000 steps | No memory explosion |
| `test_extreme_population_size` | 10 million population | Handles large numbers |
| `test_network_with_too_many_nodes` | 5,000 node network | Graceful memory handling |
| `test_rapid_consecutive_calls` | 20 simulations in a row | No resource leaks |
| `test_extreme_parameter_values` | Invalid values (negative, None, inf) | No crash on bad input |

### 2. Memory Exhaustion Tests (`test_memory_exhaustion.py`)

Tests that memory usage stays within reasonable bounds.

| Test | Description | What it verifies |
|:---|:---|:---|
| `test_memory_usage_not_exploding` | 10 consecutive simulations | Memory growth < 5MB |
| `test_large_network_memory_bound` | 100 vs 500 node networks | Proportional memory use |
| `test_clear_data_between_simulations` | Sequential simulations | No memory doubling |
| `test_no_memory_leak_with_exceptions` | Invalid inputs trigger errors | Memory released after errors |

### 3. Unicode Attack Tests (`test_unicode_attacks.py`)

Tests that the simulator handles malicious Unicode/UTF-8 inputs safely.

| Test | Description | What it verifies |
|:---|:---|:---|
| `test_homoglyph_attack` | Visually similar Cyrillic characters | No command injection |
| `test_rtl_override_attack` | Right-to-left override characters | No hidden execution |
| `test_overflow_surrogate_pair` | Invalid Unicode surrogates | Graceful handling |
| `test_invalid_utf8_bytes` | Malformed UTF-8 sequences | Safe decode with replacement |
| `test_normalization_attack` | Different Unicode forms | No normalization bypass |
| `test_extremely_long_unicode` | 50,000 character string | No DoS from length |

### 4. XSS Prevention Tests (`test_xss_prevention.py`)

Tests that outputs are safe for web display (Streamlit dashboard).

| Test | Description | What it verifies |
|:---|:---|:---|
| `test_html_escaping_angles` | `<script>` tags | `<` and `>` become `&lt;` and `&gt;` |
| `test_html_escaping_quotes` | Event handler injection | Quotes become `&quot;` |
| `test_filename_safety_simple` | HTML tags in filenames | Tags removed from filenames |
| `test_json_output_safe_by_default` | XSS in JSON | JSON parsers handle safely |
| `test_dataframe_html_escaping` | DataFrame with malicious data | Escaped in safe column |
| `test_javascript_protocol_safety` | `javascript:` URLs | Protocol detection works |
| `test_cli_output_safety` | CLI printing | No XSS risk in terminal |

---

## 🏃‍♂️ Running Security Tests

### Run all security tests:
```bash
python -m unittest discover tests/security -v
```

### Run a specific test file:
```bash
python tests/security/test_dos_attack.py
python tests/security/test_memory_exhaustion.py
python tests/security/test_unicode_attacks.py
python tests/security/test_xss_prevention.py
```

### Run a specific test case:
```bash
python -m unittest tests.security.test_xss_prevention.TestXSSPrevention.test_html_escaping_angles
```

### Run with increased verbosity:
```bash
python -m unittest discover tests/security -v
```

---

## 📊 Interpreting Results

### ✅ All tests pass:
```
Ran 22 tests in 0.415s
OK
```
**Meaning:** Your simulator is secure against common attack vectors.

### ❌ Test failures:

| Error | Likely Cause | Fix |
|:---|:---|:---|
| `MemoryError` | Population too large | Reduce test population or add memory limits |
| `KeyError` | Wrong column name | Check DataFrame column names |
| `AssertionError` in XSS tests | Missing HTML escaping | Use `html.escape()` on user inputs |
| `ODEintWarning` | Extreme parameters | Expected warning, not a failure |

### ⚠️ About ODEintWarning:
```
ODEintWarning: Illegal input detected (internal error)
```
This warning appears during extreme parameter tests (e.g., negative beta). It's **expected and safe** - the tests catch and handle these exceptions.

---

## 🛡️ Security Best Practices for This Project

### For CLI inputs:
```python
# Always sanitize user inputs
import html
user_input = html.escape(input("Enter value: "))
```

### For filenames:
```python
import re
safe_name = re.sub(r'[<>"/\\|?*]', '_', unsafe_name)
```

### For JSON outputs:
```python
import json
# Standard json.dumps is safe
json_output = json.dumps({'data': user_input})
```

### For Streamlit dashboard:
```python
import streamlit as st
# Streamlit auto-escapes by default - this is safe
st.write(user_input)  # Safe!
# For raw HTML, use components.html() with caution
```

### For CSV exports:
```python
# Prefix formulas with quote to prevent execution
if user_input.startswith(('=', '+', '-', '@')):
    safe_input = "'" + user_input
```

---

## 🔄 Integration with CI/CD

Security tests run automatically on GitHub Actions:

```yaml
# In .github/workflows/security.yml
name: Security Scan Pipeline
on: [push, pull_request, schedule]
jobs:
  security-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run security tests
        run: python -m unittest discover tests/security
```

Badge for README:
```markdown
[![Security Tests](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/security.yml/badge.svg)](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/security.yml)
```

---

## 📝 Test Coverage Summary

```
┌─────────────────────────────┬──────────┬─────────┐
│ Category                    │ Tests    │ Status  │
├─────────────────────────────┼──────────┼─────────┤
│ DoS Attack                  │ 5        │ ✅      │
│ Memory Exhaustion           │ 4        │ ✅      │
│ Unicode Attacks             │ 6        │ ✅      │
│ XSS Prevention              │ 7        │ ✅      │
├─────────────────────────────┼──────────┼─────────┤
│ Total Security Tests        │ 22       │ ✅      │
└─────────────────────────────┴──────────┴─────────┘
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|:---|:---|
| `ModuleNotFoundError: No module named 'tests.security'` | Create `tests/security/__init__.py` (empty file) |
| Tests take too long | Reduce `max_steps` or `t_max` in test parameters |
| Memory error on large network | Your system may have less RAM; skip that test |
| UnicodeEncodeError on Windows | Set `PYTHONUTF8=1` environment variable |

---

**All security tests pass? Your simulator is production-ready!** 🔒
