import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 SPY Options Screener")

ticker = yf.Ticker("SPY")

expirations = ticker.options
selected_exp = st.selectbox("Select Expiration Date", expirations)

# Load option chain
option_chain = ticker.option_chain(selected_exp)
calls = option_chain.calls

# Filter inputs
max_price = st.slider("Max Premium ($)", 0.0, 5.0, 0.50)
min_volume = st.slider("Min Volume", 0, 5000, 1000)

# Filter Data
filtered_calls = calls[(calls["lastPrice"] <= max_price) & (calls["volume"] >= min_volume)]

# Show results
st.subheader("🔍 Filtered Call Options")
if filtered_calls.empty:
    st.write("No options match your criteria.")
else:
    st.dataframe(filtered_calls[['contractSymbol', 'strike', 'lastPrice', 'volume']])
