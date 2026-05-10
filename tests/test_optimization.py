import os
import sys
import unittest

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sir_simulator.advanced_features.parameter_optimization import ParameterOptimizer


class TestParameterOptimization(unittest.TestCase):

    def test_optimizer_initialization_sir(self):
        """Test ParameterOptimizer initializes for SIR model"""
        optimizer = ParameterOptimizer(model_type="sir")
        self.assertIsNotNone(optimizer)

    def test_optimizer_initialization_seir(self):
        """Test ParameterOptimizer initializes for SEIR model"""
        optimizer = ParameterOptimizer(model_type="seir")
        self.assertIsNotNone(optimizer)

    def test_fit_returns_expected_keys(self):
        """Test fit method returns dictionary with expected keys"""
        t = np.linspace(0, 100, 50)
        observed_data = 100 * np.exp(-0.1 * t) + 5 * np.random.randn(len(t))

        optimizer = ParameterOptimizer(model_type="sir")
        results = optimizer.fit(observed_data, t, [990, 10, 0])

        expected_keys = ["beta", "gamma", "R0", "r_squared"]
        for key in expected_keys:
            self.assertIn(key, results)

    def test_fit_returns_numeric_values(self):
        """Test fit returns numeric parameter values"""
        t = np.linspace(0, 100, 50)
        observed_data = 100 * np.exp(-0.1 * t) + 5 * np.random.randn(len(t))

        optimizer = ParameterOptimizer(model_type="sir")
        results = optimizer.fit(observed_data, t, [990, 10, 0])

        self.assertIsInstance(results["beta"], float)
        self.assertIsInstance(results["gamma"], float)
        self.assertIsInstance(results["R0"], float)

    def test_R0_positive(self):
        """Test R0 is positive"""
        t = np.linspace(0, 100, 50)
        observed_data = 100 * np.exp(-0.1 * t) + 5 * np.random.randn(len(t))

        optimizer = ParameterOptimizer(model_type="sir")
        results = optimizer.fit(observed_data, t, [990, 10, 0])

        self.assertGreater(results["R0"], 0)

    def test_r_squared_between_0_and_1(self):
        """Test R² score is between 0 and 1"""
        t = np.linspace(0, 100, 50)
        observed_data = 100 * np.exp(-0.1 * t) + 5 * np.random.randn(len(t))

        optimizer = ParameterOptimizer(model_type="sir")
        results = optimizer.fit(observed_data, t, [990, 10, 0])

        self.assertGreaterEqual(results["r_squared"], 0)
        self.assertLessEqual(results["r_squared"], 1)


if __name__ == "__main__":
    unittest.main()
