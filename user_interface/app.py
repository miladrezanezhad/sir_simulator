"""
SIR Epidemic Simulator - Streamlit Dashboard
Run with: python -m streamlit run user_interface/app.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from core_models.sir_model import run_sir_simulation, calculate_R0, calculate_peak_infected
from core_models.seir_model import run_seir_simulation
from core_models.network_model import SocialNetworkSimulator
from advanced_features.parameter_optimization import ParameterOptimizer, generate_synthetic_data
from advanced_features.ml_prediction import EpidemicPredictor, generate_training_data
from advanced_features.scenario_comparison import ScenarioComparator

st.set_page_config(page_title="SIR Epidemic Simulator", page_icon="🦠", layout="wide")

st.sidebar.title("🦠 SIR Epidemic Simulator")
st.sidebar.markdown("---")

feature = st.sidebar.selectbox(
    "Select Feature",
    ["🏠 Home", "📊 SIR Model", "🟢 SEIR Model", "🌐 Social Network", 
     "📈 Parameter Optimization", "🤖 ML Prediction", "🏥 Scenario Comparison"]
)

if feature == "🏠 Home":
    st.title("🦠 Epidemic Simulation Suite")
    st.markdown("""
    ## Welcome to the Complete Epidemic Simulator!
    
    ### Available Features:
    - **SIR Model**: Basic Susceptible-Infected-Recovered
    - **SEIR Model**: With Exposed compartment
    - **Social Network**: Fake news spread simulation
    - **Parameter Optimization**: Fit model to real data
    - **ML Prediction**: Forecast future cases
    - **Scenario Comparison**: Quarantine vs Vaccination
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Models", "6", "SIR, SEIR, Network")
    col2.metric("ML Algorithms", "3", "RF, XGBoost, GBM")
    col3.metric("Interventions", "2", "Quarantine, Vaccination")
    col4.metric("Export", "CSV", "Downloadable")

elif feature == "📊 SIR Model":
    st.title("📊 SIR Epidemic Model")
    
    col1, col2 = st.columns(2)
    
    with col1:
        beta = st.slider("Transmission rate (β)", 0.1, 1.5, 0.5, 0.05)
        gamma = st.slider("Recovery rate (γ)", 0.05, 0.5, 0.2, 0.05)
        S0 = st.number_input("Initial Susceptible", 100, 5000, 990)
        I0 = st.number_input("Initial Infected", 1, 100, 10)
    
    with col2:
        t_max = st.slider("Simulation days", 30, 200, 100)
        st.metric("R₀", f"{beta/gamma:.2f}")
        if beta/gamma > 1:
            st.warning("⚠️ R₀ > 1: Epidemic will spread")
        else:
            st.success("✅ R₀ < 1: Disease will die out")
    
    df = run_sir_simulation(beta, gamma, S0, I0, 0, t_max, 500)
    peak, peak_time = calculate_peak_infected(df)
    
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df['time'], df['Susceptible'], label='Susceptible', lw=2)
    ax.plot(df['time'], df['Infected'], label='Infected', lw=2, color='red')
    ax.plot(df['time'], df['Recovered'], label='Recovered', lw=2, color='green')
    ax.axvline(x=peak_time, color='gray', linestyle='--', label=f'Peak: {peak:.0f} at day {peak_time:.1f}')
    ax.set_xlabel("Days")
    ax.set_ylabel("Population")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, "sir_results.csv", "text/csv")

