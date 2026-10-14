import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
import pandas as pd

from sir_simulator.core_models.sirs_model import run_sirs_simulation


class TestSIRSModel(unittest.TestCase):

    def setUp(self):
        self.default_params = {
            "beta": 0.4,
            "gamma": 0.1,
            "xi": 0.02,
            "S0": 990,
            "I0": 10,
            "R0": 0,
            "t_max": 200,
            "steps": 1000,
        }

    def test_run_sirs_simulation_returns_dataframe(self):
        """Test output is a pandas DataFrame"""
        df = run_sirs_simulation(**self.default_params)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), self.default_params["steps"])

    def test_run_sirs_simulation_has_required_columns(self):
        """Test DataFrame contains required columns"""
        df = run_sirs_simulation(**self.default_params)
        for col in ["time", "Susceptible", "Infected", "Recovered"]:
            self.assertIn(col, df.columns)

    def test_sirs_total_population_conserved(self):
        """Test total population conservation (S + I + R = constant)"""
        df = run_sirs_simulation(**self.default_params)
        compartments = ["Susceptible", "Infected", "Recovered"]
        initial_pop = df.iloc[0][compartments].sum()

        for i in range(len(df)):
            current_pop = df.iloc[i][compartments].sum()
            self.assertAlmostEqual(initial_pop, current_pop, places=4)

    def test_sirs_endemic_persistence(self):
        """Test that with waning immunity, infected population persists (endemic equilibrium)"""
        df = run_sirs_simulation(
            beta=0.4,
            gamma=0.1,
            xi=0.03,
            S0=990,
            I0=10,
            R0=0,
            t_max=300,
            steps=1500,
        )
        final_infected = df["Infected"].iloc[-1]
        # In endemic state with R0 = 4, infected individuals remain > 0
        self.assertGreater(final_infected, 1.0)

    def test_sirs_zero_waning_behaves_like_sir(self):
        """Test that with xi=0 (no loss of immunity), infection eventually approaches zero"""
        df = run_sirs_simulation(
            beta=0.4,
            gamma=0.1,
            xi=0.0,
            S0=990,
            I0=10,
            R0=0,
            t_max=150,
            steps=500,
        )
        final_infected = df["Infected"].iloc[-1]
        self.assertLess(final_infected, 1.0)


if __name__ == "__main__":
    unittest.main()
