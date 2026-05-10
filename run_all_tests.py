#!/usr/bin/env python3
"""
Run all test suites for SIR Epidemic Simulator
"""

import os
import sys
import unittest


def run_all_tests():
    """Discover and run all tests in the tests directory"""

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir="tests", pattern="test_*.py")

    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    print("\n" + "=" * 60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 60)

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
