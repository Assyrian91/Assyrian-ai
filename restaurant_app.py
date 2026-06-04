import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Ember Melbourne Restaurant", page_icon="🍽️", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #DC2626;
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover { background-color: #B91C1C; }
    .restaurant-header {
        background-color: #FEF2F2;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #DC2626;
    }
    .restaurant-info { font-size: 13px; color: #374151; line-height: 1.8; }
    </style>
""", unsafe_allow_html=True)

st.title("🍽️ Ember Melbourne")

st.markdown("""
<div class="restaurant-header">
    <div class="restaurant-info">
        📍 88 Flinders Lane, Melbourne VIC 3000<br>
        📞 +61 3 9000 3333 &nbsp;|&nbsp;
        🕐 Tue–Sun: 12pm–3pm, 6pm–10pm. Closed Monday.<br>
        ✉️ bookings@embermelbourne.com.au
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("Welcome to Ember! Ask me about our menu, dietary options, or make a reservation.")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write("👋 Welcome to Ember Melbourne! Whether you'd like to make a reservation, ask about our menu, or plan a special occasion — I'm here to help. What can I do for you?")

business_info = """
You are a warm and knowledgeable assistant for Ember Melbourne, a modern Australian fine dining restaurant in Melbourne.

Business info:
- Restaurant name: Ember Melbourne
- Address: 88 Flinders Lane, Melbourne VIC 3000
- Phone: +61 3 9000 3333
- Email: bookings@embermelbourne.com.au
- Hours: Tuesday to Sunday — Lunch 12pm–3pm, Dinner 6pm–10pm. Closed Monday.
- Dress code: Smart casual

Menu highlights:
ENTREES:
- Seared scallops with cauliflower purée and crispy capers — $24
- Wagyu beef tartare with truffle aioli — $28
- Burrata with heirloom tomatoes and basil oil — $22 (V)

MAINS:
- 300g dry-aged ribeye with roasted bone marrow butter — $68
- Pan-seared barramundi with lemon beurre blanc — $52
- Slow-roasted lamb shoulder with pomegranate jus — $58
- Mushroom and truffle risotto — $42 (V)
- Pasta of the day — ask your server (V option available)

DESSERTS:
- Warm chocolate fondant with vanilla ice cream — $18
- Lemon tart with raspberry coulis — $16
- Cheese board selection — $28

DRINKS:
- Extensive wine list — Australian and imported
- Cocktail menu available at the bar
- Non-alcoholic mocktail menu available

Dietary options:
- Vegetarian (V) options available
- Gluten-free options available on request
- Vegan options available — please inform staff
- Nut allergy — kitchen can accommodate, please advise when booking

Private dining:
- Private room available for groups of 10–30 people
- Set menus available for corporate events, birthdays, and weddings
- Deposit required for groups of 8 or more

Rules:
- If someone wants to make a reservation ask for: name, phone number, date, time (lunch or dinner), number of guests, any dietary requirements or special occasions
- For groups of 8 or more mention that a set menu and deposit may be required
- If someone has a special occasion (birthday, anniversary, proposal) offer to arrange a cake, flowers or a special table setup
- Always be warm, welcoming and passionate about the food
- If asked for recommendations suggest the wagyu tartare and dry-aged ribeye as signatures
- Mention that bookings are recommended especially on weekends
- Never confirm a booking — say you will send a confirmation email shortly
"""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask me anything about Ember Melbourne..."):
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
    st.caption("📞 +61 3 9000 3333")
with col2:
    st.caption("✉️ bookings@embermelbourne.com.au")

if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()
