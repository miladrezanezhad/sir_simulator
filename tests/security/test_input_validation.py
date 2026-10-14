"""
Input Validation and Robustness Security Tests
==============================================
Validates that core models and optimization pipelines safely handle
malformed, invalid, out-of-bound, and boundary input values without unhandled crashes.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from sir_simulator.advanced_features.parameter_optimization import ParameterOptimizer
from sir_simulator.core_models.seird_model import run_seird_simulation
from sir_simulator.core_models.sir_model import run_sir_simulation
from sir_simulator.core_models.sirs_model import run_sirs_simulation


class TestInputValidation(unittest.TestCase):

    def test_zero_total_population_safety(self):
        """Should safely handle zero total population without division by zero crash"""
        try:
            df = run_sir_simulation(
                beta=0.5, gamma=0.2, S0=0, I0=0, R0=0, t_max=10, steps=20
            )
            self.assertEqual(len(df), 20)
        except ZeroDivisionError:
            self.fail("ZeroDivisionError encountered for S0=0, I0=0, R0=0")

    def test_seird_zero_population_safety(self):
        """Should safely handle zero population in SEIRD"""
        try:
            df = run_seird_simulation(
                beta=0.5,
                sigma=0.2,
                gamma=0.1,
                mu=0.02,
                S0=0,
                E0=0,
                I0=0,
                R0=0,
                D0=0,
                t_max=10,
                steps=20,
            )
            self.assertEqual(len(df), 20)
        except ZeroDivisionError:
            self.fail("ZeroDivisionError encountered in SEIRD")

    def test_parameter_optimizer_out_of_bounds_rejection(self):
        """Optimizer cost function should penalize out-of-bounds parameters safely"""
        optimizer = ParameterOptimizer(model_type="sir")
        t = np.linspace(0, 10, 10)
        real_data = np.ones(10)
        initial_conditions = [990, 10, 0]

        # Negative beta
        cost_neg_beta = optimizer.cost_function(
            [-0.5, 0.2], t, real_data, initial_conditions
        )
        self.assertGreaterEqual(cost_neg_beta, 1e9)

        # Huge beta (> 2)
        cost_huge_beta = optimizer.cost_function(
            [5.0, 0.2], t, real_data, initial_conditions
        )
        self.assertGreaterEqual(cost_huge_beta, 1e9)

        # Negative gamma
        cost_neg_gamma = optimizer.cost_function(
            [0.5, -0.1], t, real_data, initial_conditions
        )
        self.assertGreaterEqual(cost_neg_gamma, 1e9)

    def test_sirs_waning_rate_bounds(self):
        """SIRS should run safely with zero or very small waning rates"""
        df = run_sirs_simulation(
            beta=0.3, gamma=0.1, xi=0.0, S0=100, I0=5, R0=0, t_max=20, steps=50
        )
        self.assertFalse(df.isna().any().any())


if __name__ == "__main__":
    unittest.main()
