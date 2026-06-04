import streamlit as st
from groq import Groq
import pypdf
import io
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
st.set_page_config(page_title="AI Document Summarizer", page_icon="📄", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #0F766E;
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover { background-color: #0D9488; }
    </style>
""", unsafe_allow_html=True)

def summarize_text(text, style, language):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a professional document summarizer. Always respond in the language specified by the user."
            },
            {
                "role": "user",
                "content": f"""Summarize the following text in {style} style.
Respond in {language}.

{text}

Be accurate, clear and concise."""
            }
        ]
    )
    return response.choices[0].message.content

st.title("📄 AI Document Summarizer")
st.caption("Upload a PDF or paste text — get a clear summary instantly.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("Summary style", [
        "bullet points",
        "short paragraph",
        "executive summary",
        "simple plain english"
    ])

with col2:
    language = st.selectbox("Output language", [
        "English",
        "Arabic",
        "French",
        "Spanish"
    ])

tab1, tab2 = st.tabs(["📂 Upload PDF", "📋 Paste Text"])

with tab1:
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_reader = pypdf.PdfReader(io.BytesIO(uploaded_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        st.success(f"✅ PDF loaded — {len(pdf_reader.pages)} pages, {len(text)} characters")
        if st.button("📄 Summarize PDF"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(text[:8000], style, language)
            st.divider()
            st.subheader("Summary")
            st.write(summary)
            st.download_button(
                label="⬇️ Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

with tab2:
    pasted_text = st.text_area(
        "Paste your text here",
        placeholder="Paste any document, article, report or email...",
        height=200
    )
    if st.button("📋 Summarize Text"):
        if pasted_text.strip() == "":
            st.warning("Please paste some text first.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_text(pasted_text, style, language)
            st.divider()
            st.subheader("Summary")
            st.write(summary)
            st.download_button(
                label="⬇️ Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

st.divider()
st.caption("Built with AI · Contact us to get this for your business")
