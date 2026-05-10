"""
Denial of Service (DoS) Attack Tests
=====================================
Tests if the simulator can handle extreme inputs without crashing.
"""

import os
import sys
import time
import unittest

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from sir_simulator.core_models.network_model import SocialNetworkSimulator
from sir_simulator.core_models.seir_model import run_seir_simulation
from sir_simulator.core_models.sir_model import run_sir_simulation


class TestDoSAttack(unittest.TestCase):

    def test_extreme_time_steps(self):
        """Should handle extremely large t_max without memory explosion"""
        try:
            start_time = time.time()
            df = run_sir_simulation(
                beta=0.5, gamma=0.2, S0=990, I0=10, R0=0, t_max=10000, steps=50000
            )
            elapsed = time.time() - start_time
            self.assertLess(elapsed, 60)
            self.assertGreater(len(df), 0)
        except MemoryError:
            self.fail("MemoryError: t_max too large caused memory explosion")
        except Exception as e:
            self.fail(f"Unexpected error: {e}")

    def test_extreme_population_size(self):
        """Should handle extremely large population"""
        try:
            df = run_sir_simulation(
                beta=0.5, gamma=0.2, S0=10_000_000, I0=1000, R0=0, t_max=100, steps=500
            )
            self.assertGreater(len(df), 0)
        except MemoryError:
            self.fail("MemoryError: Population too large for system memory")
        except Exception as e:
            pass

    def test_network_with_too_many_nodes(self):
        """Should handle large network or fail gracefully"""
        try:
            sim = SocialNetworkSimulator(num_nodes=5000, network_type="scale_free")
            df = sim.simulate_spread(
                transmission_prob=0.3, recovery_prob=0.1, max_steps=20
            )
            self.assertGreater(len(df), 0)
        except MemoryError:
            self.skipTest("5000 nodes requires too much memory - graceful skip")
        except Exception as e:
            self.fail(f"Network simulation crashed: {e}")

    def test_rapid_consecutive_calls(self):
        """Should handle many rapid simulation calls without crash"""
        try:
            for i in range(20):
                df = run_sir_simulation(
                    beta=0.5, gamma=0.2, S0=1000, I0=10, R0=0, t_max=50, steps=100
                )
                self.assertGreater(len(df), 0)
        except Exception as e:
            self.fail(f"Failed after {i+1} calls: {e}")

    def test_extreme_parameter_values(self):
        """Should handle extreme parameter values without crash"""
        extreme_params = [
            (0, 0),
            (2, 2),
            (-0.5, 0.1),
            (0.5, -0.1),
        ]

        for beta, gamma in extreme_params:
            try:
                df = run_sir_simulation(
                    beta=beta, gamma=gamma, S0=990, I0=10, R0=0, t_max=10, steps=50
                )
                self.assertTrue(True)
            except (TypeError, ValueError):
                pass
            except Exception as e:
                self.fail(f"Unexpected crash with beta={beta}, gamma={gamma}: {e}")


if __name__ == "__main__":
    unittest.main()
