import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="AI Blog Post Writer", page_icon="✍️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #0F766E, #0369A1);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 0 15px rgba(15, 118, 110, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(15, 118, 110, 0.6);
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
        background: linear-gradient(135deg, #0F766E, #0369A1);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(15, 118, 110, 0.3);
    }
    .header h1 { color: white; font-size: 1.8rem; }
    .header p { color: #CCFBF1; font-size: 1rem; }
    .result-box {
        background: #111118;
        border: 1px solid #0F766E;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>✍️ AI Blog Post Writer</h1>
    <p>Generate full SEO-optimised blog posts for any business in seconds</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    industry = st.selectbox("Industry", [
        "Dental / Medical",
        "Real estate",
        "Restaurant / Cafe",
        "Hotel / Hospitality",
        "Fitness / Gym",
        "Law firm",
        "Finance / Accounting",
        "Technology / AI",
        "Beauty / Salon",
        "Education",
        "General business"
    ])

with col2:
    tone = st.selectbox("Tone", [
        "Professional",
        "Friendly & conversational",
        "Educational",
        "Inspirational",
        "Persuasive"
    ])

col3, col4 = st.columns(2)
with col3:
    length = st.selectbox("Blog post length", [
        "Short (300-500 words)",
        "Medium (600-900 words)",
        "Long (1000-1500 words)"
    ])

with col4:
    language = st.selectbox("Language", [
        "English",
        "Arabic",
        "French",
        "Spanish"
    ])

topic = st.text_input(
    "Blog post topic",
    placeholder="e.g. 5 reasons why you should visit the dentist every 6 months"
)

keywords = st.text_input(
    "SEO keywords (optional)",
    placeholder="e.g. Melbourne dentist, dental checkup, oral health"
)

business_name = st.text_input(
    "Business name (optional)",
    placeholder="e.g. SmileCare Dental"
)

include_cta = st.checkbox("Include call to action at the end", value=True)
include_meta = st.checkbox("Include SEO meta description", value=True)

if st.button("✍️ Write Blog Post"):
    if topic.strip() == "":
        st.warning("Please enter a blog post topic.")
    else:
        with st.spinner("Writing your blog post... this may take 15-20 seconds"):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert content writer and SEO specialist for Australian businesses. You write engaging, informative and SEO-optimised blog posts that rank well on Google and convert readers into customers."
                    },
                    {
                        "role": "user",
                        "content": f"""Write a {length} blog post for the following:

Topic: {topic}
Industry: {industry}
Tone: {tone}
Business name: {business_name if business_name else "Not specified"}
SEO keywords to include: {keywords if keywords else "Not specified"}
Language: {language}
Target audience: Australian readers, specifically Melbourne

Requirements:
- Write a compelling headline
- Use subheadings (H2, H3) to break up the content
- Include the SEO keywords naturally throughout
- Write for an Australian audience
- {"Include a strong call to action at the end" if include_cta else "No call to action needed"}
- {"Include an SEO meta description at the top (150-160 characters)" if include_meta else ""}
- Make it genuinely helpful and informative
- Avoid generic filler content"""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Your Blog Post")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Blog Post",
            data=result,
            file_name=f"blog_{topic[:30].replace(' ', '_')}.txt",
            mime="text/plain"
        )

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")