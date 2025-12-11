import random
import requests
import sys

# --- 🧠 MEMORY (CACHE) ---
# Idhu dhaan namma diary. Weather-a inga note panni vechu pom.
weather_cache = {}

# --- AGENT 1: Weather Agent (Smart Version) 🌤️ ---
def weather_agent(city):
    # 1. Check Cache (Diary-la irukka?)
    if city in weather_cache:
        print(f"   [Weather Agent] Found in Cache! ⚡ (No API call needed)")
        return weather_cache[city]
    
    # 2. Illana Internet-la thedu (Simulated)
    print(f"   [Weather Agent] Checking weather for {city}...")
    weathers = ["Sunny", "Rainy", "Cloudy", "Snowy"]
    result = random.choice(weathers)
    
    # 3. Cache-la ezhudhu
    weather_cache[city] = result
    return result

# --- AGENT 2: Travel Agent ✈️ ---
def travel_agent(weather_data):
    print(f"   [Travel Agent] Analyzing weather: {weather_data}...")
    if "Sunny" in weather_data:
        return "Pack sunglasses and sunscreen! 😎"
    elif "Rainy" in weather_data:
        return "Don't forget an umbrella and raincoat! ☔"
    elif "Snowy" in weather_data:
        return "Wear warm clothes and gloves! 🧤"
    else:
        return "Just enjoy the day, maybe a light jacket! 🧥"

# --- AGENT 4: Notification Agent 🔔 ---
def notification_agent(city, weather, advice):
    # 👇 UNGA WEBHOOK URL INGA IRUKKANUM 👇
    webhook_url = "	https://webhook.site/0590add1-ee24-45a9-87b5-c77f632a0c50" 
    
    if "Rainy" in weather or "Snowy" in weather:
        print(f"   [Notification Agent] Bad weather detected! Sending alert... 🚨")
        data = {
            "alert": "Weather Warning",
            "city": city,
            "weather": weather,
            "advice": advice
        }
        try:
            requests.post(webhook_url, json=data)
            print("   [Notification Agent] Alert sent successfully! ✅")
        except:
            print("   [Notification Agent] Failed to send alert. ❌")

# --- AGENT 3: Manager Agent 👔 ---
def manager_agent():
    print("--- 🤖 AI Multi-Agent Travel Assistant (With Cache) ---")
    print("Type 'exit' to stop.")
    
    while True:
        user_input = input("\nEnter a city name: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break
            
        # Step 1: Manager asks Weather Agent
        weather = weather_agent(user_input)
        
        # Step 2: Manager passes info to Travel Agent
        advice = travel_agent(weather)
        
        # Step 3: Manager gives final answer to User
        print(f"\n📢 Final Advice for {user_input}:")
        print(f"   Weather: {weather}")
        print(f"   Tip: {advice}")
        
        # Step 4: Notification
        notification_agent(user_input, weather, advice)

if __name__ == "__main__":
    manager_agent()