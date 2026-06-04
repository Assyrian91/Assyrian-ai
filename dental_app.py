import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="SmileCare Dental", page_icon="🦷", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover { background-color: #1D4ED8; }
    .clinic-header {
        background-color: #EFF6FF;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #2563EB;
    }
    .clinic-info {
        font-size: 13px;
        color: #374151;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🦷 SmileCare Dental Clinic")

st.markdown("""
<div class="clinic-header">
    <div class="clinic-info">
        📍 123 Collins Street, Melbourne VIC 3000<br>
        📞 +61 3 9000 1234 &nbsp;|&nbsp;
        🕐 Mon–Fri 8am–6pm, Sat 9am–2pm<br>
        🚨 <b>Dental emergency?</b> Call us immediately on +61 3 9000 1234
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("Hi! I'm your virtual dental assistant. Ask me about services, prices, or book an appointment.")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write("👋 Welcome to SmileCare! I can help you with pricing, services, appointments and more. What can I do for you today?")

business_info = """
You are a friendly virtual assistant for SmileCare Dental Clinic in Melbourne, Australia.

Business info:
- Clinic name: SmileCare Dental Clinic
- Address: 123 Collins Street, Melbourne VIC 3000
- Phone: +61 3 9000 1234
- Email: hello@smilecare.com.au
- Working hours: Monday to Friday 8am to 6pm, Saturday 9am to 2pm, Closed Sunday

Services and prices:
- General checkup and clean: $180
- Teeth whitening: $450
- Fillings: from $180
- Root canal: from $800
- Braces consultation: free first visit
- Emergency appointments: available same day

Insurance: We accept all major health funds including Medibank, BUPA, HCF and NIB.

Rules:
- If someone wants to book an appointment, ask for their name, phone number, preferred date and what service they need
- If someone has a dental emergency, tell them to call immediately on +61 3 9000 1234
- If someone asks about a specific medical condition, advise them to speak directly with the dentist
- Always be warm, calm and reassuring — many people are nervous about dentists
- Never give specific medical advice
- Keep responses short and friendly
"""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type your message here..."):
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
    st.caption("📞 Emergency: +61 3 9000 1234")
with col2:
    st.caption("✉️ hello@smilecare.com.au")

if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()
