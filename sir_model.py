"""
SIR Epidemic Model
==================
Susceptible (S) -> Infected (I) -> Recovered (R)
"""

import numpy as np
from scipy.integrate import odeint
import pandas as pd

def sir_equations(y, t, beta, gamma):
    """
    Differential equations for the SIR model.
    
    Parameters:
    y : list [S, I, R] - current populations
    t : float - time
    beta : float - transmission rate
    gamma : float - recovery rate
    
    Returns:
    list : derivatives [dS/dt, dI/dt, dR/dt]
    """
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

def run_sir_simulation(beta, gamma, S0, I0, R0, t_max, steps):
    """
    Run SIR simulation using numerical integration.
    
    Parameters:
    beta : float - transmission rate (0.1 to 2.0 typical)
    gamma : float - recovery rate (0.05 to 1.0 typical)
    S0 : float - initial susceptible population
    I0 : float - initial infected population
    R0 : float - initial recovered population
    t_max : float - simulation duration (days)
    steps : int - number of time points
    
    Returns:
    pandas.DataFrame : columns: time, Susceptible, Infected, Recovered
    """
    t = np.linspace(0, t_max, steps)
    y0 = [S0, I0, R0]
    
    # Solve ODE system
    result = odeint(sir_equations, y0, t, args=(beta, gamma))
    
    # Create DataFrame
    df = pd.DataFrame({
        'time': t,
        'Susceptible': result[:, 0],
        'Infected': result[:, 1],
        'Recovered': result[:, 2]
    })
    
    return df

def calculate_R0(beta, gamma):
    """Calculate basic reproduction number R₀ = β/γ"""
    return beta / gamma

def calculate_peak_infected(df):
    """Find maximum infected population and time of peak"""
    max_infected = df['Infected'].max()
    peak_time = df[df['Infected'] == max_infected]['time'].values[0]
    return max_infected, peak_time