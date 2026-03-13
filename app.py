import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# Use caching to optimize performance
@st.cache(suppress_st_warning=True)
def load_data():
    # Load your data here
    return pd.DataFrame({'Time': [datetime.now(pytz.utc)], 'Signal': ['Buy']})

# Error handling
try:
    data = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")

# Timezone management
timezone = pytz.timezone('UTC')  # Adjust to your desired timezone
current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Current Time (UTC): {current_time}")

# Display the data
st.title('Trading Signal Bot')
st.write(data)