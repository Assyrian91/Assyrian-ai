import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Social Media Caption Writer", page_icon="📱", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #E1306C, #833AB4);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 0 15px rgba(225, 48, 108, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(225, 48, 108, 0.6);
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
        background: linear-gradient(135deg, #E1306C, #833AB4);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(225, 48, 108, 0.3);
    }
    .header h1 { color: white; font-size: 1.8rem; }
    .header p { color: #F8D7E3; font-size: 1rem; }
    .result-box {
        background: #111118;
        border: 1px solid #833AB4;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>📱 Social Media Caption Writer</h1>
    <p>Generate engaging captions for Instagram, Facebook, LinkedIn and TikTok instantly</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("Platform", [
        "Instagram",
        "Facebook",
        "LinkedIn",
        "TikTok",
        "Twitter / X"
    ])
with col2:
    tone = st.selectbox("Tone", [
        "Professional",
        "Fun & casual",
        "Inspirational",
        "Promotional",
        "Educational"
    ])

col3, col4 = st.columns(2)
with col3:
    industry = st.selectbox("Industry", [
        "Restaurant / Cafe",
        "Real estate",
        "Dental / Medical",
        "Hotel / Hospitality",
        "Fitness / Gym",
        "Fashion / Retail",
        "Technology",
        "General business"
    ])
with col4:
    include_hashtags = st.selectbox("Include hashtags?", [
        "Yes — Melbourne focused",
        "Yes — Australia wide",
        "Yes — Global",
        "No hashtags"
    ])

topic = st.text_area(
    "What is your post about?",
    placeholder="e.g. We just launched a new spring menu with fresh seasonal ingredients...",
    height=120
)

include_emoji = st.checkbox("Include emojis", value=True)
num_captions = st.selectbox("How many caption options?", ["1", "2", "3"])

if st.button("✍️ Generate Captions"):
    if topic.strip() == "":
        st.warning("Please describe what your post is about.")
    else:
        with st.spinner("Writing your captions..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert social media copywriter specialising in Australian businesses. You write engaging, authentic captions that drive real engagement."
                    },
                    {
                        "role": "user",
                        "content": f"""Write {num_captions} different {tone.lower()} caption(s) for {platform} for a {industry} business.

Topic: {topic}

Requirements:
- Tone: {tone}
- Platform: {platform} (optimise length and style for this platform)
- {"Include emojis" if include_emoji else "No emojis"}
- Hashtags: {include_hashtags}
- Write for an Australian audience
- Make it authentic and engaging, not generic

{"Separate each caption with --- if writing multiple." if int(num_captions) > 1 else ""}"""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Your Captions")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Captions",
            data=result,
            file_name="captions.txt",
            mime="text/plain"
        )

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")