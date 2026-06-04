import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
st.set_page_config(page_title="AI Email Writer", page_icon="✉️", layout="centered")

st.markdown("""
    <style>
    .main { max-width: 700px; margin: auto; }
    .stButton>button {
        width: 100%;
        background-color: #4F46E5;
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover { background-color: #4338CA; }
    </style>
""", unsafe_allow_html=True)

st.title("✉️ AI Email Writer")
st.caption("Turn bullet points into a professional email in seconds.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox("Email tone", [
        "Professional",
        "Friendly",
        "Follow-up",
        "Cold outreach"
    ])

with col2:
    language = st.selectbox("Language", [
        "English",
        "Arabic",
        "French",
        "Spanish"
    ])

bullet_points = st.text_area(
    "Your bullet points",
    placeholder="- Meeting on Tuesday at 3pm\n- Discuss Q4 budget\n- Bring sales report",
    height=150
)

context = st.text_input(
    "Extra context (optional)",
    placeholder="e.g. This is for a new client I met at a conference"
)

if st.button("✉️ Write Email"):
    if bullet_points.strip() == "":
        st.warning("Please enter at least one bullet point.")
    else:
        with st.spinner("Writing your email..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional email writer. Write clear, concise and effective emails based on bullet points. Always write in the language specified by the user."
                    },
                    {
                        "role": "user",
                        "content": f"""Write a {tone.lower()} email in {language} based on these points:

{bullet_points}

Extra context: {context}

Format with subject line, greeting, body and sign-off."""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.success("Email ready!")
        st.divider()
        st.text_area("Your Email", value=result, height=300)
        st.download_button(
            label="Download Email",
            data=result,
            file_name="email.txt",
            mime="text/plain"
        )

st.divider()
st.caption("Built with AI · Contact us to get this for your business")
