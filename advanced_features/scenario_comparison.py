"""
Scenario Comparison: Quarantine vs Vaccination
===============================================
Compare different intervention strategies
"""

import numpy as np
from scipy.integrate import odeint
import pandas as pd
import matplotlib.pyplot as plt

class ScenarioComparator:
    """
    Compare different intervention scenarios for epidemic control
    """
    
    def __init__(self, population=1000, initial_infected=5, beta=0.25, gamma=0.1):
        self.population = population
        self.initial_infected = initial_infected
        self.beta = beta
        self.gamma = gamma
        self.initial_conditions = [population - initial_infected, initial_infected, 0]
        
    def sir_model(self, y, t, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / self.population
        dIdt = beta * S * I / self.population - gamma * I
        dRdt = gamma * I
        return [dSdt, dIdt, dRdt]
    
    def baseline_scenario(self, days=150):
        t = np.linspace(0, days, days)
        result = odeint(self.sir_model, self.initial_conditions, t, args=(self.beta, self.gamma))
        return pd.DataFrame({'day': t, 'susceptible': result[:, 0], 'infected': result[:, 1], 'recovered': result[:, 2]})
    
    def quarantine_scenario(self, days=150, start_day=10, end_day=80, reduction_factor=0.2):
        def sir_quarantine(y, t, beta, gamma):
            S, I, R = y
            effective_beta = beta * reduction_factor if start_day <= t <= end_day else beta
            dSdt = -effective_beta * S * I / self.population
            dIdt = effective_beta * S * I / self.population - gamma * I
            dRdt = gamma * I
            return [dSdt, dIdt, dRdt]
        
        t = np.linspace(0, days, days)
        result = odeint(sir_quarantine, self.initial_conditions, t, args=(self.beta, self.gamma))
        return pd.DataFrame({'day': t, 'susceptible': result[:, 0], 'infected': result[:, 1], 'recovered': result[:, 2]})
    
    def vaccination_scenario(self, days=150, start_day=5, daily_vaccinations=15, vaccine_efficacy=0.9):
        def sir_vaccination(y, t, beta, gamma):
            S, I, R = y
            dSdt = -beta * S * I / self.population
            dIdt = beta * S * I / self.population - gamma * I
            dRdt = gamma * I
            
            if t >= start_day and S > 0:
                vaccinate = min(daily_vaccinations * vaccine_efficacy, S)
                dSdt -= vaccinate
                dRdt += vaccinate
            
            return [dSdt, dIdt, dRdt]
        
        t = np.linspace(0, days, days)
        result = odeint(sir_vaccination, self.initial_conditions, t, args=(self.beta, self.gamma))
        return pd.DataFrame({'day': t, 'susceptible': result[:, 0], 'infected': result[:, 1], 'recovered': result[:, 2]})
    
    def combined_scenario(self, days=150, quarantine_start=10, quarantine_end=80, 
                          quarantine_reduction=0.2, vaccination_start=5, daily_vaccinations=12):
        def sir_combined(y, t, beta, gamma):
            S, I, R = y
            effective_beta = beta * quarantine_reduction if quarantine_start <= t <= quarantine_end else beta
            dSdt = -effective_beta * S * I / self.population
            dIdt = effective_beta * S * I / self.population - gamma * I
            dRdt = gamma * I
            
            if t >= vaccination_start and S > 0:
                vaccinate = min(daily_vaccinations * 0.9, S)
                dSdt -= vaccinate
                dRdt += vaccinate
            
            return [dSdt, dIdt, dRdt]
        
        t = np.linspace(0, days, days)
        result = odeint(sir_combined, self.initial_conditions, t, args=(self.beta, self.gamma))
        return pd.DataFrame({'day': t, 'susceptible': result[:, 0], 'infected': result[:, 1], 'recovered': result[:, 2]})
    
    def compare_all_scenarios(self, days=150):
        scenarios = {
            'Baseline': self.baseline_scenario(days),
            'Quarantine': self.quarantine_scenario(days),
            'Vaccination': self.vaccination_scenario(days),
            'Combined': self.combined_scenario(days)
        }
        
        baseline_peak = scenarios['Baseline']['infected'].max()
        metrics = []
        
        for name, df in scenarios.items():
            peak = df['infected'].max()
            reduction = 0 if name == 'Baseline' else (baseline_peak - peak) / baseline_peak * 100
            metrics.append({
                'scenario': name,
                'peak_infected': int(peak),
                'peak_day': int(df[df['infected'] == peak]['day'].values[0]),
                'reduction': f"{reduction:.1f}%"
            })
        
        return scenarios, pd.DataFrame(metrics)

if __name__ == "__main__":
    comp = ScenarioComparator()
    scenarios, metrics = comp.compare_all_scenarios(120)
    print(metrics)