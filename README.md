# 🧠 Assyrian AI — AI-Powered Business Tools Suite

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

🔗 **Live Demo:** [ashuraya-ai.streamlit.app](https://ashuraya-ai.streamlit.app/)

A collection of AI-powered micro-tools built with Streamlit, designed to help small businesses automate everyday content and customer-facing tasks — from writing blog posts to running a niche chatbot for hotels, dental clinics, and restaurants.

---

## ✨ What's Inside

| Tool | Description |
|---|---|
| 💬 Chatbot | General-purpose AI chatbot assistant |
| ✍️ Blog Writer | Generates blog posts from a topic/prompt |
| 🛍️ Product Description Writer | Auto-generates product copy for e-commerce |
| 📱 Social Media Writer | Creates social media captions/posts |
| 🏷️ Business Name Generator | Suggests business names based on input criteria |
| ❓ FAQ Generator | Builds FAQ sections for a business or product |
| 📝 Summarizer | Summarizes long-form text into key points |
| 📧 Email Writer | Drafts business/marketing emails |
| 🏨 Hotel Assistant App | Niche AI assistant tailored for hotel businesses |
| 🦷 Dental Clinic App | Niche AI assistant tailored for dental clinics |
| 🍽️ Restaurant App | Niche AI assistant tailored for restaurants |
| 📊 Client Dashboard | Dashboard view for managing/tracking client tools |
| 💼 Portfolio & Pricing | Public-facing portfolio and pricing page for the suite |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Assyrian91/Assyrian-ai.git
cd Assyrian-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run any app
```bash
streamlit run portfolio.py
```
Swap `portfolio.py` for any other app file (e.g. `chatbot_app.py`, `hotel_app.py`, `blog_writer_app.py`) to launch that specific tool.

---

## 📁 Project Structure
```
Assyrian-ai/
├── portfolio.py                 # Main portfolio / landing page
├── pricing.py                   # Pricing page
├── dashboard.py                 # Client dashboard
├── chatbot_app.py                # General AI chatbot
├── blog_writer_app.py            # Blog post generator
├── product_description_app.py    # Product description generator
├── social_media_app.py           # Social media content generator
├── business_name_app.py          # Business name generator
├── faq_generator_app.py          # FAQ generator
├── summarizer_app.py             # Text summarizer
├── email_app.py                  # Email writer
├── hotel_app.py                  # Hotel niche assistant
├── dental_app.py / dental_app1.py # Dental clinic niche assistant
├── restaurant_app.py             # Restaurant niche assistant
├── onboarding_template.txt       # Client onboarding template
├── requirements.txt              # Dependencies
└── .devcontainer/                # Dev container config
```

---

## 🛠️ Tech Stack
- **Python** + **Streamlit** for all app UIs
- AI integration for content generation and chat (model/provider used in each app)

---

## 📝 License
MIT — free to use, modify, and distribute.

Built by **Khoshaba Odeesho**
