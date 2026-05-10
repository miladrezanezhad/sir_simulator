"""
🦠 Streamlit Dashboard for SIR Epidemic Simulator
==================================================
Interactive web application for epidemic modeling
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from sir_simulator.advanced_features.parameter_optimization import ParameterOptimizer
from sir_simulator.advanced_features.scenario_comparison import ScenarioComparator
from sir_simulator.core_models.network_model import SocialNetworkSimulator
from sir_simulator.core_models.seir_model import run_seir_simulation
from sir_simulator.core_models.sir_model import run_sir_simulation

# Page configuration
st.set_page_config(
    page_title="🦠 SIR Epidemic Simulator",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown(
    """
<style>
    .main-header {
        font-size: 2.5rem;
        text-align: center;
        color: #2c3e50;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    '<p class="main-header">🦠 SIR Epidemic Simulator</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">📊 A complete epidemic modeling suite with SIR/SEIR models, network simulation, ML prediction, and scenario comparison</p>',
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.markdown("## 🎛️ Control Panel")
st.sidebar.markdown("---")

model_type = st.sidebar.selectbox(
    "📋 Select Model",
    [
        "📈 SIR Model",
        "🧬 SEIR Model",
        "🌐 Network Simulation",
        "🎯 Parameter Optimization",
        "⚖️ Scenario Comparison",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Tip:** Adjust parameters and click the run button to see results in real-time."
)
st.sidebar.markdown("---")
st.sidebar.markdown("🔬 Built with ❤️ for epidemic research")

# ============================================================================
# SIR MODEL
# ============================================================================
if model_type == "📈 SIR Model":
    st.markdown("## 📈 SIR Model Simulation")
    st.markdown("🟢 **Susceptible** → 🔴 **Infected** → 🔵 **Recovered**")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🦠 Disease Parameters")
        beta = st.slider(
            "📈 Infection Rate (β)",
            0.0,
            1.0,
            0.5,
            0.01,
            help="Rate at which susceptible individuals become infected",
        )
        gamma = st.slider(
            "💊 Recovery Rate (γ)",
            0.0,
            1.0,
            0.2,
            0.01,
            help="Rate at which infected individuals recover",
        )

        st.markdown("### 👥 Population Parameters")
        S0 = st.number_input(
            "🟢 Initial Susceptible",
            0,
            10000,
            990,
            help="Number of susceptible individuals at start",
        )
        I0 = st.number_input(
            "🔴 Initial Infected",
            0,
            1000,
            10,
            help="Number of infected individuals at start",
        )

    with col2:
        st.markdown("### ⏱️ Simulation Parameters")
        t_max = st.slider(
            "📅 Time Range (days)",
            10,
            500,
            100,
            help="Total simulation duration in days",
        )
        steps = st.slider(
            "🔢 Number of Steps",
            100,
            2000,
            500,
            help="Number of time points for calculation",
        )
        R0 = st.number_input(
            "🔵 Initial Recovered",
            0,
            1000,
            0,
            help="Number of recovered individuals at start",
        )

        if beta > 0 and gamma > 0:
            r0_value = beta / gamma
            st.metric(
                "📊 Basic Reproduction Number (R₀)",
                f"{r0_value:.2f}",
                delta=">1 (outbreak)" if r0_value > 1 else "<1 (contained)",
                delta_color="inverse" if r0_value > 1 else "off",
            )

    if st.button("🚀 Run SIR Simulation", type="primary", use_container_width=True):
        with st.spinner("🔄 Running simulation..."):
            df = run_sir_simulation(beta, gamma, S0, I0, R0, t_max, steps)

            # Plot
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(
                df["time"],
                df["Susceptible"],
                label="🟢 Susceptible",
                color="#2ecc71",
                linewidth=2,
            )
            ax.plot(
                df["time"],
                df["Infected"],
                label="🔴 Infected",
                color="#e74c3c",
                linewidth=2,
            )
            ax.plot(
                df["time"],
                df["Recovered"],
                label="🔵 Recovered",
                color="#3498db",
                linewidth=2,
            )
            ax.fill_between(df["time"], 0, df["Infected"], alpha=0.2, color="#e74c3c")
            ax.set_xlabel("📅 Time (days)", fontsize=12)
            ax.set_ylabel("👥 Population", fontsize=12)
            ax.set_title(
                "📈 SIR Epidemic Model Dynamics", fontsize=14, fontweight="bold"
            )
            ax.legend(loc="upper right", fontsize=11)
            ax.grid(True, alpha=0.3)
            ax.set_facecolor("#f8f9fa")
            st.pyplot(fig)

            # Metrics
            st.markdown("### 📊 Key Metrics")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🔴 Peak Infected", f"{int(df['Infected'].max()):,}")
            with col2:
                st.metric("📅 Peak Day", f"{int(df['Infected'].idxmax())}")
            with col3:
                st.metric("📈 Final R₀", f"{beta/gamma:.2f}")
            with col4:
                st.metric(
                    "🟢 Final Susceptible", f"{int(df['Susceptible'].iloc[-1]):,}"
                )

            # Data preview
            with st.expander("📋 View Data Preview"):
                st.dataframe(df.tail(10))
                csv = df.to_csv(index=False)
                st.download_button("💾 Download CSV", csv, "sir_output.csv", "text/csv")

# ============================================================================
# SEIR MODEL
# ============================================================================
elif model_type == "🧬 SEIR Model":
    st.markdown("## 🧬 SEIR Model Simulation (with Exposed Compartment)")
    st.markdown(
        "🟢 **Susceptible** → 🟡 **Exposed** → 🔴 **Infected** → 🔵 **Recovered**"
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🦠 Disease Parameters")
        beta = st.slider("📈 Infection Rate (β)", 0.0, 1.0, 0.5, 0.01)
        sigma = st.slider(
            "⏱️ Incubation Rate (σ)",
            0.0,
            1.0,
            0.2,
            0.01,
            help="Rate at which exposed become infectious (1/incubation period)",
        )
        gamma = st.slider("💊 Recovery Rate (γ)", 0.0, 1.0, 0.1, 0.01)

        st.markdown("### 👥 Population Parameters")
        S0 = st.number_input("🟢 Initial Susceptible", 0, 10000, 990)

    with col2:
        st.markdown("### 🧑‍🤝‍🧑 Initial Conditions")
        E0 = st.number_input("🟡 Initial Exposed", 0, 1000, 5)
        I0 = st.number_input("🔴 Initial Infected", 0, 1000, 5)
        t_max = st.slider("📅 Time Range (days)", 10, 500, 100)
        steps = st.slider("🔢 Number of Steps", 100, 2000, 500)

    if st.button("🧬 Run SEIR Simulation", type="primary", use_container_width=True):
        with st.spinner("🔄 Running simulation..."):
            df = run_seir_simulation(beta, sigma, gamma, S0, E0, I0, 0, t_max, steps)

            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(
                df["time"],
                df["Susceptible"],
                label="🟢 Susceptible",
                color="#2ecc71",
                linewidth=2,
            )
            ax.plot(
                df["time"],
                df["Exposed"],
                label="🟡 Exposed",
                color="#f39c12",
                linewidth=2,
            )
            ax.plot(
                df["time"],
                df["Infected"],
                label="🔴 Infected",
                color="#e74c3c",
                linewidth=2,
            )
            ax.plot(
                df["time"],
                df["Recovered"],
                label="🔵 Recovered",
                color="#3498db",
                linewidth=2,
            )
            ax.fill_between(df["time"], 0, df["Infected"], alpha=0.15, color="#e74c3c")
            ax.set_xlabel("📅 Time (days)", fontsize=12)
            ax.set_ylabel("👥 Population", fontsize=12)
            ax.set_title(
                "🧬 SEIR Epidemic Model Dynamics", fontsize=14, fontweight="bold"
            )
            ax.legend(loc="upper right", fontsize=11)
            ax.grid(True, alpha=0.3)
            ax.set_facecolor("#f8f9fa")
            st.pyplot(fig)

            st.markdown("### 📊 Key Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🔴 Peak Infected", f"{int(df['Infected'].max()):,}")
            with col2:
                st.metric("🟡 Peak Exposed", f"{int(df['Exposed'].max()):,}")
            with col3:
                st.metric("📈 R₀", f"{beta/gamma:.2f}")

            with st.expander("📋 View Data Preview"):
                st.dataframe(df.tail(10))

# ============================================================================
# NETWORK SIMULATION
# ============================================================================
elif model_type == "🌐 Network Simulation":
    st.markdown("## 🌐 Social Network Simulation (Fake News Spread)")
    st.markdown(
        "📡 Simulate how information (or misinformation) spreads through a social network"
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🌍 Network Configuration")
        num_nodes = st.number_input(
            "👥 Number of Nodes", 50, 2000, 200, help="Number of people in the network"
        )
        network_type = st.selectbox(
            "🕸️ Network Type",
            ["scale_free", "small_world", "random"],
            help="Scale-free: power law distribution | Small-world: high clustering | Random: Erdős–Rényi",
        )
        transmission_prob = st.slider(
            "📡 Transmission Probability",
            0.0,
            1.0,
            0.3,
            help="Probability of spreading to a neighbor",
        )

    with col2:
        st.markdown("### 🩺 Spread Parameters")
        recovery_prob = st.slider(
            "💊 Recovery Probability",
            0.0,
            1.0,
            0.1,
            help="Probability of recovering at each step",
        )
        initial_infected = st.number_input("🦠 Initial Infected", 1, 50, 5)
        max_steps = st.slider("⏰ Max Steps", 10, 200, 50)

    if st.button("🌐 Run Network Simulation", type="primary", use_container_width=True):
        with st.spinner("🏗️ Building network and simulating..."):
            sim = SocialNetworkSimulator(num_nodes, network_type)
            stats = sim.get_network_stats()

            st.markdown("### 📊 Network Statistics")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🔘 Nodes", stats["nodes"])
            with col2:
                st.metric("🔗 Edges", stats["edges"])
            with col3:
                st.metric("📈 Avg Degree", f"{stats['avg_degree']:.2f}")
            with col4:
                st.metric("🕸️ Density", f"{stats['density']:.4f}")

            df = sim.simulate_spread(
                transmission_prob, recovery_prob, initial_infected, max_steps
            )

            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(
                df["step"],
                df["susceptible"],
                label="🟢 Susceptible",
                color="#2ecc71",
                linewidth=2,
            )
            ax.plot(
                df["step"],
                df["infected"],
                label="🔴 Infected",
                color="#e74c3c",
                linewidth=2,
            )
            ax.plot(
                df["step"],
                df["recovered"],
                label="🔵 Recovered",
                color="#3498db",
                linewidth=2,
            )
            ax.fill_between(df["step"], 0, df["infected"], alpha=0.2, color="#e74c3c")
            ax.set_xlabel("⏰ Step", fontsize=12)
            ax.set_ylabel("👥 Number of Nodes", fontsize=12)
            ax.set_title(
                "🌐 Fake News Spread on Social Network", fontsize=14, fontweight="bold"
            )
            ax.legend(loc="upper right", fontsize=11)
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

            with st.expander("📋 View Data Preview"):
                st.dataframe(df.tail(10))

# ============================================================================
# PARAMETER OPTIMIZATION
# ============================================================================
elif model_type == "🎯 Parameter Optimization":
    st.markdown("## 🎯 Parameter Optimization (Fit to Real Data)")
    st.markdown("📊 Fit SIR model parameters to observed epidemic data")
    st.markdown("---")

    st.info(
        "💡 **Demo Mode:** Using synthetic data generated from a real SIR model with noise. Upload your own CSV file for real data."
    )

    model_type_opt = st.selectbox("📋 Model Type", ["SIR", "SEIR"])

    use_synthetic = st.checkbox("🔄 Use synthetic data", value=True)

    uploaded_file = None
    if not use_synthetic:
        uploaded_file = st.file_uploader("📁 Upload CSV file", type=["csv"])
        st.caption("CSV should contain 'day' and 'cases' columns")

    if st.button("🎯 Optimize Parameters", type="primary", use_container_width=True):
        with st.spinner("🔍 Optimizing parameters..."):
            if use_synthetic:
                from sir_simulator.advanced_features.parameter_optimization import (
                    generate_synthetic_data,
                )

                t = np.linspace(0, 100, 100)
                t, observed, true = generate_synthetic_data(noise_level=5)
                st.success("✅ Using synthetic data")
            elif uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                observed = df["cases"].values
                t = (
                    df["day"].values
                    if "day" in df.columns
                    else np.arange(len(observed))
                )

            optimizer = ParameterOptimizer(model_type="sir")
            results = optimizer.fit(observed, t, [990, 10, 0])

            st.markdown("### 📊 Optimization Results")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🦠 β (Infection Rate)", f"{results['beta']:.4f}")
            with col2:
                st.metric("💊 γ (Recovery Rate)", f"{results['gamma']:.4f}")
            with col3:
                st.metric("📈 R₀", f"{results['R0']:.4f}")

            st.metric("⭐ R² (Goodness of Fit)", f"{results['r_squared']:.4f}")

            fig, ax = plt.subplots(figsize=(12, 6))
            ax.scatter(
                t, observed, alpha=0.5, s=20, color="#e74c3c", label="📊 Observed Data"
            )
            ax.plot(
                t, results["fitted_curve"], "b-", linewidth=2, label="📈 Fitted Model"
            )
            ax.set_xlabel("📅 Time", fontsize=12)
            ax.set_ylabel("🦠 Infected Cases", fontsize=12)
            ax.set_title(
                "🎯 Parameter Optimization Results", fontsize=14, fontweight="bold"
            )
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

# ============================================================================
# SCENARIO COMPARISON
# ============================================================================
elif model_type == "⚖️ Scenario Comparison":
    st.markdown("## ⚖️ Scenario Comparison: Quarantine vs Vaccination")
    st.markdown("📊 Evaluate the effectiveness of different intervention strategies")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🦠 Disease Parameters")
        beta = st.slider("📈 Infection Rate (β)", 0.1, 0.8, 0.25, 0.01)
        gamma = st.slider("💊 Recovery Rate (γ)", 0.05, 0.3, 0.1, 0.01)

    with col2:
        st.markdown("### ⏱️ Simulation Settings")
        days = st.slider("📅 Simulation Days", 50, 200, 120)

    if st.button("⚖️ Compare Scenarios", type="primary", use_container_width=True):
        with st.spinner("🔄 Running scenarios..."):
            comp = ScenarioComparator(
                population=1000, initial_infected=5, beta=beta, gamma=gamma
            )
            scenarios, metrics = comp.compare_all_scenarios(days)

            st.markdown("### 📊 Comparison Metrics")

            # Color-coded metrics display
            for _, row in metrics.iterrows():
                col1, col2, col3, col4 = st.columns(4)
                icon = (
                    "🔵"
                    if row["scenario"] == "Baseline"
                    else (
                        "🟢"
                        if row["scenario"] == "Quarantine"
                        else "🟠" if row["scenario"] == "Vaccination" else "🔴"
                    )
                )
                with col1:
                    st.metric(f"{icon} {row['scenario']}", row["peak_infected"])
                with col2:
                    st.metric("📅 Peak Day", row["peak_day"])
                with col3:
                    st.metric("📉 Reduction", row["reduction"])

            # Plot
            fig, ax = plt.subplots(figsize=(12, 6))
            colors = {
                "Baseline": "#3498db",
                "Quarantine": "#2ecc71",
                "Vaccination": "#f39c12",
                "Combined": "#e74c3c",
            }
            line_styles = {
                "Baseline": "-",
                "Quarantine": "--",
                "Vaccination": "-.",
                "Combined": ":",
            }

            for name, df in scenarios.items():
                ax.plot(
                    df["day"],
                    df["infected"],
                    label=name,
                    color=colors.get(name, "#95a5a6"),
                    linestyle=line_styles.get(name, "-"),
                    linewidth=2,
                )

            ax.set_xlabel("📅 Day", fontsize=12)
            ax.set_ylabel("🦠 Infected Population", fontsize=12)
            ax.set_title(
                "⚖️ Epidemic Scenario Comparison", fontsize=14, fontweight="bold"
            )
            ax.legend(loc="upper right", fontsize=11)
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
