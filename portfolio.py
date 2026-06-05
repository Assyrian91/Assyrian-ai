import streamlit as st
import requests

st.set_page_config(page_title="AI Solutions by Assyrian", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    /* Global dark background */
    .stApp {
        background-color: #0A0A0F;
        color: #E2E8F0;
    }
    .main { max-width: 800px; margin: auto; }

    /* Hero */
    .hero {
        background: linear-gradient(135deg, #0066FF, #0A0A0F 80%);
        border: 1px solid #0066FF;
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 0 40px rgba(0, 102, 255, 0.3);
    }
    .hero h1 { font-size: 2rem; margin-bottom: 0.5rem; color: white; }
    .hero p { font-size: 1.1rem; opacity: 0.85; color: #CBD5E1; }

    /* Cards */
    .card {
        background: #111118;
        border: 1px solid #1E1E2E;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 0 20px rgba(0, 102, 255, 0.05);
        transition: border-color 0.2s;
    }
    .card:hover { border-color: #0066FF; }
    .card h3 { margin-bottom: 0.3rem; color: #F1F5F9; }
    .card p { color: #94A3B8; font-size: 14px; margin-bottom: 1rem; }

    /* Tags */
    .tag {
        display: inline-block;
        background: #0A1628;
        color: #3B82F6;
        border: 1px solid #1E3A5F;
        padding: 3px 10px;
        border-radius: 99px;
        font-size: 12px;
        margin-right: 4px;
    }

    /* Price */
    .price {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0066FF;
    }

    /* Section titles */
    .section-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #F1F5F9;
        margin: 2rem 0 1rem;
        border-left: 3px solid #0066FF;
        padding-left: 12px;
    }

    /* Contact box */
    .contact-box {
        background: #111118;
        border: 1px solid #0066FF;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 102, 255, 0.15);
    }
    .contact-box h3 { color: #F1F5F9; }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #0066FF, #0044CC);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 8px;
        font-size: 15px;
        width: 100%;
        box-shadow: 0 0 15px rgba(0, 102, 255, 0.4);
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0080FF, #0066FF);
        box-shadow: 0 0 25px rgba(0, 102, 255, 0.6);
    }

    /* Input fields */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        background-color: #111118 !important;
        color: #E2E8F0 !important;
        border: 1px solid #1E1E2E !important;
        border-radius: 8px !important;
    }
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #0066FF !important;
        box-shadow: 0 0 10px rgba(0, 102, 255, 0.2) !important;
    }

    /* Divider */
    hr { border-color: #1E1E2E !important; }

    /* Caption */
    .stCaption { color: #475569 !important; }

    /* Glow dot */
    .glow {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: #0066FF;
        border-radius: 50%;
        box-shadow: 0 0 8px #0066FF;
        margin-right: 6px;
        vertical-align: middle;
    }

    /* Demo links */
    .demo-link {
        display: block;
        background: #0A1628;
        border: 1px solid #1E3A5F;
        border-radius: 8px;
        padding: 10px 16px;
        margin-bottom: 8px;
        color: #60A5FA;
        font-size: 14px;
        text-decoration: none;
    }
    .demo-link:hover { border-color: #0066FF; color: #93C5FD; }
    </style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <h1>🤖 AI Solutions by Assyrian</h1>
    <p>I build custom AI tools for Melbourne businesses that save your team 10+ hours every week.<br>
    Chatbots · Content Writing · Document Automation · Social Media</p>
    <br>
    <span style="background:#0066FF22; border:1px solid #0066FF; padding:6px 16px; border-radius:99px; font-size:13px; color:#60A5FA;">
        <span class="glow"></span> Available for new projects
    </span>
</div>
""", unsafe_allow_html=True)

# Stats bar
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.markdown("""
    <div class="card" style="text-align:center; padding:1rem;">
        <div style="font-size:1.8rem; font-weight:700; color:#0066FF;">12+</div>
        <div style="font-size:13px; color:#64748B;">AI Tools Built</div>
    </div>
    """, unsafe_allow_html=True)
with col_s2:
    st.markdown("""
    <div class="card" style="text-align:center; padding:1rem;">
        <div style="font-size:1.8rem; font-weight:700; color:#0066FF;">3-5</div>
        <div style="font-size:13px; color:#64748B;">Days Delivery</div>
    </div>
    """, unsafe_allow_html=True)
with col_s3:
    st.markdown("""
    <div class="card" style="text-align:center; padding:1rem;">
        <div style="font-size:1.8rem; font-weight:700; color:#0066FF;">30</div>
        <div style="font-size:13px; color:#64748B;">Days Free Support</div>
    </div>
    """, unsafe_allow_html=True)

# What I build
st.markdown('<div class="section-title">🛠️ What I Build</div>', unsafe_allow_html=True)

# Row 1
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="card">
        <h3>🤖 Business Chatbot</h3>
        <p>A 24/7 AI assistant trained on your business — answers questions, books appointments and captures leads automatically.</p>
        <span class="tag">Real estate</span>
        <span class="tag">Clinics</span>
        <span class="tag">Restaurants</span>
        <br><br>
        <span class="price">From $799 AUD</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📄 Document Summarizer</h3>
        <p>Upload any PDF or document and get a clear summary instantly. Saves hours of reading for law firms, agencies and consultants.</p>
        <span class="tag">Law firms</span>
        <span class="tag">Finance</span>
        <span class="tag">HR</span>
        <br><br>
        <span class="price">From $599 AUD</span>
    </div>
    """, unsafe_allow_html=True)

# Row 2
col3, col4 = st.columns(2)
with col3:
    st.markdown("""
    <div class="card">
        <h3>✉️ AI Email Writer</h3>
        <p>Turn bullet points into professional emails in seconds. Supports multiple tones and languages including Arabic.</p>
        <span class="tag">Sales teams</span>
        <span class="tag">Agencies</span>
        <span class="tag">Freelancers</span>
        <br><br>
        <span class="price">From $499 AUD</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>🏨 Hotel Reservation Bot</h3>
        <p>A smart concierge that handles room inquiries, bookings and guest questions around the clock.</p>
        <span class="tag">Hotels</span>
        <span class="tag">Serviced apartments</span>
        <span class="tag">B&Bs</span>
        <br><br>
        <span class="price">From $999 AUD</span>
    </div>
    """, unsafe_allow_html=True)

# Row 3
col5, col6 = st.columns(2)
with col5:
    st.markdown("""
    <div class="card">
        <h3>🍽️ Restaurant Assistant</h3>
        <p>Handles table reservations, menu questions, dietary needs and special occasion requests — 24/7.</p>
        <span class="tag">Restaurants</span>
        <span class="tag">Cafes</span>
        <span class="tag">Catering</span>
        <br><br>
        <span class="price">From $849 AUD</span>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <h3>📱 Social Media Caption Writer</h3>
        <p>Generate engaging captions for Instagram, Facebook, LinkedIn and TikTok instantly. Supports Melbourne focused hashtags.</p>
        <span class="tag">Instagram</span>
        <span class="tag">Facebook</span>
        <span class="tag">LinkedIn</span>
        <br><br>
        <span class="price">From $399 AUD</span>
    </div>
    """, unsafe_allow_html=True)

# Row 4
col7, col8 = st.columns(2)
with col7:
    st.markdown("""
    <div class="card">
        <h3>🏷️ Business Name Generator</h3>
        <p>Generate creative business names and catchy slogans tailored to your industry, style and Melbourne market.</p>
        <span class="tag">Startups</span>
        <span class="tag">Rebranding</span>
        <span class="tag">New ventures</span>
        <br><br>
        <span class="price">From $299 AUD</span>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown("""
    <div class="card">
        <h3>❓ FAQ Generator</h3>
        <p>Generate professional FAQs for your website instantly. Saves hours of writing and covers every question customers ask.</p>
        <span class="tag">Websites</span>
        <span class="tag">E-commerce</span>
        <span class="tag">Any business</span>
        <br><br>
        <span class="price">From $299 AUD</span>
    </div>
    """, unsafe_allow_html=True)

# Row 5
col9, col10 = st.columns(2)
with col9:
    st.markdown("""
    <div class="card">
        <h3>✍️ Blog Post Writer</h3>
        <p>Generate full SEO-optimised blog posts for any business in seconds. Drives organic traffic and builds authority online.</p>
        <span class="tag">SEO</span>
        <span class="tag">Content marketing</span>
        <span class="tag">Any industry</span>
        <br><br>
        <span class="price">From $349 AUD</span>
    </div>
    """, unsafe_allow_html=True)

with col10:
    st.markdown("""
    <div class="card">
        <h3>🛍️ Product Description Writer</h3>
        <p>Generate compelling product descriptions that convert browsers into buyers. Optimised for Shopify, Amazon, eBay and more.</p>
        <span class="tag">Shopify</span>
        <span class="tag">Amazon</span>
        <span class="tag">E-commerce</span>
        <br><br>
        <span class="price">From $349 AUD</span>
    </div>
    """, unsafe_allow_html=True)

# Row 6
col11, col12 = st.columns(2)
with col11:
    st.markdown("""
    <div class="card">
        <h3>🏠 Real Estate Chatbot</h3>
        <p>AI property assistant that covers 30+ Melbourne suburbs, guides first home buyers and books inspections automatically.</p>
        <span class="tag">Real estate</span>
        <span class="tag">Property management</span>
        <span class="tag">Melbourne</span>
        <br><br>
        <span class="price">From $799 AUD</span>
    </div>
    """, unsafe_allow_html=True)

with col12:
    st.markdown("""
    <div class="card">
        <h3>⚙️ Custom AI Tool</h3>
        <p>Have a specific problem? I will build a custom AI solution tailored to your workflow, team and industry.</p>
        <span class="tag">Any industry</span>
        <span class="tag">Any size</span>
        <br><br>
        <span class="price">From $1,199 AUD</span>
    </div>
    """, unsafe_allow_html=True)

# Why work with me
st.markdown('<div class="section-title">✅ Why Work With Me</div>', unsafe_allow_html=True)

col13, col14, col15 = st.columns(3)
with col13:
    st.markdown("""
    <div class="card" style="text-align:center">
        <h3>⚡ Fast</h3>
        <p>Most tools delivered within 3–5 business days</p>
    </div>
    """, unsafe_allow_html=True)

with col14:
    st.markdown("""
    <div class="card" style="text-align:center">
        <h3>💰 Affordable</h3>
        <p>Flat fees — no hidden costs or hourly billing surprises</p>
    </div>
    """, unsafe_allow_html=True)

with col15:
    st.markdown("""
    <div class="card" style="text-align:center">
        <h3>🔧 Supported</h3>
        <p>30 days free support after every delivery</p>
    </div>
    """, unsafe_allow_html=True)

# Live demos
st.markdown('<div class="section-title">🚀 Live Demos</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>Try my tools live</h3>
    <p>These are real working demos — the same quality you would get for your Melbourne business.</p>
    <p style="color:#64748B; font-size:13px; margin-bottom:12px;">Run any demo by typing in your terminal:</p>
    <span class="demo-link">✉️ Email Writer &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run email_app.py</code></span>
    <span class="demo-link">📄 Document Summarizer &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run summarizer_app.py</code></span>
    <span class="demo-link">🦷 Dental Clinic Chatbot &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run dental_app.py</code></span>
    <span class="demo-link">🏨 Hotel Reservation Bot &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run hotel_app.py</code></span>
    <span class="demo-link">🍽️ Restaurant Assistant &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run restaurant_app.py</code></span>
    <span class="demo-link">🏠 Real Estate Chatbot &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run chatbot_app.py</code></span>
    <span class="demo-link">📱 Social Media Writer &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run social_media_app.py</code></span>
    <span class="demo-link">🏷️ Business Name Generator &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run business_name_app.py</code></span>
    <span class="demo-link">❓ FAQ Generator &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run faq_generator_app.py</code></span>
    <span class="demo-link">✍️ Blog Post Writer &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run blog_writer_app.py</code></span>
    <span class="demo-link">🛍️ Product Description Writer &nbsp;→&nbsp; <code style="color:#94A3B8;">streamlit run product_description_app.py</code></span>
</div>
""", unsafe_allow_html=True)

# Contact
st.markdown('<div class="section-title">📬 Get In Touch</div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">
    <h3>Ready to save 10+ hours a week?</h3>
    <p style="color:#94A3B8; margin-bottom: 1rem;">Book a free 15 minute call with Assyrian and I will show you exactly what I can build for your Melbourne business.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

contact_name = st.text_input("Your name")
contact_email = st.text_input("Your email")
contact_message = st.text_area("Tell me about your business", placeholder="e.g. I run a dental clinic in Melbourne and need a chatbot...")

if st.button("📩 Send Message"):
    if contact_name and contact_email and contact_message:
        with st.spinner("Sending your message..."):
            try:
                response = requests.post(
                    "https://formspree.io/f/meewqpqn",
                    data={
                        "name": contact_name,
                        "email": contact_email,
                        "message": contact_message
                    },
                    headers={"Accept": "application/json"}
                )
                if response.status_code == 200:
                    st.success(f"Thanks {contact_name}! Your message was sent — Assyrian will get back to you within 24 hours. 🎉")
                    st.balloons()
                else:
                    st.error("Something went wrong. Please email me directly.")
            except Exception as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please fill in all fields before sending.")

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses · Built with Python & Streamlit")