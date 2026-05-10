import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from advanced_features.scenario_comparison import ScenarioComparator
import pandas as pd

class TestScenarioComparison(unittest.TestCase):
    
    def test_comparator_initialization(self):
        comp = ScenarioComparator()
        self.assertIsNotNone(comp)
    
    def test_compare_all_scenarios_returns_tuple(self):
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(days=100)
        
        self.assertIsInstance(scenarios, dict)
        self.assertIsInstance(metrics, pd.DataFrame)
    
    def test_compare_all_scenarios_has_expected_keys(self):
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(days=100)
        
        expected_scenarios = ['Baseline', 'Quarantine', 'Vaccination', 'Combined']
        for scenario in expected_scenarios:
            self.assertIn(scenario, scenarios)
    
    def test_scenario_dataframe_has_required_columns(self):
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(days=100)
        
        required_columns = ['day', 'susceptible', 'infected', 'recovered']
        for scenario_name, df in scenarios.items():
            for col in required_columns:
                self.assertIn(col, df.columns)
    
    def test_quarantine_reduces_peak_infected(self):
        comp = ScenarioComparator(beta=0.3, gamma=0.1)
        scenarios, metrics = comp.compare_all_scenarios(days=120)
        
        baseline_peak = scenarios['Baseline']['infected'].max()
        quarantine_peak = scenarios['Quarantine']['infected'].max()
        
        self.assertLess(quarantine_peak, baseline_peak)
    
    def test_vaccination_reduces_peak_infected(self):
        comp = ScenarioComparator(beta=0.3, gamma=0.1)
        scenarios, metrics = comp.compare_all_scenarios(days=120)
        
        baseline_peak = scenarios['Baseline']['infected'].max()
        vaccination_peak = scenarios['Vaccination']['infected'].max()
        
        self.assertLess(vaccination_peak, baseline_peak)
    
    def test_metrics_dataframe_has_required_columns(self):
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(days=100)
        
        expected_columns = ['scenario', 'peak_infected', 'peak_day', 'reduction']
        for col in expected_columns:
            self.assertIn(col, metrics.columns)
    
    def test_metrics_has_four_scenarios(self):
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(days=100)
        
        self.assertEqual(len(metrics), 4)

if __name__ == '__main__':
    unittest.main()