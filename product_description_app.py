import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Product Description Writer", page_icon="🛍️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #BE185D, #7C3AED);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 0 15px rgba(190, 24, 93, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(190, 24, 93, 0.6);
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
        background: linear-gradient(135deg, #BE185D, #7C3AED);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(190, 24, 93, 0.3);
    }
    .header h1 { color: white; font-size: 1.8rem; }
    .header p { color: #FCE7F3; font-size: 1rem; }
    .result-box {
        background: #111118;
        border: 1px solid #BE185D;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>🛍️ Product Description Writer</h1>
    <p>Generate compelling product descriptions that convert browsers into buyers</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("Platform", [
        "Shopify / Website",
        "Amazon",
        "eBay",
        "Etsy",
        "Instagram Shop",
        "General e-commerce"
    ])

with col2:
    tone = st.selectbox("Tone", [
        "Professional",
        "Luxury & premium",
        "Fun & playful",
        "Minimal & clean",
        "Persuasive & urgent"
    ])

col3, col4 = st.columns(2)
with col3:
    length = st.selectbox("Description length", [
        "Short (50-100 words)",
        "Medium (100-200 words)",
        "Long (200-350 words)"
    ])

with col4:
    language = st.selectbox("Language", [
        "English",
        "Arabic",
        "French",
        "Spanish"
    ])

product_name = st.text_input(
    "Product name",
    placeholder="e.g. Handmade Leather Wallet"
)

product_details = st.text_area(
    "Product details",
    placeholder="e.g. Full grain leather, 6 card slots, coin pocket, available in brown and black, handmade in Melbourne, dimensions 12x9cm...",
    height=120
)

target_audience = st.text_input(
    "Target audience (optional)",
    placeholder="e.g. Men aged 25-45 who value quality"
)

keywords = st.text_input(
    "SEO keywords (optional)",
    placeholder="e.g. leather wallet Melbourne, handmade wallet Australia"
)

num_descriptions = st.selectbox("How many variations?", ["1", "2", "3"])
include_bullet_points = st.checkbox("Include bullet point features", value=True)

if st.button("🛍️ Write Description"):
    if product_name.strip() == "" or product_details.strip() == "":
        st.warning("Please enter a product name and details.")
    else:
        with st.spinner("Writing your product description..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert e-commerce copywriter specialising in Australian businesses. You write compelling product descriptions that highlight benefits, create desire and convert browsers into buyers."
                    },
                    {
                        "role": "user",
                        "content": f"""Write {num_descriptions} product description(s) for the following:

Product name: {product_name}
Platform: {platform}
Details: {product_details}
Tone: {tone}
Length: {length}
Target audience: {target_audience if target_audience else "General Australian consumers"}
SEO keywords: {keywords if keywords else "Not specified"}
Language: {language}

Requirements:
- Start with a compelling opening line that grabs attention
- Focus on benefits not just features
- {"Include a bullet point list of key features" if include_bullet_points else "No bullet points — flowing prose only"}
- Include the SEO keywords naturally
- Write for Australian consumers
- End with a subtle call to action
{"- Separate each variation with ---" if int(num_descriptions) > 1 else ""}"""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader(f"Description for {product_name}")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Description",
            data=result,
            file_name=f"description_{product_name[:30].replace(' ', '_')}.txt",
            mime="text/plain"
        )

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")