import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from advanced_features.parameter_optimization import ParameterOptimizer, generate_synthetic_data

def test_optimizer():
    t, data, _ = generate_synthetic_data(0.5, 0.2, 1000, 10, 50, 5)
    optimizer = ParameterOptimizer('sir')
    results = optimizer.fit(data, t, [990, 10, 0])
    assert 0 < results['beta'] < 2
    assert 0 < results['gamma'] < 1
    print("✅ Optimization Test PASSED")
    return True

if __name__ == "__main__":
    success = test_optimizer()
    print(f"\nResult: {'PASSED' if success else 'FAILED'}")