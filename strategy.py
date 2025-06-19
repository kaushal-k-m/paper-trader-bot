import pandas as pd
import talib

def calculate_rsi(data):
    close = data['Close']
    rsi = talib.RSI(close, timeperiod=14)
    return rsi.iloc[-1] if not rsi.isna().all() else None

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