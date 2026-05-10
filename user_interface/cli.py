#!/usr/bin/env python3
"""
SIR Model - Command Line Interface
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
from core_models.sir_model import run_sir_simulation, calculate_R0, calculate_peak_infected

def main():
    parser = argparse.ArgumentParser(description="SIR Epidemic Model Simulator")
    
    parser.add_argument("--beta", type=float, default=0.5, help="Transmission rate")
    parser.add_argument("--gamma", type=float, default=0.2, help="Recovery rate")
    parser.add_argument("--S0", type=float, default=990, help="Initial susceptible")
    parser.add_argument("--I0", type=float, default=10, help="Initial infected")
    parser.add_argument("--tmax", type=int, default=100, help="Simulation days")
    parser.add_argument("--output", type=str, default="sir_output.csv", help="Output CSV file")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    
    args = parser.parse_args()
    
    df = run_sir_simulation(args.beta, args.gamma, args.S0, args.I0, 0, args.tmax, 500)
    df.to_csv(args.output, index=False)
    
    if not args.quiet:
        print("=" * 60)
        print("SIR EPIDEMIC SIMULATION RESULTS")
        print("=" * 60)
        print(f"β = {args.beta}, γ = {args.gamma}, R₀ = {calculate_R0(args.beta, args.gamma):.3f}")
        print(f"Initial: S={args.S0}, I={args.I0}")
        
        peak, peak_time = calculate_peak_infected(df)
        print(f"Peak infected: {peak:.0f} at day {peak_time:.1f}")
        print(f"Final: S={df['Susceptible'].iloc[-1]:.0f}, I={df['Infected'].iloc[-1]:.0f}, R={df['Recovered'].iloc[-1]:.0f}")
        print(f"✅ Output saved to: {args.output}")

if __name__ == "__main__":
    main()