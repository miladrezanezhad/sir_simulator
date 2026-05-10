"""
Parameter Optimization with Real Data
=====================================
Fit SIR/SEIR model parameters to observed data
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize, differential_evolution
import pandas as pd

from core_models.sir_model import sir_equations
from core_models.seir_model import seir_equations

class ParameterOptimizer:
    """
    Optimize SIR/SEIR model parameters to fit real-world data
    """
    
    def __init__(self, model_type='sir'):
        self.model_type = model_type
        self.fitted_params = None
        self.fitted_model = None
        
    def simulate(self, params, t, initial_conditions):
        """Run simulation with given parameters"""
        if self.model_type == 'sir':
            beta, gamma = params
            result = odeint(sir_equations, initial_conditions, t, args=(beta, gamma))
            return result[:, 1]
        else:
            beta, sigma, gamma = params
            result = odeint(seir_equations, initial_conditions, t, args=(beta, sigma, gamma))
            return result[:, 2]
    
    def cost_function(self, params, t, real_data, initial_conditions):
        """Calculate error between simulation and real data"""
        try:
            simulated = self.simulate(params, t, initial_conditions)
            mse = np.mean((simulated - real_data) ** 2)
            
            if self.model_type == 'sir':
                beta, gamma = params
                if beta < 0 or gamma < 0 or beta > 2 or gamma > 1:
                    return 1e10
            else:
                beta, sigma, gamma = params
                if beta < 0 or sigma < 0 or gamma < 0 or beta > 2 or sigma > 1 or gamma > 1:
                    return 1e10
                    
            return mse
        except:
            return 1e10
    
    def fit(self, real_data, t, initial_conditions, method='differential_evolution'):
        """Fit model parameters to real data"""
        if self.model_type == 'sir':
            bounds = [(0.01, 2.0), (0.01, 1.0)]
            initial_guess = [0.5, 0.2]
        else:
            bounds = [(0.01, 2.0), (0.01, 1.0), (0.01, 1.0)]
            initial_guess = [0.5, 0.2, 0.1]
        
        if method == 'differential_evolution':
            result = differential_evolution(
                self.cost_function,
                bounds,
                args=(t, real_data, initial_conditions),
                maxiter=100,
                popsize=15,
                seed=42
            )
            self.fitted_params = result.x
        else:
            result = minimize(
                self.cost_function,
                initial_guess,
                args=(t, real_data, initial_conditions),
                method='L-BFGS-B',
                bounds=bounds
            )
            self.fitted_params = result.x
        
        fitted_curve = self.simulate(self.fitted_params, t, initial_conditions)
        
        ss_res = np.sum((real_data - fitted_curve) ** 2)
        ss_tot = np.sum((real_data - np.mean(real_data)) ** 2)
        r_squared = 1 - (ss_res / ss_tot)
        
        if self.model_type == 'sir':
            results = {
                'beta': self.fitted_params[0],
                'gamma': self.fitted_params[1],
                'R0': self.fitted_params[0] / self.fitted_params[1],
                'final_error': result.fun,
                'r_squared': r_squared,
                'fitted_curve': fitted_curve
            }
        else:
            results = {
                'beta': self.fitted_params[0],
                'sigma': self.fitted_params[1],
                'gamma': self.fitted_params[2],
                'R0': self.fitted_params[0] / self.fitted_params[2],
                'incubation_period': 1 / self.fitted_params[1],
                'infectious_period': 1 / self.fitted_params[2],
                'final_error': result.fun,
                'r_squared': r_squared,
                'fitted_curve': fitted_curve
            }
        
        self.fitted_model = results
        return results

def generate_synthetic_data(true_beta=0.5, true_gamma=0.2, 
                           S0=990, I0=10, R0=0, 
                           t_max=100, noise_level=5):
    """Generate synthetic epidemic data for testing"""
    t = np.linspace(0, t_max, t_max)
    y0 = [S0, I0, R0]
    result = odeint(sir_equations, y0, t, args=(true_beta, true_gamma))
    
    noisy_data = result[:, 1] + np.random.normal(0, noise_level, len(t))
    noisy_data = np.maximum(noisy_data, 0)
    
    return t, noisy_data, result[:, 1]

if __name__ == "__main__":
    t, data, true = generate_synthetic_data()
    optimizer = ParameterOptimizer('sir')
    results = optimizer.fit(data, t, [990, 10, 0])
    print(f"Estimated: β={results['beta']:.3f}, γ={results['gamma']:.3f}")
    print(f"R² = {results['r_squared']:.3f}")