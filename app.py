import streamlit as st
import time
from read_feed import get_latest_value

st.set_page_config(page_title="SmartFarm Light Monitor", page_icon="💡")
st.title("💡 SmartFarm: Real-Time Light Sensor")

feed_key = "smartfarm.light"  # Your actual Adafruit IO feed

placeholder = st.empty()

while True:
    value, timestamp = get_latest_value(feed_key)
    if value is not None:
        with placeholder.container():
            st.metric(label="Light Intensity", value=f"{value:.2f}")
            st.caption(f"Last updated: {timestamp}")
    else:
        st.warning("Waiting for data or feed not found.")
    
    time.sleep(5)