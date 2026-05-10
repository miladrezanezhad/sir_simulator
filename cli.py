#!/usr/bin/env python3
"""
SIR Model - Command Line Interface

Usage examples:
    python cli.py
    python cli.py --beta 0.8 --gamma 0.3 --tmax 200
    python cli.py --beta 0.4 --gamma 0.1 --output my_simulation.csv
"""

import argparse
import sys
from sir_model import run_sir_simulation, calculate_R0, calculate_peak_infected

def main():
    parser = argparse.ArgumentParser(
        description="SIR Epidemic Model Simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--beta", type=float, default=0.5,
                        help="Transmission rate (default: 0.5)")
    parser.add_argument("--gamma", type=float, default=0.2,
                        help="Recovery rate (default: 0.2)")
    parser.add_argument("--S0", type=float, default=990,
                        help="Initial susceptible population (default: 990)")
    parser.add_argument("--I0", type=float, default=10,
                        help="Initial infected population (default: 10)")
    parser.add_argument("--R0", type=float, default=0,
                        help="Initial recovered population (default: 0)")
    parser.add_argument("--tmax", type=int, default=100,
                        help="Simulation duration in days (default: 100)")
    parser.add_argument("--steps", type=int, default=500,
                        help="Number of time points (default: 500)")
    parser.add_argument("--output", type=str, default="sir_output.csv",
                        help="Output CSV filename (default: sir_output.csv)")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress console output")
    
    args = parser.parse_args()
    
    # Run simulation
    df = run_sir_simulation(
        args.beta, args.gamma,
        args.S0, args.I0, args.R0,
        args.tmax, args.steps
    )
    
    # Save to CSV
    df.to_csv(args.output, index=False)
    
    if not args.quiet:
        print("=" * 60)
        print("SIR EPIDEMIC SIMULATION RESULTS")
        print("=" * 60)
        print(f"Parameters:")
        print(f"  β (transmission rate) = {args.beta}")
        print(f"  γ (recovery rate)     = {args.gamma}")
        print(f"  R₀ = β/γ              = {calculate_R0(args.beta, args.gamma):.3f}")
        print(f"  Initial: S={args.S0}, I={args.I0}, R={args.R0}")
        print(f"  Duration: {args.tmax} days")
        print("-" * 60)
        
        # Statistics
        peak_infected, peak_time = calculate_peak_infected(df)
        final_S = df['Susceptible'].iloc[-1]
        final_I = df['Infected'].iloc[-1]
        final_R = df['Recovered'].iloc[-1]
        
        print(f"Results:")
        print(f"  Peak infected: {peak_infected:.0f} at day {peak_time:.1f}")
        print(f"  Final state: S={final_S:.0f}, I={final_I:.0f}, R={final_R:.0f}")
        print("-" * 60)
        print(f"✅ Output saved to: {args.output}")
        print("=" * 60)
        
        # Show last 5 rows
        print("\nLast 5 time points:")
        print(df.tail().to_string(index=False))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())