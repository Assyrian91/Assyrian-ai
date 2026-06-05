import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="FAQ Generator", page_icon="❓", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #059669, #0284C7);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 0 15px rgba(5, 150, 105, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(5, 150, 105, 0.6);
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
        background: linear-gradient(135deg, #059669, #0284C7);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(5, 150, 105, 0.3);
    }
    .header h1 { color: white; font-size: 1.8rem; }
    .header p { color: #D1FAE5; font-size: 1rem; }
    .result-box {
        background: #111118;
        border: 1px solid #059669;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>❓ FAQ Generator</h1>
    <p>Generate professional FAQs for any business instantly</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    industry = st.selectbox("Industry", [
        "Dental / Medical clinic",
        "Restaurant / Cafe",
        "Real estate agency",
        "Hotel / Hospitality",
        "Fitness / Gym",
        "Law firm",
        "Finance / Accounting",
        "Beauty / Salon",
        "E-commerce / Retail",
        "Education / Tutoring",
        "Technology / Software",
        "General business"
    ])

with col2:
    num_faqs = st.selectbox("Number of FAQs", ["5", "10", "15", "20"])

col3, col4 = st.columns(2)
with col3:
    tone = st.selectbox("Tone", [
        "Professional",
        "Friendly & casual",
        "Formal",
        "Simple & clear"
    ])

with col4:
    language = st.selectbox("Language", [
        "English",
        "Arabic",
        "French",
        "Spanish"
    ])

business_name = st.text_input(
    "Business name (optional)",
    placeholder="e.g. SmileCare Dental Clinic"
)

business_description = st.text_area(
    "Describe your business",
    placeholder="e.g. A dental clinic in Melbourne offering general checkups, teeth whitening, braces and emergency appointments. We accept BUPA and Medibank insurance...",
    height=150
)

if st.button("❓ Generate FAQs"):
    if business_description.strip() == "":
        st.warning("Please describe your business first.")
    else:
        with st.spinner("Generating your FAQs..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert business consultant who creates clear, helpful and comprehensive FAQ sections for business websites. Your FAQs address real customer concerns and are optimised for Australian businesses."
                    },
                    {
                        "role": "user",
                        "content": f"""Generate {num_faqs} FAQs for the following business:

Business name: {business_name if business_name else "Not specified"}
Industry: {industry}
Description: {business_description}
Tone: {tone}
Language: {language}

Format each FAQ as:
Q: [Question]
A: [Answer]

Make the questions realistic — things customers actually ask.
Make the answers helpful, accurate and concise.
Include questions about pricing, hours, location, services, 
booking process and any industry specific concerns."""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader(f"FAQs for {business_name if business_name else industry}")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download FAQs",
            data=result,
            file_name=f"faqs_{business_name if business_name else 'business'}.txt",
            mime="text/plain"
        )

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")