elif feature == "🟢 SEIR Model":
    st.title("🟢 SEIR Model with Exposed Compartment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        beta = st.slider("Transmission (β)", 0.1, 1.5, 0.5, 0.05)
        sigma = st.slider("Incubation rate (σ)", 0.1, 0.5, 0.2, 0.05)
        gamma = st.slider("Recovery rate (γ)", 0.05, 0.5, 0.1, 0.05)
    
    with col2:
        S0 = st.number_input("Susceptible", 100, 5000, 990)
        I0 = st.number_input("Infected", 1, 100, 10)
        t_max = st.slider("Days", 30, 200, 100)
        st.info(f"Incubation period: {1/sigma:.1f} days | Infectious: {1/gamma:.1f} days")
    
    df = run_seir_simulation(beta, sigma, gamma, S0, 0, I0, 0, t_max, 500)
    
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df['time'], df['Susceptible'], label='Susceptible', lw=2)
    ax.plot(df['time'], df['Exposed'], label='Exposed', lw=2, color='orange')
    ax.plot(df['time'], df['Infected'], label='Infected', lw=2, color='red')
    ax.plot(df['time'], df['Recovered'], label='Recovered', lw=2, color='green')
    ax.set_xlabel("Days")
    ax.set_ylabel("Population")
    ax.set_title(f"Peak Infected: {df['Infected'].max():.0f}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, "seir_results.csv", "text/csv")

elif feature == "🌐 Social Network":
    st.title("🌐 Fake News Spread on Social Network")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_nodes = st.slider("Network size", 50, 500, 200)
        network_type = st.selectbox("Network type", ["scale_free", "small_world", "random"])
        transmission_prob = st.slider("Spread probability", 0.1, 0.8, 0.4)
    
    with col2:
        recovery_prob = st.slider("Stop sharing probability", 0.05, 0.3, 0.1)
        initial_spreaders = st.slider("Initial spreaders", 1, 20, 5)
        max_steps = st.slider("Simulation steps", 20, 100, 50)
    
    if st.button("🚀 Run Simulation"):
        with st.spinner("Simulating..."):
            sim = SocialNetworkSimulator(num_nodes, network_type)
            stats = sim.get_network_stats()
            df = sim.simulate_spread(transmission_prob, recovery_prob, initial_spreaders, max_steps)
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Nodes", stats['nodes'])
            col2.metric("Edges", stats['edges'])
            col3.metric("Avg Degree", f"{stats['avg_degree']:.1f}")
            col4.metric("Peak Spreaders", f"{df['infected'].max():.0f}")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(df['step'], df['susceptible'], label='Not seen', lw=2)
            ax.plot(df['step'], df['infected'], label='Spreading', lw=2, color='red')
            ax.plot(df['step'], df['recovered'], label='Stopped', lw=2, color='green')
            ax.set_xlabel("Time steps")
            ax.set_ylabel("Number of people")
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download CSV", csv, "network_results.csv", "text/csv")

elif feature == "📈 Parameter Optimization":
    st.title("📈 Parameter Optimization")
    
    data_source = st.radio("Data source", ["Generate synthetic data", "Upload CSV"])
    
    if data_source == "Generate synthetic data":
        true_beta = st.slider("True β", 0.2, 1.0, 0.5)
        true_gamma = st.slider("True γ", 0.05, 0.3, 0.15)
        
        if st.button("Optimize"):
            t, observed, _ = generate_synthetic_data(true_beta, true_gamma, 1000, 10, 100, 5)
            optimizer = ParameterOptimizer('sir')
            results = optimizer.fit(observed, t, [990, 10, 0])
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Estimated β", f"{results['beta']:.3f}")
            col2.metric("Estimated γ", f"{results['gamma']:.3f}")
            col3.metric("R² Score", f"{results['r_squared']:.3f}")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(t, observed, 'o', alpha=0.5, label='Observed', markersize=3)
            ax.plot(t, results['fitted_curve'], 'r-', label='Fitted', lw=2)
            ax.set_xlabel("Days")
            ax.set_ylabel("Infected")
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

elif feature == "🤖 ML Prediction":
    st.title("🤖 Machine Learning Prediction")
    
    model_type = st.selectbox("ML Model", ["random_forest", "gradient_boosting"])
    lookback = st.slider("Lookback days", 3, 14, 7)
    
    if st.button("Train & Predict"):
        with st.spinner("Training model..."):
            data = generate_training_data()
            predictor = EpidemicPredictor(model_type, lookback)
            metrics, pred, actual = predictor.train(data)
            
            if metrics:
                col1, col2, col3 = st.columns(3)
                col1.metric("Train R²", f"{metrics['train_r2']:.3f}")
                col2.metric("Test R²", f"{metrics['test_r2']:.3f}")
                col3.metric("Test MAE", f"{metrics['test_mae']:.1f}")
                
                future = predictor.predict_future(data, 30)
                
                fig, ax = plt.subplots(figsize=(12, 5))
                ax.plot(data, 'b-', label='Historical', alpha=0.7)
                future_days = range(len(data), len(data) + len(future))
                ax.plot(future_days, future, 'r--', label='Forecast', lw=2)
                ax.set_xlabel("Days")
                ax.set_ylabel("Cases")
                ax.set_title(f"30-Day Forecast (Peak: {future.max():.0f})")
                ax.legend()
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)

elif feature == "🏥 Scenario Comparison":
    st.title("🏥 Scenario Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        quarantine_reduction = st.slider("Quarantine effectiveness", 0.1, 1.0, 0.3)
    with col2:
        vax_rate = st.slider("Vaccination rate (people/day)", 5, 50, 20)
    
    if st.button("Compare"):
        comp = ScenarioComparator()
        scenarios, metrics = comp.compare_all_scenarios(120)
        
        st.dataframe(metrics)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        for name, df in scenarios.items():
            ax.plot(df['day'], df['infected'], label=name, lw=2)
        ax.set_xlabel("Days")
        ax.set_ylabel("Infected")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)