import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from advanced_features.scenario_comparison import ScenarioComparator

def test_scenarios():
    comp = ScenarioComparator()
    
    baseline = comp.baseline_scenario(100)
    quarantine = comp.quarantine_scenario(100)
    vaccination = comp.vaccination_scenario(100)
    
    baseline_peak = baseline['infected'].max()
    quarantine_peak = quarantine['infected'].max()
    vax_peak = vaccination['infected'].max()
    
    if quarantine_peak < baseline_peak and vax_peak < baseline_peak:
        print("✅ Scenario Test PASSED")
        return True
    else:
        print("❌ Scenario Test FAILED")
        return False

if __name__ == "__main__":
    success = test_scenarios()
    print(f"\nResult: {'PASSED' if success else 'FAILED'}")