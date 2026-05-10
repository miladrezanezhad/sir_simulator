import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from advanced_features.ml_prediction import EpidemicPredictor, generate_training_data

def test_ml():
    data = generate_training_data()
    predictor = EpidemicPredictor()
    result = predictor.train(data, test_size=0.2)
    
    if result is None:
        print("❌ ML Test FAILED")
        return False
    
    metrics, _, _ = result
    assert 'train_r2' in metrics
    print(f"✅ ML Test PASSED (R²={metrics['test_r2']:.3f})")
    return True

if __name__ == "__main__":
    success = test_ml()
    print(f"\nResult: {'PASSED' if success else 'FAILED'}")