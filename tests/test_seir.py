import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from core_models.seir_model import run_seir_simulation

def test_seir_basic():
    df = run_seir_simulation(0.5, 0.2, 0.1, 990, 0, 10, 0, 100, 100)
    assert len(df) > 0
    assert 'Exposed' in df.columns
    print("✅ SEIR Test 1 PASSED")
    return True

def test_exposed_exists():
    df = run_seir_simulation(0.5, 0.2, 0.1, 990, 0, 10, 0, 100, 100)
    assert df['Exposed'].max() > 0
    print("✅ SEIR Test 2 PASSED")
    return True

def test_conservation():
    df = run_seir_simulation(0.5, 0.2, 0.1, 990, 0, 10, 0, 100, 100)
    total = df['Susceptible'] + df['Exposed'] + df['Infected'] + df['Recovered']
    assert np.allclose(total, 1000, rtol=1e-6)
    print("✅ SEIR Test 3 PASSED")
    return True

if __name__ == "__main__":
    tests = [test_seir_basic, test_exposed_exists, test_conservation]
    results = [t() for t in tests]
    print(f"\nResults: {sum(results)}/3 passed")