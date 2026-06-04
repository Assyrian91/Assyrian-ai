import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Business Name Generator", page_icon="🏷️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #F59E0B, #EF4444);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(245, 158, 11, 0.6);
    }
    .stSelectbox>div>div,
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        background-color: #111118 !important;
        color: #E2E8F0 !important;
        border: 1px solid #1E1E2E !important;
        border-radius: 8px !important;
    }
    .header {
        background: linear-gradient(135deg, #F59E0B, #EF4444);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(245, 158, 11, 0.3);
    }
    .header h1 { color: white; font-size: 1.8rem; }
    .header p { color: #FEF3C7; font-size: 1rem; }
    .result-box {
        background: #111118;
        border: 1px solid #F59E0B;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>🏷️ Business Name & Slogan Generator</h1>
    <p>Generate creative business names and catchy slogans instantly</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    industry = st.selectbox("Industry", [
        "Restaurant / Cafe",
        "Real estate",
        "Dental / Medical",
        "Hotel / Hospitality",
        "Fitness / Gym",
        "Fashion / Retail",
        "Technology / AI",
        "Beauty / Salon",
        "Law firm",
        "Finance / Accounting",
        "Education / Tutoring",
        "General business"
    ])

with col2:
    style = st.selectbox("Name style", [
        "Modern & professional",
        "Fun & playful",
        "Luxury & premium",
        "Bold & powerful",
        "Minimal & clean",
        "Local & community focused"
    ])

col3, col4 = st.columns(2)
with col3:
    location = st.text_input(
        "Location (optional)",
        placeholder="e.g. Melbourne, Sydney, Australia"
    )
with col4:
    num_names = st.selectbox("How many names?", ["3", "5", "10"])

keywords = st.text_area(
    "Describe your business",
    placeholder="e.g. A premium coffee shop that focuses on single origin beans and a cozy atmosphere for remote workers...",
    height=120
)

include_slogans = st.checkbox("Include slogans for each name", value=True)
include_domain = st.checkbox("Check if .com.au domain name is available", value=False)

if st.button("🏷️ Generate Business Names"):
    if keywords.strip() == "":
        st.warning("Please describe your business first.")
    else:
        with st.spinner("Generating creative names..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a world class branding expert and business naming consultant. You create memorable, unique and meaningful business names that resonate with target audiences."
                    },
                    {
                        "role": "user",
                        "content": f"""Generate {num_names} creative business names for the following:

Industry: {industry}
Style: {style}
Location: {location if location else "Australia"}
Description: {keywords}

For each name provide:
1. The business name
2. Why it works (1 sentence)
{"3. A catchy slogan" if include_slogans else ""}

Format each one clearly numbered.
Make them memorable, unique and suitable for the Australian market.
Avoid generic names — be creative and distinctive."""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Your Business Names")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

        if include_domain:
            st.info("💡 Check domain availability at whois.com.au or auda.org.au")

        st.download_button(
            label="⬇️ Download Names",
            data=result,
            file_name="business_names.txt",
            mime="text/plain"
        )

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")