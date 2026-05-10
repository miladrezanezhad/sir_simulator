import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd

from sir_simulator.core_models.network_model import SocialNetworkSimulator


class TestNetworkModel(unittest.TestCase):

    def test_social_network_simulator_initialization(self):
        """Test simulator initializes correctly"""
        sim = SocialNetworkSimulator(num_nodes=100, network_type="scale_free")
        self.assertIsNotNone(sim.graph)
        self.assertEqual(sim.num_nodes, 100)

    def test_social_network_simulator_returns_dataframe(self):
        """Test simulate_spread returns DataFrame"""
        sim = SocialNetworkSimulator(num_nodes=50, network_type="small_world")
        df = sim.simulate_spread(transmission_prob=0.3, recovery_prob=0.1)
        self.assertIsInstance(df, pd.DataFrame)

    def test_social_network_simulator_has_required_columns(self):
        """Test output DataFrame has required columns"""
        sim = SocialNetworkSimulator(num_nodes=50, network_type="scale_free")
        df = sim.simulate_spread(transmission_prob=0.3, recovery_prob=0.1)
        required_columns = ["step", "susceptible", "infected", "recovered"]
        for col in required_columns:
            self.assertIn(col, df.columns)

    def test_network_simulation_infected_increases_initially(self):
        """Test that infected count increases in early steps"""
        sim = SocialNetworkSimulator(num_nodes=100, network_type="scale_free")
        df = sim.simulate_spread(
            transmission_prob=0.5, recovery_prob=0.05, max_steps=30
        )

        if len(df) > 1:
            initial_infected = df.iloc[0]["infected"]
            later_infected = df.iloc[min(5, len(df) - 1)]["infected"]
            self.assertGreaterEqual(later_infected, initial_infected)

    def test_network_simulation_eventually_recovers(self):
        """Test that all nodes eventually recover or remain susceptible"""
        sim = SocialNetworkSimulator(num_nodes=80, network_type="small_world")
        df = sim.simulate_spread(
            transmission_prob=0.4, recovery_prob=0.15, max_steps=200
        )

        final_infected = df.iloc[-1]["infected"]
        self.assertEqual(final_infected, 0)

    def test_network_simulation_zero_transmission(self):
        """Test no new spread when transmission_prob = 0 (only initial infected)"""
        sim = SocialNetworkSimulator(num_nodes=50, network_type="scale_free")
        df = sim.simulate_spread(
            transmission_prob=0.0, recovery_prob=0.1, initial_infected=5, max_steps=20
        )

        peak_infected = df["infected"].max()
        self.assertEqual(peak_infected, 5)

    def test_different_network_types_initializable(self):
        """Test all network types can be initialized"""
        network_types = ["scale_free", "small_world", "random"]
        for net_type in network_types:
            sim = SocialNetworkSimulator(num_nodes=60, network_type=net_type)
            self.assertIsNotNone(sim.graph)

    def test_network_stats_returns_dict(self):
        """Test get_network_stats returns dictionary with expected keys"""
        sim = SocialNetworkSimulator(num_nodes=100, network_type="scale_free")
        stats = sim.get_network_stats()

        self.assertIsInstance(stats, dict)
        self.assertIn("nodes", stats)
        self.assertIn("edges", stats)
        self.assertIn("avg_degree", stats)
        self.assertIn("density", stats)

    def test_network_simulation_respects_max_steps(self):
        """Test that simulation stops at max_steps"""
        max_steps = 25
        sim = SocialNetworkSimulator(num_nodes=50, network_type="small_world")
        df = sim.simulate_spread(
            transmission_prob=0.3, recovery_prob=0.1, max_steps=max_steps
        )

        self.assertLessEqual(len(df), max_steps + 1)

    def test_network_simulation_with_high_recovery(self):
        """Test high recovery probability quickly ends outbreak"""
        sim = SocialNetworkSimulator(num_nodes=50, network_type="scale_free")
        df = sim.simulate_spread(transmission_prob=0.5, recovery_prob=0.9, max_steps=50)

        self.assertLessEqual(len(df), 20)


if __name__ == "__main__":
    unittest.main()
