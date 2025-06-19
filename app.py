import streamlit as st
import yfinance as yf
from sentiment import get_sentiment
from strategy import generate_signal

st.set_page_config(page_title="Dummy AI Trading Bot", layout="centered")
st.title("📈 Dummy AI-Powered Trading Bot")

symbol = st.text_input("Enter Stock Symbol (e.g., INFY.NS)", "INFY.NS")

if st.button("Run Bot"):
    st.write("Fetching data for:", symbol)
    data = yf.download(symbol, period="5d", interval="15m")

    if data.empty:
        st.error("No data found. Please check the symbol.")
    else:
        st.write("Latest Data:", data.tail(3))

        sentiment = get_sentiment(symbol)
        signal, reason = generate_signal(data, sentiment)

        st.subheader("🤖 Bot Decision")
        st.write(f"**Signal:** {signal}")
        st.write(f"**Reason:** {reason}")