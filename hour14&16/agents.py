import random

# --- AGENT 1: Weather Agent 🌤️ ---
# Ivaroda velai: City name vangittu, anga weather epdi irukku nu solrathu.
def weather_agent(city):
    print(f"   [Weather Agent] Checking weather for {city}...")
    # Namma kitta real API illa, so random-a generate panrom.
    weathers = ["Sunny", "Rainy", "Cloudy", "Snowy"]
    return random.choice(weathers)

# --- AGENT 2: Travel Agent ✈️ ---
# Ivaroda velai: Weather therinja udane, tips solrathu.
def travel_agent(weather_data):
    print(f"   [Travel Agent] Analying weather: {weather_data}...")
    if "Sunny" in weather_data:
        return "Pack sunglasses and sunscreen! 😎"
    elif "Rainy" in weather_data:
        return "Don't forget an umbrella and raincoat! ☔"
    elif "Snowy" in weather_data:
        return "Wear warm clothes and gloves! 🧤"
    else:
        return "Just enjoy the day, maybe a light jacket! 🧥"

# --- AGENT 3: Manager Agent 👔 ---
# Ivar dhaan "Orchestrator". User kitta pesuvar, matha agents-a vela vanguvar.
def manager_agent():
    print("--- 🤖 AI Multi-Agent Travel Assistant ---")
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

# Simulation Start
if __name__ == "__main__":
    manager_agent()