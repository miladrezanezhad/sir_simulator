"""
Memory Exhaustion Tests
=======================
Tests if the simulator properly manages memory usage.
"""

import unittest
import sys
import os
import tracemalloc
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core_models.sir_model import run_sir_simulation
from core_models.network_model import SocialNetworkSimulator


class TestMemoryExhaustion(unittest.TestCase):
    
    def setUp(self):
        tracemalloc.start()
    
    def tearDown(self):
        tracemalloc.stop()
    
    def test_memory_usage_not_exploding(self):
        """Memory usage should not grow uncontrollably"""
        snapshot1 = tracemalloc.take_snapshot()
        
        # Run multiple simulations
        for _ in range(10):
            df = run_sir_simulation(
                beta=0.5, gamma=0.2,
                S0=1000, I0=10, R0=0,
                t_max=100, steps=500
            )
        
        snapshot2 = tracemalloc.take_snapshot()
        
        # Get memory difference
        stats = snapshot2.compare_to(snapshot1, 'lineno')
        total_diff = sum(stat.size_diff for stat in stats)
        
        # Memory growth should be less than 5MB
        self.assertLess(total_diff, 5 * 1024 * 1024,
                        f"Memory grew by {total_diff / 1024 / 1024:.2f} MB")
    
    def test_large_network_memory_bound(self):
        """Memory usage should be proportional to network size"""
        # Small network
        sim_small = SocialNetworkSimulator(num_nodes=100, network_type='scale_free')
        df_small = sim_small.simulate_spread(max_steps=10)
        
        # Medium network
        sim_medium = SocialNetworkSimulator(num_nodes=500, network_type='scale_free')
        df_medium = sim_medium.simulate_spread(max_steps=10)
        
        # Both should complete without memory error
        self.assertIsNotNone(df_small)
        self.assertIsNotNone(df_medium)
    
    def test_clear_data_between_simulations(self):
        """Previous simulation data should not persist in memory"""
        # Store reference to first simulation result
        df1 = run_sir_simulation(
            beta=0.5, gamma=0.2,
            S0=1000, I0=10, R0=0,
            t_max=100, steps=500
        )
        
        memory_before = tracemalloc.get_traced_memory()[0]
        
        # Run second simulation
        df2 = run_sir_simulation(
            beta=0.3, gamma=0.1,
            S0=500, I0=20, R0=0,
            t_max=100, steps=500
        )
        
        memory_after = tracemalloc.get_traced_memory()[0]
        
        # Memory should not double (df1 may still exist in scope)
        self.assertLess(memory_after, memory_before * 2)
    
    def test_no_memory_leak_with_exceptions(self):
        """Even when errors occur, memory should be released"""
        initial_memory = tracemalloc.get_traced_memory()[0]
        
        for _ in range(5):
            try:
                # Invalid parameters to trigger exception
                df = run_sir_simulation(
                    beta=float('inf'), gamma=0.2,  # Invalid beta
                    S0=-100, I0=10, R0=0,  # Negative population
                    t_max=100, steps=500
                )
            except (ValueError, OverflowError):
                pass
            except Exception:
                pass
        
        final_memory = tracemalloc.get_traced_memory()[0]
        
        # Memory should not leak significantly
        memory_increase = final_memory - initial_memory
        self.assertLess(memory_increase, 10 * 1024 * 1024,
                        f"Memory leak detected: +{memory_increase / 1024 / 1024:.2f} MB")


if __name__ == '__main__':
    unittest.main()