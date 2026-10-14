"""
SEIRD Epidemic Model
====================
SEIRD (Susceptible-Exposed-Infected-Recovered-Deceased) model
incorporating disease mortality and incubation dynamics.
"""

import numpy as np
import pandas as pd
from scipy.integrate import odeint


def seird_equations(y, t, beta, sigma, gamma, mu):
    """
    SEIRD differential equations

    Parameters:
    - y: current state [S, E, I, R, D]
    - t: current time point
    - beta: infection transmission rate
    - sigma: incubation rate (1 / incubation period)
    - gamma: recovery rate
    - mu: disease-induced mortality rate

    Returns:
    - Derivatives [dSdt, dEdt, dIdt, dRdt, dDdt]
    """
    S, E, I, R, D = y
    N = S + E + I + R + D
    if N <= 0:
        return [0.0, 0.0, 0.0, 0.0, 0.0]

    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - (gamma + mu) * I
    dRdt = gamma * I
    dDdt = mu * I

    return [dSdt, dEdt, dIdt, dRdt, dDdt]


def run_seird_simulation(
    beta, sigma, gamma, mu, S0, E0, I0, R0=0, D0=0, t_max=100, steps=500
):
    """
    Run SEIRD simulation

    Parameters:
    - beta: infection rate
    - sigma: incubation rate (1/incubation_period)
    - gamma: recovery rate
    - mu: mortality rate
    - S0, E0, I0, R0, D0: initial populations
    - t_max: maximum time in days
    - steps: number of time steps

    Returns:
    - DataFrame with columns: time, Susceptible, Exposed, Infected, Recovered, Deceased
    """
    t = np.linspace(0, t_max, steps)
    y0 = [float(S0), float(E0), float(I0), float(R0), float(D0)]

    result = odeint(seird_equations, y0, t, args=(beta, sigma, gamma, mu))

    df = pd.DataFrame(
        {
            "time": t,
            "Susceptible": result[:, 0],
            "Exposed": result[:, 1],
            "Infected": result[:, 2],
            "Recovered": result[:, 3],
            "Deceased": result[:, 4],
        }
    )
    return df


if __name__ == "__main__":
    df = run_seird_simulation(
        beta=0.5,
        sigma=0.2,
        gamma=0.1,
        mu=0.02,
        S0=980,
        E0=10,
        I0=10,
        R0=0,
        D0=0,
        t_max=100,
        steps=500,
    )
    print(df.tail())
