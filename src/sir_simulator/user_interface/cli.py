"""
Command Line Interface for SIR Simulator
========================================
Run simulations from terminal
"""

import argparse
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sir_simulator.core_models.network_model import SocialNetworkSimulator
from sir_simulator.core_models.seir_model import run_seir_simulation
from sir_simulator.core_models.sir_model import run_sir_simulation


def main():
    parser = argparse.ArgumentParser(description="SIR Epidemic Simulator CLI")
    parser.add_argument(
        "--model",
        type=str,
        default="sir",
        choices=["sir", "seir", "network"],
        help="Model type to simulate",
    )
    parser.add_argument("--beta", type=float, default=0.5, help="Infection rate")
    parser.add_argument("--gamma", type=float, default=0.2, help="Recovery rate")
    parser.add_argument(
        "--sigma", type=float, default=0.2, help="Incubation rate (for SEIR)"
    )
    parser.add_argument("--S0", type=int, default=990, help="Initial susceptible")
    parser.add_argument("--I0", type=int, default=10, help="Initial infected")
    parser.add_argument("--E0", type=int, default=0, help="Initial exposed (for SEIR)")
    parser.add_argument("--R0", type=int, default=0, help="Initial recovered")
    parser.add_argument("--tmax", type=int, default=100, help="Maximum time")
    parser.add_argument("--steps", type=int, default=500, help="Number of time steps")
    parser.add_argument(
        "--output", type=str, default="simulation_output.csv", help="Output CSV file"
    )

    args = parser.parse_args()

    print(f"\n🦠 Running {args.model.upper()} Simulation...")
    print(f"Parameters: beta={args.beta}, gamma={args.gamma}")

    if args.model == "sir":
        df = run_sir_simulation(
            beta=args.beta,
            gamma=args.gamma,
            S0=args.S0,
            I0=args.I0,
            R0=args.R0,
            t_max=args.tmax,
            steps=args.steps,
        )
    elif args.model == "seir":
        df = run_seir_simulation(
            beta=args.beta,
            sigma=args.sigma,
            gamma=args.gamma,
            S0=args.S0,
            E0=args.E0,
            I0=args.I0,
            R0=args.R0,
            t_max=args.tmax,
            steps=args.steps,
        )
    else:
        sim = SocialNetworkSimulator(num_nodes=200, network_type="scale_free")
        df = sim.simulate_spread(transmission_prob=args.beta, recovery_prob=args.gamma)

    print(f"\n✅ Simulation complete!")
    print(f"📊 Output shape: {df.shape}")
    print(f"\n📈 Last 5 rows:")
    print(df.tail())

    df.to_csv(args.output, index=False)
    print(f"\n💾 Saved to: {args.output}")

    return df


if __name__ == "__main__":
    main()
