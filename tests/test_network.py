import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core_models.network_model import SocialNetworkSimulator

def test_network_creation():
    sim = SocialNetworkSimulator(100)
    stats = sim.get_network_stats()
    assert stats['nodes'] == 100
    print("✅ Network Test 1 PASSED")
    return True

def test_simulation():
    sim = SocialNetworkSimulator(50)
    df = sim.simulate_spread(0.3, 0.1, 3, 30)
    assert len(df) > 0
    print("✅ Network Test 2 PASSED")
    return True

def test_spread():
    sim = SocialNetworkSimulator(100)
    df = sim.simulate_spread(0.5, 0.05, 5, 30)
    total_affected = df['infected'].iloc[-1] + df['recovered'].iloc[-1]
    assert total_affected > 5
    print("✅ Network Test 3 PASSED")
    return True

if __name__ == "__main__":
    tests = [test_network_creation, test_simulation, test_spread]
    results = [t() for t in tests]
    print(f"\nResults: {sum(results)}/3 passed")