"""
Advanced Features Module

Contains:
- Parameter Optimization
- Machine Learning Prediction
- Scenario Comparison
"""

from .ml_prediction import EpidemicPredictor
from .parameter_optimization import ParameterOptimizer, generate_synthetic_data
from .scenario_comparison import ScenarioComparator

__all__ = [
    "ParameterOptimizer",
    "generate_synthetic_data",
    "EpidemicPredictor",
    "generate_training_data",
    "ScenarioComparator",
]
