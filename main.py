#!/usr/bin/env python3
"""
Interactive Menu for SIR Epidemic Simulator
"""

import os
import sys

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from sir_simulator.advanced_features.ml_prediction import EpidemicPredictor
from sir_simulator.advanced_features.parameter_optimization import ParameterOptimizer
from sir_simulator.advanced_features.scenario_comparison import ScenarioComparator
from sir_simulator.core_models.network_model import SocialNetworkSimulator
from sir_simulator.core_models.seir_model import run_seir_simulation
from sir_simulator.core_models.sir_model import run_sir_simulation


def print_menu():
    """Display main menu"""
    print("\n" + "🦠" * 25)
    print("   SIR EPIDEMIC SIMULATOR")
    print("🦠" * 25)
    print("")
    print("   MAIN MENU")
    print("   " + "-" * 40)
    print("")
    print("   1. Run SIR Model")
    print("   2. Run SEIR Model")
    print("   3. Run Network Simulation")
    print("   4. Parameter Optimization")
    print("   5. ML Prediction")
    print("   6. Scenario Comparison")
    print("   7. Run All Tests")
    print("   0. Exit")
    print("")
    print("   " + "-" * 40)
    print("🦠" * 25)


def run_sir():
    """Run SIR model simulation"""
    print("\n" + "=" * 50)
    print("SIR MODEL SIMULATION")
    print("=" * 50)

    try:
        print("\nEnter simulation parameters:")
        beta = float(input("   Infection rate (β) [0.5]: ") or 0.5)
        gamma = float(input("   Recovery rate (γ) [0.2]: ") or 0.2)
        S0 = int(input("   Initial susceptible [990]: ") or 990)
        I0 = int(input("   Initial infected [10]: ") or 10)
        t_max = int(input("   Time range (days) [100]: ") or 100)

        print("\nRunning simulation...")
        df = run_sir_simulation(beta, gamma, S0, I0, 0, t_max)

        print("\n[SUCCESS] Simulation complete!")
        print("\nRESULTS:")
        print("-" * 30)
        print(f"   Peak infected: {int(df['Infected'].max())}")
        print(f"   Final susceptible: {int(df['Susceptible'].iloc[-1])}")
        print(f"   Final recovered: {int(df['Recovered'].iloc[-1])}")
        print(f"   R0 value: {beta/gamma:.2f}")
        print("-" * 30)

        save = input("\nSave to CSV? (y/n): ").lower()
        if save == "y":
            filename = input("   Filename [sir_output.csv]: ") or "sir_output.csv"
            df.to_csv(filename, index=False)
            print(f"\n[SUCCESS] Saved to {filename}")

    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_seir():
    """Run SEIR model simulation"""
    print("\n" + "=" * 50)
    print("SEIR MODEL SIMULATION")
    print("=" * 50)

    try:
        print("\nEnter simulation parameters:")
        beta = float(input("   Infection rate (β) [0.5]: ") or 0.5)
        sigma = float(input("   Incubation rate (σ) [0.2]: ") or 0.2)
        gamma = float(input("   Recovery rate (γ) [0.1]: ") or 0.1)
        S0 = int(input("   Initial susceptible [990]: ") or 990)
        E0 = int(input("   Initial exposed [5]: ") or 5)
        I0 = int(input("   Initial infected [5]: ") or 5)
        t_max = int(input("   Time range (days) [100]: ") or 100)

        print("\nRunning simulation...")
        df = run_seir_simulation(beta, sigma, gamma, S0, E0, I0, 0, t_max)

        print("\n[SUCCESS] Simulation complete!")
        print("\nRESULTS:")
        print("-" * 30)
        print(f"   Peak infected: {int(df['Infected'].max())}")
        print(f"   Peak exposed: {int(df['Exposed'].max())}")
        print(f"   Final susceptible: {int(df['Susceptible'].iloc[-1])}")
        print(f"   Final recovered: {int(df['Recovered'].iloc[-1])}")
        print(f"   R0 value: {beta/gamma:.2f}")
        print("-" * 30)

        save = input("\nSave to CSV? (y/n): ").lower()
        if save == "y":
            filename = input("   Filename [seir_output.csv]: ") or "seir_output.csv"
            df.to_csv(filename, index=False)
            print(f"\n[SUCCESS] Saved to {filename}")

    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_network():
    """Run network simulation"""
    print("\n" + "=" * 50)
    print("NETWORK SIMULATION (Fake News Spread)")
    print("=" * 50)

    try:
        print("\nEnter simulation parameters:")
        num_nodes = int(input("   Number of nodes [200]: ") or 200)
        net_type = (
            input("   Network type (scale_free/small_world/random) [scale_free]: ")
            or "scale_free"
        )
        transmission = float(input("   Transmission probability [0.3]: ") or 0.3)
        recovery = float(input("   Recovery probability [0.1]: ") or 0.1)
        max_steps = int(input("   Max steps [50]: ") or 50)

        print("\nBuilding network...")
        sim = SocialNetworkSimulator(num_nodes, net_type)
        stats = sim.get_network_stats()

        print("\nNETWORK STATISTICS:")
        print("-" * 30)
        print(f"   Nodes: {stats['nodes']}")
        print(f"   Edges: {stats['edges']}")
        print(f"   Avg Degree: {stats['avg_degree']:.2f}")
        print(f"   Density: {stats['density']:.4f}")
        print("-" * 30)

        print("\nRunning simulation...")
        df = sim.simulate_spread(transmission, recovery, max_steps=max_steps)

        print("\n[SUCCESS] Simulation complete!")
        print("\nRESULTS:")
        print("-" * 30)
        print(f"   Final susceptible: {df['susceptible'].iloc[-1]}")
        print(f"   Final infected: {df['infected'].iloc[-1]}")
        print(f"   Final recovered: {df['recovered'].iloc[-1]}")
        print("-" * 30)

        save = input("\nSave to CSV? (y/n): ").lower()
        if save == "y":
            filename = (
                input("   Filename [network_output.csv]: ") or "network_output.csv"
            )
            df.to_csv(filename, index=False)
            print(f"\n[SUCCESS] Saved to {filename}")

    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_optimization():
    """Run parameter optimization"""
    print("\n" + "=" * 50)
    print("PARAMETER OPTIMIZATION")
    print("=" * 50)
    print("\nNOTE: This requires observed data. Using synthetic data for demo.\n")

    try:
        import numpy as np

        print("Generating synthetic data...")

        t = np.linspace(0, 100, 100)
        true_beta, true_gamma = 0.5, 0.2
        y0 = [990, 10, 0]

        from scipy.integrate import odeint

        from sir_simulator.core_models.sir_model import sir_equations

        result = odeint(sir_equations, y0, t, args=(true_beta, true_gamma))
        observed = result[:, 1] + np.random.normal(0, 5, len(t))
        observed = np.maximum(observed, 0)

        print("Optimizing parameters...")
        optimizer = ParameterOptimizer("sir")
        results = optimizer.fit(observed, t, y0)

        print("\n[SUCCESS] Optimization complete!")
        print("\nRESULTS:")
        print("-" * 30)
        print(f"   Estimated β: {results['beta']:.4f}")
        print(f"   Estimated γ: {results['gamma']:.4f}")
        print(f"   Estimated R0: {results['R0']:.4f}")
        print(f"   R2 (goodness of fit): {results['r_squared']:.4f}")
        print(f"   Final error: {results['final_error']:.4f}")
        print("-" * 30)

        print("\nCOMPARISON WITH TRUE VALUES:")
        print(f"   True β: {true_beta:.2f} -> Estimated: {results['beta']:.4f}")
        print(f"   True γ: {true_gamma:.2f} -> Estimated: {results['gamma']:.4f}")

    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_ml():
    """Run ML prediction"""
    print("\n" + "=" * 50)
    print("MACHINE LEARNING PREDICTION")
    print("=" * 50)
    print("\nNOTE: This requires historical data. Using synthetic data for demo.\n")

    try:
        import numpy as np
        import pandas as pd

        print("Generating synthetic historical data...")

        days = 100
        cases = 10 + np.cumsum(np.random.poisson(0.5, days))
        historical = pd.DataFrame({"day": range(1, days + 1), "cases": cases})

        print("Training model...")
        predictor = EpidemicPredictor("random_forest")
        metrics, predictions, model = predictor.train(historical)

        print("\n[SUCCESS] Training complete!")
        print("\nMODEL PERFORMANCE:")
        print("-" * 30)
        print(f"   R2 score: {metrics['r2']:.4f}")
        print(f"   RMSE: {metrics['rmse']:.4f}")
        print(f"   Training size: {metrics['train_size']}")
        print(f"   Test size: {metrics['test_size']}")
        print("-" * 30)

        print("\nGenerating future predictions...")
        future = predictor.predict_future(historical, days=30)

        print("\nFUTURE PREDICTIONS (next 30 days):")
        print("-" * 30)
        print(f"   Peak predicted: {int(future.max())}")
        print(f"   Average: {future.mean():.1f}")
        print(f"   First 5: {future.head().values}")
        print("-" * 30)

    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_scenarios():
    """Run scenario comparison"""
    print("\n" + "=" * 50)
    print("SCENARIO COMPARISON")
    print("=" * 50)
    print("\nComparing: Baseline vs Quarantine vs Vaccination vs Combined\n")

    try:
        print("Running scenarios...")
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(days=120)

        print("\n[SUCCESS] Comparison complete!")
        print("\nRESULTS:")
        print("-" * 55)
        print(
            f"   {'SCENARIO':<15} {'PEAK INFECTED':<15} {'PEAK DAY':<10} {'REDUCTION'}"
        )
        print("-" * 55)

        for _, row in metrics.iterrows():
            print(
                f"   {row['scenario']:<15} {row['peak_infected']:<15} {row['peak_day']:<10} {row['reduction']}"
            )

        print("-" * 55)

    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_tests():
    """Run all tests"""
    print("\n" + "=" * 50)
    print("RUNNING TEST SUITE")
    print("=" * 50)
    print("\nExecuting all tests (35 unit + 22 security)...\n")

    try:
        import subprocess

        result = subprocess.run(
            [sys.executable, "run_all_tests.py"], capture_output=True, text=True
        )

        if result.returncode == 0:
            print("[SUCCESS] All tests passed successfully!")
        else:
            print("[FAILED] Some tests failed!")

        print("\nTEST OUTPUT:")
        print("-" * 50)
        print(result.stdout)

        if result.stderr:
            print("WARNINGS:")
            print(result.stderr)
        print("-" * 50)

    except Exception as e:
        print(f"\n[ERROR] {e}")


def main():
    """Main interactive menu loop"""
    print("\nWelcome to the SIR Epidemic Simulator!")

    while True:
        print_menu()
        choice = input("\nEnter your choice (0-7): ")

        if choice == "1":
            run_sir()
        elif choice == "2":
            run_seir()
        elif choice == "3":
            run_network()
        elif choice == "4":
            run_optimization()
        elif choice == "5":
            run_ml()
        elif choice == "6":
            run_scenarios()
        elif choice == "7":
            run_tests()
        elif choice == "0":
            print("\n" + "=" * 40)
            print("Thank you for using SIR Epidemic Simulator!")
            print("Stay safe and healthy!")
            print("=" * 40)
            break
        else:
            print("\n[ERROR] Invalid choice! Please enter a number between 0 and 7.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
