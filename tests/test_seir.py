import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_models.seir_model import run_seir_simulation
import pandas as pd
import numpy as np

class TestSEIRModel(unittest.TestCase):
    
    def test_run_seir_simulation_returns_dataframe(self):
        """Test that output is a pandas DataFrame"""
        df = run_seir_simulation(
            beta=0.5, sigma=0.2, gamma=0.1,
            S0=990, E0=5, I0=5, R0=0,
            t_max=100, steps=500
        )
        self.assertIsInstance(df, pd.DataFrame)
    
    def test_run_seir_simulation_has_required_columns(self):
        """Test DataFrame has required columns"""
        df = run_seir_simulation(
            beta=0.5, sigma=0.2, gamma=0.1,
            S0=990, E0=5, I0=5, R0=0,
            t_max=100, steps=500
        )
        required_columns = ['time', 'Susceptible', 'Exposed', 'Infected', 'Recovered']
        for col in required_columns:
            self.assertIn(col, df.columns)
    
    def test_run_seir_simulation_non_empty(self):
        """Test that simulation returns non-empty data"""
        df = run_seir_simulation(
            beta=0.5, sigma=0.2, gamma=0.1,
            S0=990, E0=5, I0=5, R0=0,
            t_max=100, steps=500
        )
        self.assertGreater(len(df), 0)
    
    def test_run_seir_total_population_conserved(self):
        """Test total population remains constant (S+E+I+R = constant)"""
        df = run_seir_simulation(
            beta=0.5, sigma=0.2, gamma=0.1,
            S0=990, E0=5, I0=5, R0=0,
            t_max=100, steps=500
        )
        total_initial = df.iloc[0][['Susceptible', 'Exposed', 'Infected', 'Recovered']].sum()
        for i in range(len(df)):
            total_current = df.iloc[i][['Susceptible', 'Exposed', 'Infected', 'Recovered']].sum()
            self.assertAlmostEqual(total_initial, total_current, places=5)
    
    def test_run_seir_infected_peak_occurs(self):
        """Test that infected count reaches a peak then decreases"""
        df = run_seir_simulation(
            beta=0.5, sigma=0.2, gamma=0.1,
            S0=990, E0=5, I0=5, R0=0,
            t_max=200, steps=1000
        )
        infected = df['Infected'].values
        peak_index = np.argmax(infected)
        self.assertGreater(peak_index, 0)
        self.assertLess(peak_index, len(infected) - 1)
    
    def test_run_seir_with_zero_initial_infected(self):
        """Test behavior when I0 = 0 (no outbreak)"""
        df = run_seir_simulation(
            beta=0.5, sigma=0.2, gamma=0.1,
            S0=1000, E0=0, I0=0, R0=0,
            t_max=100, steps=500
        )
        infected = df['Infected'].values
        self.assertTrue(np.all(infected == 0))
    
    def test_run_seir_with_different_beta_values(self):
        """Test that higher beta gives higher peak"""
        df_low = run_seir_simulation(beta=0.2, sigma=0.2, gamma=0.1, S0=990, E0=5, I0=5, R0=0, t_max=100, steps=500)
        df_high = run_seir_simulation(beta=0.8, sigma=0.2, gamma=0.1, S0=990, E0=5, I0=5, R0=0, t_max=100, steps=500)
        
        peak_low = df_low['Infected'].max()
        peak_high = df_high['Infected'].max()
        self.assertGreater(peak_high, peak_low)

if __name__ == '__main__':
    unittest.main()