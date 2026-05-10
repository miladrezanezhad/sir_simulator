"""
SEIR Epidemic Model
===================
SEIR (Susceptible-Exposed-Infected-Recovered) model with incubation period
"""

import numpy as np
import pandas as pd
from scipy.integrate import odeint


def seir_equations(y, t, beta, sigma, gamma):
    """SEIR differential equations"""
    S, E, I, R = y
    N = S + E + I + R
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]


def run_seir_simulation(beta, sigma, gamma, S0, E0, I0, R0, t_max, steps=500):
    """
    Run SEIR simulation

    Parameters:
    - beta: infection rate
    - sigma: incubation rate (1/incubation_period)
    - gamma: recovery rate
    - S0, E0, I0, R0: initial populations
    - t_max: maximum time
    - steps: number of time steps

    Returns:
    - DataFrame with time, Susceptible, Exposed, Infected, Recovered
    """
    t = np.linspace(0, t_max, steps)
    y0 = [S0, E0, I0, R0]
    result = odeint(seir_equations, y0, t, args=(beta, sigma, gamma))

    df = pd.DataFrame(
        {
            "time": t,
            "Susceptible": result[:, 0],
            "Exposed": result[:, 1],
            "Infected": result[:, 2],
            "Recovered": result[:, 3],
        }
    )
    return df


if __name__ == "__main__":
    df = run_seir_simulation(0.5, 0.2, 0.1, 990, 5, 5, 0, 100, 500)
    print(df.tail())
