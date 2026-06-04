import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Melbourne Property Assistant", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #059669;
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover { background-color: #047857; }
    .agency-header {
        background-color: #ECFDF5;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #059669;
    }
    .agency-info {
        font-size: 13px;
        color: #374151;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏠 Melbourne Real Estate Agency")

st.markdown("""
<div class="agency-header">
    <div class="agency-info">
        📍 456 Collins Street, Melbourne VIC 3000<br>
        📞 +61 3 9000 5678 &nbsp;|&nbsp;
        🕐 Mon–Fri 9am–5:30pm, Sat 10am–3pm<br>
        ✉️ info@melbournerealestate.com.au
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("Hi! I'm your Melbourne property assistant. Ask me about buying, selling, renting or investment.")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write("👋 Welcome to Melbourne Real Estate Agency! Whether you're buying, selling or renting, I'm here to help. What are you looking for today?")

business_info = """
You are a friendly and knowledgeable property assistant for Melbourne Real Estate Agency in Melbourne, Australia.

Business info:
- Agency name: Melbourne Real Estate Agency
- Address: 456 Collins Street, Melbourne VIC 3000
- Phone: +61 3 9000 5678
- Email: info@melbournerealestate.com.au
- Working hours: Monday to Friday 9am to 5:30pm, Saturday 10am to 3pm, Closed Sunday

Areas we cover and typical price ranges:
INNER CITY & PREMIUM SUBURBS:
- Southbank: apartments $500k–$1.2M, rent $2,200–$4,500/month
- South Yarra: units $600k–$2M, rent $2,500–$5,000/month
- Toorak: houses $2M–$10M+, rent $5,000–$15,000/month
- Richmond: units $500k–$1.2M, rent $2,000–$3,500/month
- Fitzroy: houses $1M–$2.5M, rent $2,800–$4,500/month
- Carlton: units $400k–$900k, rent $1,800–$3,000/month
- Docklands: apartments $450k–$1.1M, rent $2,000–$4,000/month
- St Kilda: units $450k–$1M, rent $1,900–$3,500/month

MIDDLE SUBURBS:
- Hawthorn: houses $1.2M–$3M, rent $3,000–$5,500/month
- Camberwell: houses $1.2M–$3.5M, rent $3,000–$5,000/month
- Box Hill: units $450k–$900k, rent $1,700–$2,800/month
- Glen Waverley: houses $900k–$2M, rent $2,500–$4,000/month
- Moonee Ponds: houses $800k–$1.8M, rent $2,200–$3,500/month
- Footscray: units $400k–$750k, rent $1,600–$2,500/month
- Sunshine: houses $550k–$950k, rent $1,800–$2,800/month
- Frankston: houses $450k–$850k, rent $1,500–$2,500/month

OUTER & AFFORDABLE SUBURBS:
- Craigieburn: houses $480k–$750k, rent $1,600–$2,200/month
- Mickleham: houses $460k–$720k, rent $1,500–$2,100/month
- Wollert: houses $450k–$700k, rent $1,500–$2,000/month
- Mernda: houses $470k–$730k, rent $1,550–$2,100/month
- Epping: houses $550k–$900k, rent $1,700–$2,400/month
- Pakenham: houses $430k–$680k, rent $1,400–$2,000/month
- Berwick: houses $550k–$950k, rent $1,700–$2,400/month
- Clyde North: houses $450k–$720k, rent $1,500–$2,100/month
- Officer: houses $440k–$700k, rent $1,450–$2,000/month
- Melton: houses $380k–$620k, rent $1,300–$1,900/month
- Werribee: houses $430k–$700k, rent $1,400–$2,000/month
- Hoppers Crossing: houses $480k–$780k, rent $1,500–$2,200/month
- Tarneit: houses $460k–$750k, rent $1,500–$2,100/month
- Point Cook: houses $600k–$1M, rent $1,900–$2,800/month
- Truganina: houses $450k–$720k, rent $1,500–$2,000/month

Services:
- Buying, selling, renting, property management
- First home buyer guidance
- Investment property advice
- Free property appraisals

Rules:
- Always use Australian terminology (unit, house, townhouse, appraisal)
- If someone wants to book an inspection, ask for name, phone number, preferred suburb and budget
- If someone is a first home buyer mention the First Home Owner Grant (FHOG) in Victoria — up to $10,000 for new builds
- For investment advice, mention rental yield and capital growth potential
- Keep responses friendly, concise and helpful
- If unsure about a specific property, offer to have an agent follow up
"""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask me anything about Melbourne property..."):
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
    st.caption("📞 +61 3 9000 5678")
with col2:
    st.caption("✉️ info@melbournerealestate.com.au")

if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()
