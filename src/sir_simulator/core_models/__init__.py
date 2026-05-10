"""
Core Models Module

Contains fundamental epidemic models:
- SIR Model
- SEIR Model
- Social Network Simulation
"""

from .network_model import SocialNetworkSimulator
from .seir_model import run_seir_simulation
from .sir_model import run_sir_simulation

__all__ = [
    "run_sir_simulation",
    "calculate_R0",
    "calculate_peak_infected",
    "run_seir_simulation",
    "SocialNetworkSimulator",
]
