import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Enterprise Version", page_icon="📈")

st.markdown("# Virtual Oil Factory, Hyrule")
st.sidebar.header("Methane Monitor [last 100 days]")
st.write(
    """This mock-up illustrates a plot for a Methane Plume Detection in hypothetical Oil Factory's location. 
    
We're generating a bunch of random numbers in a loop for around
5 seconds for now. It will be replaced by real-time data based on satellite images we are receiving from Space Y. 

Enjoy!🥳"""
)
st.divider()
st.subheader("Communication Channel")
text_contents = '''This is demo report'''
# Create two columns for the buttons
col1, col2 = st.columns(2)

# Left aligned button in the left column
with col1:
    st.markdown(
        f"<div style='text-align: left;'>"
        f"<button class='streamlit-button'>{chr(128226)} Generate Report for Regulators</button>"
        f"</div>",
        unsafe_allow_html=True,
    )

# Right aligned button in the right column
with col2:
    st.markdown(
        f"<div style='text-align: right;'>"
        f"<button class='streamlit-button'>{chr(128230)} Check Message from Regulator</button>"
        f"</div>",
        unsafe_allow_html=True,
    )

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.normal(0.6, 0.1, 1)
st.divider()
st.subheader("Monitor Channel")
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = np.random.normal(0.6, 0.1, 1)
    # Check if the new value exceeds the threshold and add an alert if it does
    if new_rows[0] > 0.8:
        
        st.warning(f"Abnormal Methane Emission {np.round(new_rows,4)} detected on day {i}. Warning of fugitive emission.",icon="⚠️")
 
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")