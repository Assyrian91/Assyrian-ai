import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI Image Generator", page_icon="🎨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #7C3AED, #DB2777);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 0 15px rgba(124, 58, 237, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(124, 58, 237, 0.6);
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
        background: linear-gradient(135deg, #7C3AED, #DB2777);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(124, 58, 237, 0.3);
    }
    .header h1 { color: white; font-size: 1.8rem; }
    .header p { color: #F3E8FF; font-size: 1rem; }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>🎨 AI Image Generator</h1>
    <p>Generate stunning images for your business in seconds</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Image style", [
        "Photorealistic",
        "Professional photography",
        "Minimalist",
        "Watercolor",
        "Digital art",
        "Cinematic",
        "Flat illustration"
    ])

with col2:
    use_case = st.selectbox("Use case", [
        "Restaurant / Food",
        "Real estate / Property",
        "Hotel / Hospitality",
        "Business / Corporate",
        "Social media post",
        "Product showcase",
        "General"
    ])

prompt = st.text_area(
    "Describe the image you want",
    placeholder="e.g. A cozy Melbourne cafe with warm lighting, fresh coffee and pastries on a wooden table...",
    height=120
)

negative = st.text_input(
    "What to avoid (optional)",
    placeholder="e.g. blurry, dark, text"
)

if st.button("🎨 Generate Image"):
    if prompt.strip() == "":
        st.warning("Please describe the image you want.")
    else:
        with st.spinner("Generating your image... this takes 15-20 seconds"):
            try:
                full_prompt = f"{prompt}, {style} style, high quality, professional"
                if negative:
                    full_prompt += f", avoid: {negative}"
                if use_case != "General":
                    full_prompt += f", {use_case} context"

                API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
                headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}
                payload = {"inputs": full_prompt}

                response = requests.post(
                    API_URL,
                    headers=headers,
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption=prompt, use_container_width=True)
                    st.download_button(
                        label="⬇️ Download Image",
                        data=response.content,
                        file_name="generated_image.png",
                        mime="image/png"
                    )
                    st.success("Image generated!")
                elif response.status_code == 503:
                    st.warning("Model is loading — wait 20 seconds and try again.")
                else:
                    st.error(f"Error {response.status_code} — please try again.")

            except Exception as e:
                st.error(f"Connection error: {e}")

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")