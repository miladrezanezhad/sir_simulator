#!/usr/bin/env python3
"""
Run all tests for the SIR Simulator
"""

import subprocess
import sys
import os

def run_test(test_file):
    print(f"\n{'='*60}")
    print(f"Running: {test_file}")
    print('='*60)
    result = subprocess.run([sys.executable, test_file], capture_output=False, text=True)
    return result.returncode == 0

def main():
    print("\n" + "="*60)
    print("🧪 SIR SIMULATOR - COMPLETE TEST SUITE")
    print("="*60)
    
    tests = [
        "tests/test_seir.py",
        "tests/test_network.py",
        "tests/test_optimization.py",
        "tests/test_ml.py",
        "tests/test_scenarios.py"
    ]
    
    results = {}
    for test_file in tests:
        if os.path.exists(test_file):
            success = run_test(test_file)
            results[test_file] = success
            if not success:
                print(f"\n❌ Stopped at: {test_file}")
                break
        else:
            print(f"⚠️ File not found: {test_file}")
            results[test_file] = False
    
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    
    all_passed = all(results.values())
    for test, passed in results.items():
        print(f"{'✅' if passed else '❌'} {test}")
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print("\n⚠️ SOME TESTS FAILED!")

if __name__ == "__main__":
    main()