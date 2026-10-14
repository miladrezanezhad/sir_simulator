"""
SIRS Epidemic Model
===================
SIRS (Susceptible-Infected-Recovered-Susceptible) model
with waning immunity where recovered individuals eventually become susceptible again.
"""

import numpy as np
import pandas as pd
from scipy.integrate import odeint


def sirs_equations(y, t, beta, gamma, xi):
    """
    SIRS differential equations with waning immunity

    Parameters:
    - y: current state [S, I, R]
    - t: current time point
    - beta: infection transmission rate
    - gamma: recovery rate
    - xi: immunity loss rate (1 / immunity duration in days)

    Returns:
    - Derivatives [dSdt, dIdt, dRdt]
    """
    S, I, R = y
    N = S + I + R
    if N <= 0:
        return [0.0, 0.0, 0.0]

    dSdt = -beta * S * I / N + xi * R
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I - xi * R

    return [dSdt, dIdt, dRdt]


def run_sirs_simulation(beta, gamma, xi, S0, I0, R0=0, t_max=150, steps=500):
    """
    Run SIRS simulation

    Parameters:
    - beta: infection rate
    - gamma: recovery rate
    - xi: waning immunity rate (1 / duration_of_immunity)
    - S0, I0, R0: initial populations
    - t_max: maximum time in days
    - steps: number of time steps

    Returns:
    - DataFrame with columns: time, Susceptible, Infected, Recovered
    """
    t = np.linspace(0, t_max, steps)
    y0 = [float(S0), float(I0), float(R0)]

    result = odeint(sirs_equations, y0, t, args=(beta, gamma, xi))

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
    # Immunity lasts on average 60 days (xi = 1/60)
    df = run_sirs_simulation(
        beta=0.4,
        gamma=0.1,
        xi=0.02,
        S0=990,
        I0=10,
        R0=0,
        t_max=200,
        steps=1000,
    )
    print(df.tail())
