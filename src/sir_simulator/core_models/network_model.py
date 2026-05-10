"""
Social Network Simulation for Fake News Spread
===============================================
SIR model on graph structures
"""

import networkx as nx
import numpy as np
import pandas as pd


class SocialNetworkSimulator:
    """
    Simulate fake news spread on social networks
    Similar to SIR but on a graph structure
    """

    def __init__(self, num_nodes=100, network_type="small_world"):
        """
        Initialize social network

        Parameters:
        - num_nodes: number of people in network
        - network_type: 'small_world', 'scale_free', or 'random'
        """
        self.num_nodes = num_nodes
        self.network_type = network_type
        self.graph = self._create_network()
        self.S = set()
        self.I = set()
        self.R = set()

    def _create_network(self):
        """Create social network graph"""
        if self.network_type == "small_world":
            return nx.watts_strogatz_graph(self.num_nodes, k=4, p=0.1)
        elif self.network_type == "scale_free":
            return nx.barabasi_albert_graph(self.num_nodes, m=3)
        else:
            return nx.erdos_renyi_graph(self.num_nodes, p=0.05)

    def get_network_stats(self):
        """Get network statistics"""
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "avg_degree": np.mean([d for n, d in self.graph.degree()]),
            "density": nx.density(self.graph),
        }

    def simulate_spread(
        self, transmission_prob=0.3, recovery_prob=0.1, initial_infected=5, max_steps=50
    ):
        """
        Simulate fake news spread using SIR model on network
        """
        all_nodes = set(range(self.num_nodes))
        self.S = all_nodes.copy()
        self.I = set()
        self.R = set()

        initial_infected_nodes = np.random.choice(
            list(all_nodes), size=min(initial_infected, self.num_nodes), replace=False
        )
        self.I.update(initial_infected_nodes)
        self.S -= self.I

        history = []

        for step in range(max_steps):
            history.append(
                {
                    "step": step,
                    "susceptible": len(self.S),
                    "infected": len(self.I),
                    "recovered": len(self.R),
                }
            )

            if len(self.I) == 0:
                break

            new_infected = set()
            recovered_this_step = set()

            for node in self.I:
                if np.random.random() < recovery_prob:
                    recovered_this_step.add(node)
                    continue

                for neighbor in self.graph.neighbors(node):
                    if neighbor in self.S and np.random.random() < transmission_prob:
                        new_infected.add(neighbor)

            self.I -= recovered_this_step
            self.R.update(recovered_this_step)
            self.I.update(new_infected)
            self.S -= new_infected

        return pd.DataFrame(history)

    def visualize_network(self, show_labels=False):
        """Visualize the social network"""
        import matplotlib.pyplot as plt

        pos = nx.spring_layout(self.graph, seed=42)
        plt.figure(figsize=(10, 8))

        node_colors = []
        for node in self.graph.nodes():
            if node in self.I:
                node_colors.append("red")
            elif node in self.R:
                node_colors.append("green")
            else:
                node_colors.append("blue")

        nx.draw(
            self.graph,
            pos,
            node_color=node_colors,
            node_size=50,
            with_labels=show_labels,
            edge_color="gray",
            alpha=0.6,
        )

        plt.title("Social Network (Red=Spreaders, Green=Recovered, Blue=Susceptible)")
        plt.show()


if __name__ == "__main__":
    sim = SocialNetworkSimulator(200, "scale_free")
    print(sim.get_network_stats())
    df = sim.simulate_spread(0.4, 0.1, 5, 50)
    print(df.tail())
