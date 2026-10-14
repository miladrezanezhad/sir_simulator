"""
SIR Epidemic Model
==================
Classic SIR (Susceptible-Infected-Recovered) model
"""

import numpy as np
import pandas as pd
from scipy.integrate import odeint


def sir_equations(y, t, beta, gamma):
    """SIR differential equations"""
    S, I, R = y
    N = S + I + R
    if N <= 0:
        return [0.0, 0.0, 0.0]
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]


def run_sir_simulation(beta, gamma, S0, I0, R0, t_max, steps=500):
    """
    Run SIR simulation

    Parameters:
    - beta: infection rate
    - gamma: recovery rate
    - S0, I0, R0: initial populations
    - t_max: maximum time
    - steps: number of time steps

    Returns:
    - DataFrame with time, Susceptible, Infected, Recovered
    """
    t = np.linspace(0, t_max, steps)
    y0 = [S0, I0, R0]
    result = odeint(sir_equations, y0, t, args=(beta, gamma))

    df = pd.DataFrame(
        {
            "time": t,
            "Susceptible": result[:, 0],
            "Infected": result[:, 1],
            "Recovered": result[:, 2],
        }
    )
    return df


if __name__ == "__main__":
    df = run_sir_simulation(0.5, 0.2, 990, 10, 0, 100, 500)
    print(df.tail())
