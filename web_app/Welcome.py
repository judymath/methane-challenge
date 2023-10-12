import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.write("# Welcome to CleanR Lab5 beta! 👋")

st.sidebar.success("Select a feature above.")

st.markdown(
    """
## 👈 Select a feature from the sidebar
- 🛰️**Image Prediction**: Upload a satellite image and witness our model's prediction capabilities for methane plume.
- 👮**Regulator Version**: Aimed at the energy industry regulators, it provides insights on where methane plume has been detected and the associated Enterprise.
- 📈**Enterprise Version**: Tailored for enterprises in the energy industry to constantly monitor their methane emissions.
## 🧪 What is CleanR Lab5

CleanR Lab5 is a Data Science team dedicated to CleanR's Mission for Methane (GHG): Monitoring, Reporting and Verification.

🌵 Our main objectives:

- Becoming the bridge between **Regulator** and **Enterprise** and reduce communication costs.
- Independent verification from the third party.
- Accessing difficult-to-reach locations leverage satellite images
- Providing large-scale monitoring and alerting service for both sides.


🌎 We believe it's not just about a simple **Yes/No** answer but rather understanding the overall trend and mitigateing fugitive emissions.


## 🤝 Our Partnerships

- Partnering with 🚀**Space Y** for real-time satellite image.

"""
)
