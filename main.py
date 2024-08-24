import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Set page config
st.set_page_config(page_title="Sample Streamlit App", page_icon=":chart_with_upwards_trend:", layout="wide")

# Add custom CSS to use a good font
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display a title and message
st.title("Your Sample App is Running .. Yay !!")
st.write("This app displays a Plotly graph of a Gaussian distribution.")

# Generate data for Gaussian distribution
mean = 0
std_dev = 1
x = np.linspace(-5, 5, 100)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# Create a Plotly figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Gaussian Distribution'))

fig.update_layout(
    title="Gaussian Distribution",
    xaxis_title="X",
    yaxis_title="Probability Density",
    template="plotly_dark"
)

# Display the Plotly figure
st.plotly_chart(fig)
