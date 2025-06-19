import pandas as pd
import ta

def calculate_rsi(data):
    close = data['Close'].dropna()

    if len(close) < 15:
        return None  # Not enough data for 14-period RSI

    try:
        rsi_series = ta.momentum.RSIIndicator(close, window=14).rsi()
        return rsi_series.dropna().iloc[-1]
    except Exception as e:
        print("RSI Calculation Failed:", e)
        return None

def generate_signal(data, sentiment):
    rsi_value = calculate_rsi(data)

    if rsi_value is None:
        return "Hold", "Insufficient data for RSI."

    sentiment = sentiment.lower()

    if rsi_value < 30 and "positive" in sentiment:
        return "Buy", f"RSI={rsi_value:.2f} (oversold) and sentiment is positive."
    elif rsi_value > 70 and "negative" in sentiment:
        return "Sell", f"RSI={rsi_value:.2f} (overbought) and sentiment is negative."
    else:
        return "Hold", f"RSI={rsi_value:.2f}, sentiment='{sentiment}' — no strong signal."
