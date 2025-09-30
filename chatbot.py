# chatbot.py

# 👋 Welcome to CryptoBuddy – Your First AI-Powered Financial Sidekick! 🌟

# Objective: Analyze crypto data and give advice based on profitability and sustainability.

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

print("👋 Hi! I'm CryptoBuddy—your AI-powered financial sidekick!")
print("Ask me about trending cryptos or the most sustainable coins 🌱")

user_query = input("What would you like to know? ").lower()

# Chatbot Logic
if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"🌱 Invest in {recommend}! It's eco-friendly and has long-term potential!")

elif "trending" in user_query or "growth" in user_query or "rising" in user_query:
    trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
    print(f"🚀 These coins are trending up: {', '.join(trending)}")

elif "profitable" in user_query or "best" in user_query:
    profitable = [
        coin for coin, data in crypto_db.items()
        if data["price_trend"] == "rising" and data["market_cap"] == "high"
    ]
    if profitable:
        print(f"💰 Based on profitability, consider: {', '.join(profitable)}")
    else:
        print("🤷 No coins meet the profitability criteria right now.")

else:
    print("🤔 I'm not sure about that. Try asking about sustainability or trends!")

print("⚠️ Disclaimer: Crypto is risky—always do your own research!")
