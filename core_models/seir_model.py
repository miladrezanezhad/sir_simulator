"""
SEIR Epidemic Model
===================
Susceptible (S) -> Exposed (E) -> Infected (I) -> Recovered (R)
"""

import numpy as np
from scipy.integrate import odeint
import pandas as pd

def seir_equations(y, t, beta, sigma, gamma):
    """
    SEIR model differential equations.
    
    S -> E -> I -> R
    """
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

def run_seir_simulation(beta, sigma, gamma, S0, E0, I0, R0, t_max, steps):
    """
    Run SEIR simulation.
    
    Parameters:
    - beta: transmission rate
    - sigma: incubation rate (1/incubation period)
    - gamma: recovery rate
    - S0, E0, I0, R0: initial populations
    - t_max: simulation days
    - steps: number of time points
    """
    t = np.linspace(0, t_max, steps)
    y0 = [S0, E0, I0, R0]
    
    result = odeint(seir_equations, y0, t, args=(beta, sigma, gamma))
    
    df = pd.DataFrame({
        'time': t,
        'Susceptible': result[:, 0],
        'Exposed': result[:, 1],
        'Infected': result[:, 2],
        'Recovered': result[:, 3]
    })
    
    return df

def calculate_seir_stats(df):
    """Calculate key statistics from SEIR simulation"""
    return {
        'peak_infected': df['Infected'].max(),
        'peak_exposed': df['Exposed'].max(),
        'peak_time': df[df['Infected'] == df['Infected'].max()]['time'].values[0],
        'final_recovered': df['Recovered'].iloc[-1]
    }

if __name__ == "__main__":
    df = run_seir_simulation(0.5, 0.2, 0.1, 990, 0, 10, 0, 100, 500)
    print(df.head())
    print(calculate_seir_stats(df))