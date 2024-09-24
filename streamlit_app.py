import streamlit as st
import requests

st.title("ISMS Tool Dashboard")

st.write("Use this dashboard to interact with the Deming ISMS tool.")

# Example: Fetch some data from your backend
if st.button("Fetch ISMS Data"):
    response = requests.get("https://your-backend-endpoint/isms-data")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error("Failed to fetch data")

