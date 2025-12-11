import sys
import requests
import logging
import time  # 👈 Puthu Import: Time-a track panna
from order_agent import get_order_status

# --- CONFIGURATION ---
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def send_escalation_alert(user_message):
    webhook_url = "https://webhook.site/0590add1-ee24-45a9-87b5-c77f632a0c50" # Unga URL confirm pannikkonga
    data = {"alert": "🚨 ANGRY USER DETECTED", "message": user_message, "priority": "HIGH"}
    try:
        requests.post(webhook_url, json=data)
        print("   [System] Manager notified via Webhook! ✅")
    except Exception as e:
        print(f"   [System] Failed to notify Manager. ❌ Error: {e}")

# --- MAIN AGENT LOGIC ---
def main():
    print("--- 🤖 AI Customer Service Brain (Triage Agent) ---")
    print("Type 'exit' to stop.\n")

    # Rate Limiting Tracker ⏱️
    last_message_time = 0

    while True:
        user_input = input("How can I help you today? (Type 'exit' to quit): ").strip()
        
        # 🛑 RATE LIMIT CHECK 🛑
        current_time = time.time()
        time_diff = current_time - last_message_time
        
        # 2 Seconds gap irukkanum
        if time_diff < 2: 
            print("   ⚠️  Whoa! Too fast. Please wait a moment.")
            logging.warning("Rate Limit Triggered (Spam detected)")
            continue # Skip everything below, go back to start
        
        # Update Timer
        last_message_time = current_time

        # Normal Logging
        logging.info(f"User said: {user_input}") 

        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day! 👋")
            break
        
        # LOGIC 1: ANGER DETECTION 😡
        angry_words = ["bad", "stupid", "worst", "useless", "manager", "angry"]
        if any(word in user_input.lower() for word in angry_words):
            logging.warning(f"Angry User Detected! Message: {user_input}")
            print("\n🚨 Escalating to Human Agent...")
            send_escalation_alert(user_input)
            print("   (Connecting you to a supervisor. Please hold...)")
            continue

        # LOGIC 2: ORDER STATUS 📦
        if "order" in user_input.lower() or "status" in user_input.lower():
            order_id = input("   Please enter your Order ID (e.g., ORD-101): ")
            logging.info(f"Checking status for Order ID: {order_id}")
            print(f"   [Triage Agent] Asking Order Agent about {order_id}...")
            response = get_order_status(order_id)
            print(f"   ✅ {response}")
            continue

        # LOGIC 3: REFUND/RETURN 📜
        if "refund" in user_input.lower() or "return" in user_input.lower():
            print("\n📜 Return Policy:")
            print("   You can return items within 30 days of delivery.")
            continue

        print("\n🤔 I didn't understand that.")

if __name__ == "__main__":
    main()