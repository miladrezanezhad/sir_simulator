#!/usr/bin/env python3
"""
SIR Epidemic Simulator - Main Entry Point
"""

import sys
import os
import subprocess

def show_menu():
    print("\n" + "="*60)
    print("🦠 SIR EPIDEMIC SIMULATOR")
    print("="*60)
    print("\nSelect an option:")
    print("1. 🎨 Launch Streamlit Dashboard")
    print("2. 💻 Run CLI Simulation")
    print("3. 🧪 Run All Tests")
    print("4. 🏥 Run Scenario Comparison Demo")
    print("5. 🤖 Run ML Prediction Demo")
    print("6. 🌐 Run Network Simulation Demo")
    print("7. ❌ Exit")
    
    return input("\nEnter your choice (1-7): ").strip()

def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            subprocess.run([sys.executable, "-m", "streamlit", "run", "user_interface/app.py"])
        elif choice == '2':
            subprocess.run([sys.executable, "user_interface/cli.py", "--help"])
        elif choice == '3':
            subprocess.run([sys.executable, "run_all_tests.py"])
        elif choice == '4':
            subprocess.run([sys.executable, "advanced_features/scenario_comparison.py"])
        elif choice == '5':
            subprocess.run([sys.executable, "advanced_features/ml_prediction.py"])
        elif choice == '6':
            subprocess.run([sys.executable, "core_models/network_model.py"])
        elif choice == '7':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice.")

if __name__ == "__main__":
    main()