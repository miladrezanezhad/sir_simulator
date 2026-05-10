"""
SIR Model Interactive Dashboard
Run with: streamlit run app.py
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os
from sir_model import run_sir_simulation, calculate_R0, calculate_peak_infected

# Page configuration
st.set_page_config(
    page_title="SIR Epidemic Simulator",
    page_icon="🦠",
    layout="wide"
)

# Title and description
st.title("🦠 SIR Epidemic Simulation")
st.markdown("""
This dashboard simulates the spread of an infectious disease using the **SIR model**.
- **S** = Susceptible (healthy but can catch the disease)
- **I** = Infected (sick and contagious)
- **R** = Recovered (immune)
""")

# Sidebar for parameters
st.sidebar.header("Parameters")

beta = st.sidebar.slider(
    "Transmission rate (β)", 
    min_value=0.1, 
    max_value=2.0, 
    value=0.5, 
    step=0.05,
    help="Higher values = faster spread"
)

gamma = st.sidebar.slider(
    "Recovery rate (γ)", 
    min_value=0.05, 
    max_value=1.0, 
    value=0.2, 
    step=0.05,
    help="Higher values = faster recovery"
)

col1, col2, col3 = st.sidebar.columns(3)
with col1:
    S0 = st.number_input("Initial Susceptible", value=990, min_value=0, max_value=10000)
with col2:
    I0 = st.number_input("Initial Infected", value=10, min_value=0, max_value=1000)
with col3:
    R0 = st.number_input("Initial Recovered", value=0, min_value=0, max_value=1000)

t_max = st.sidebar.slider("Simulation duration (days)", 10, 200, 100)
steps = st.sidebar.slider("Number of time points", 100, 1000, 500)

# Calculate total population and R0
total_pop = S0 + I0 + R0
R0_value = calculate_R0(beta, gamma)

# Display metrics in main area
st.subheader("📊 Key Metrics")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
metric_col1.metric("Total Population", f"{total_pop:,.0f}")
metric_col2.metric("Basic Reproduction Number (R₀)", f"{R0_value:.2f}")
metric_col3.metric("Transmission Rate (β)", f"{beta:.2f}")
metric_col4.metric("Recovery Rate (γ)", f"{gamma:.2f}")

# Run simulation
df = run_sir_simulation(beta, gamma, S0, I0, R0, t_max, steps)

# Calculate peak statistics
peak_infected, peak_time = calculate_peak_infected(df)

st.subheader(f"📈 Simulation Results (Peak: {peak_infected:.0f} infected at day {peak_time:.1f})")

# Plot results
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df['time'], df['Susceptible'], label='Susceptible (S)', lw=2, color='blue')
ax.plot(df['time'], df['Infected'], label='Infected (I)', lw=2, color='red')
ax.plot(df['time'], df['Recovered'], label='Recovered (R)', lw=2, color='green')

ax.fill_between(df['time'], 0, df['Infected'], alpha=0.3, color='red')
ax.axvline(x=peak_time, color='gray', linestyle='--', alpha=0.7, label=f'Peak at day {peak_time:.1f}')

ax.set_xlabel("Time (days)", fontsize=12)
ax.set_ylabel("Population", fontsize=12)
ax.set_title("SIR Model Disease Progression", fontsize=14)
ax.legend(loc='best', fontsize=10)
ax.grid(True, alpha=0.3)

st.pyplot(fig)

# Data preview
st.subheader("📋 Data Preview")
st.dataframe(df.tail(10))

# Download buttons
col_download1, col_download2 = st.columns(2)

with col_download1:
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"sir_simulation_beta{beta}_gamma{gamma}.csv",
        mime="text/csv"
    )

with col_download2:
    # Save to local folder option
    if st.button("💾 Save to outputs folder"):
        os.makedirs("outputs", exist_ok=True)
        path = f"outputs/sir_sim_{beta}_{gamma}_{t_max}days.csv"
        df.to_csv(path, index=False)
        st.success(f"Saved to {path}")

# Interpretation guide
with st.expander("📖 How to interpret the results?"):
    st.markdown("""
    - **If R₀ > 1**: The disease will spread through the population (epidemic)
    - **If R₀ = 1**: The disease becomes endemic (stable)
    - **If R₀ < 1**: The disease will die out
    
    **Peak infected** shows the maximum number of simultaneous infections.
    **Time to peak** helps with healthcare capacity planning.
    """)