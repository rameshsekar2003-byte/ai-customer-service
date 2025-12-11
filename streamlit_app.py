import streamlit as st
import time
import requests
import logging
# Tool-ஐ import செய்கிறோம்
from order_agent import get_order_status

# --- CONFIGURATION ---
# Page Title
st.set_page_config(page_title="AI Customer Service", page_icon="🤖")

st.title("🤖 AI Customer Support Agent")
st.caption("Ask about orders (e.g., ORD-101) or returns!")

# Webhook Function
def send_escalation_alert(user_message):
    webhook_url = "https://webhook.site/0590add1-ee24-45a9-87b5-c77f632a0c50" # உங்கள் URL
    data = {"alert": "🚨 ANGRY USER DETECTED", "message": user_message, "priority": "HIGH"}
    try:
        requests.post(webhook_url, json=data)
        return True
    except:
        return False

# --- CHAT LOGIC ---
# Chat History-ஐ நினைவில் வைத்துக்கொள்ள (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# பழைய மெசேஜ்களை திரையில் காட்டு
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input (Chat Box)
if prompt := st.chat_input("How can I help you?"):
    # 1. User Message-ஐ காட்டு
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. AI யோசிக்கிறது...
    response = ""
    
    # LOGIC 1: ANGER DETECTION 😡
    angry_words = ["bad", "stupid", "worst", "useless", "manager", "angry"]
    if any(word in prompt.lower() for word in angry_words):
        with st.spinner("Escalating to Manager..."):
            send_escalation_alert(prompt)
            time.sleep(1) # Fake delay
        response = "🚨 I have notified a human supervisor. They will contact you shortly."

    # LOGIC 2: ORDER STATUS 📦
    elif "order" in prompt.lower() or "status" in prompt.lower():
        # Streamlit-ல் "Input" வாங்க முடியாது, அதனால் Order ID-ஐ மெசேஜிலேயே தேடுகிறோம்
        # எ.கா: "Status of ORD-101"
        words = prompt.split()
        order_id = None
        for word in words:
            if word.startswith("ORD-"):
                order_id = word
                break
        
        if order_id:
            with st.spinner(f"Checking Database for {order_id}..."):
                time.sleep(1)
                status = get_order_status(order_id)
            response = f"✅ {status}"
        else:
            response = "Please mention the Order ID (e.g., ORD-101) in your message."

    # LOGIC 3: REFUND 📜
    elif "refund" in prompt.lower() or "return" in prompt.lower():
        response = "📜 **Return Policy:**\nYou can return items within **30 days** of delivery.\nItems must be unused."

    # DEFAULT
    else:
        response = "🤔 I didn't understand. Try asking about **Order Status** or **Refunds**."

    # 3. AI பதிலை காட்டு
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)