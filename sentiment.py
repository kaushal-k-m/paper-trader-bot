def get_sentiment(stock_name):
    # Dummy sentiment analyzer for now
    sample_sentiments = {
        "INFY": "Positive",
        "RELIANCE": "Negative",
        "TCS": "Neutral",
    }
    return sample_sentiments.get(stock_name.upper(), "Neutral")