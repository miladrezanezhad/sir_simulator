import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
import pandas as pd

from sir_simulator.core_models.seird_model import run_seird_simulation


class TestSEIRDModel(unittest.TestCase):

    def setUp(self):
        self.default_params = {
            "beta": 0.5,
            "sigma": 0.2,
            "gamma": 0.1,
            "mu": 0.02,
            "S0": 980,
            "E0": 10,
            "I0": 10,
            "R0": 0,
            "D0": 0,
            "t_max": 100,
            "steps": 500,
        }

    def test_run_seird_simulation_returns_dataframe(self):
        """Test that output is a pandas DataFrame"""
        df = run_seird_simulation(**self.default_params)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), self.default_params["steps"])

    def test_run_seird_simulation_has_required_columns(self):
        """Test DataFrame has required columns"""
        df = run_seird_simulation(**self.default_params)
        required_columns = [
            "time",
            "Susceptible",
            "Exposed",
            "Infected",
            "Recovered",
            "Deceased",
        ]
        for col in required_columns:
            self.assertIn(col, df.columns)

    def test_run_seird_total_population_conserved(self):
        """Test total population remains constant (S + E + I + R + D = constant)"""
        df = run_seird_simulation(**self.default_params)
        compartments = ["Susceptible", "Exposed", "Infected", "Recovered", "Deceased"]
        total_initial = df.iloc[0][compartments].sum()

        for i in range(len(df)):
            total_current = df.iloc[i][compartments].sum()
            self.assertAlmostEqual(total_initial, total_current, places=4)

    def test_deceased_monotonically_non_decreasing(self):
        """Test that cumulative deceased count is non-decreasing over time"""
        df = run_seird_simulation(**self.default_params)
        deceased = df["Deceased"].values
        diffs = np.diff(deceased)
        # Numerical precision tolerance
        self.assertTrue(np.all(diffs >= -1e-7))

    def test_infected_reaches_peak_and_declines(self):
        """Test that infected curve reaches an interior peak"""
        df = run_seird_simulation(
            beta=0.6,
            sigma=0.2,
            gamma=0.1,
            mu=0.03,
            S0=980,
            E0=10,
            I0=10,
            R0=0,
            D0=0,
            t_max=150,
            steps=750,
        )
        infected = df["Infected"].values
        peak_idx = int(np.argmax(infected))
        self.assertGreater(peak_idx, 0)
        self.assertLess(peak_idx, len(infected) - 1)

    def test_zero_initial_infection_no_epidemic(self):
        """Test that without infected individuals, no epidemic or deaths occur"""
        df = run_seird_simulation(
            beta=0.5,
            sigma=0.2,
            gamma=0.1,
            mu=0.02,
            S0=1000,
            E0=0,
            I0=0,
            R0=0,
            D0=0,
            t_max=50,
            steps=100,
        )
        self.assertTrue(np.all(df["Infected"] == 0))
        self.assertTrue(np.all(df["Deceased"] == 0))
        self.assertTrue(np.all(df["Susceptible"] == 1000))


if __name__ == "__main__":
    unittest.main()
