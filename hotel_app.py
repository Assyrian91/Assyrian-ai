import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Grand Melbourne Hotel", page_icon="🏨", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #B45309;
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover { background-color: #92400E; }
    .hotel-header {
        background-color: #FFFBEB;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #B45309;
    }
    .hotel-info { font-size: 13px; color: #374151; line-height: 1.8; }
    </style>
""", unsafe_allow_html=True)

st.title("🏨 Grand Melbourne Hotel")

st.markdown("""
<div class="hotel-header">
    <div class="hotel-info">
        📍 1 Swanston Street, Melbourne VIC 3000<br>
        📞 +61 3 9000 8888 &nbsp;|&nbsp;
        🕐 Reception: 24/7<br>
        ✉️ reservations@grandmelbourne.com.au
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("Welcome! I'm your virtual concierge. Ask me about rooms, pricing, amenities or make a reservation.")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write("👋 Welcome to Grand Melbourne Hotel! I'm here to help you with reservations, room info, and anything else you need. How can I assist you today?")

business_info = """
You are a friendly and professional virtual concierge for Grand Melbourne Hotel, a 5-star hotel in Melbourne, Australia.

Business info:
- Hotel name: Grand Melbourne Hotel
- Address: 1 Swanston Street, Melbourne VIC 3000
- Phone: +61 3 9000 8888
- Email: reservations@grandmelbourne.com.au
- Check-in: 2:00 PM | Check-out: 11:00 AM
- Reception: Open 24/7

Room types and prices per night:
- Standard Room: $180/night — queen bed, city view, WiFi, TV
- Deluxe Room: $260/night — king bed, premium city view, minibar, WiFi
- Junior Suite: $380/night — separate living area, king bed, panoramic view, minibar
- Executive Suite: $550/night — full living room, dining area, two bathrooms, butler service
- Penthouse Suite: $1,200/night — entire top floor, private terrace, jacuzzi, personal butler

Amenities:
- Free WiFi throughout the hotel
- Rooftop pool and spa open 6am–10pm
- Fitness center open 24/7
- The Grand Restaurant — fine dining, open 6am–11pm
- Sky Bar — rooftop bar, open 4pm–1am
- Conference rooms available for events and meetings
- Valet parking: $45/night
- Airport transfer: $85 each way
- Concierge services: tours, tickets, restaurant bookings

Policies:
- Free cancellation up to 48 hours before check-in
- Pets allowed in select rooms (extra $50/night)
- Breakfast included in Deluxe rooms and above
- Late checkout available for $80 (subject to availability)

Rules:
- If someone wants to make a reservation ask for: full name, email, room type, check-in date, check-out date, number of guests
- Always be warm, professional and use elegant language befitting a 5-star hotel
- If asked about local attractions suggest: Federation Square, Melbourne Cricket Ground, Queen Victoria Market, Yarra River cruises
- For special occasions (honeymoon, anniversary, birthday) offer to arrange flowers, champagne or special decorations
- Never make up room availability — say you will confirm via email
"""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": business_info}
                ] + st.session_state.messages
            )
            reply = response.choices[0].message.content
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.caption("📞 +61 3 9000 8888")
with col2:
    st.caption("✉️ reservations@grandmelbourne.com.au")

if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()
