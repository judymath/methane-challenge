import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk



st.set_page_config(page_title="Regulator_Version", page_icon="📊")

st.markdown("# Abnormal Emission Detected")
st.sidebar.header("Methane from Energy Sector in US")
st.write(
    """This mockup shows how U.S. regulators use lab5's monitoring system to identity potential fugitive emissions.
Refer to [US GHG Emission Report](https://thehill.com/policy/energy-environment/3559506-four-companies-are-top-sources-of-us-greenhouse-gas-methane-emissions-report/)."""
)
st.divider()
st.subheader("Communication Channel")
col1, col2, col3 = st.columns(3)

with col1: 

    st.radio(
        "Send message to enterprise 👉",
        key="Degree",
        options=["Emergency", "Notification"],
    )
with col2:
  
    st.text_input(
        "To",
        "Virtual Oil",
        key="placeholder",
    )
with col3:
    
    st.text_input(
        "Message",
        "Message Content",
        key="placeholder1",
    )

def create_data():
    np.random.seed(42)  # for reproducibility
    n = 10

    latitudes = np.random.uniform(30.396308, 49.384358, n)
    longitudes = np.random.uniform(-100.000000, -80.934570, n)

    data = {
        'lat': latitudes,
        'lon': longitudes,

    }

    return pd.DataFrame(data)

df = create_data()
st.divider()
st.subheader("Monitor Channel")
st.map(df)