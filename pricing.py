import streamlit as st
import requests

st.set_page_config(page_title="Pricing — AI Solutions by Assyrian", page_icon="💰", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #0066FF, #0044CC);
        color: white;
        border: none;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 15px;
        width: 100%;
        box-shadow: 0 0 15px rgba(0, 102, 255, 0.4);
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(0, 102, 255, 0.6);
    }
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        background-color: #111118 !important;
        color: #E2E8F0 !important;
        border: 1px solid #1E1E2E !important;
        border-radius: 8px !important;
    }
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
    .hero h1 { font-size: 2rem; color: white; margin-bottom: 0.5rem; }
    .hero p { color: #CBD5E1; font-size: 1rem; }
    .pricing-card {
        background: #111118;
        border: 1px solid #1E1E2E;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1rem;
        text-align: center;
        transition: all 0.2s;
    }
    .pricing-card:hover { border-color: #0066FF; box-shadow: 0 0 30px rgba(0,102,255,0.1); }
    .pricing-card.popular {
        border-color: #0066FF;
        box-shadow: 0 0 30px rgba(0, 102, 255, 0.2);
    }
    .popular-badge {
        background: #0066FF;
        color: white;
        padding: 4px 14px;
        border-radius: 99px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .plan-name {
        font-size: 1.3rem;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 0.3rem;
    }
    .plan-price {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0066FF;
        margin: 0.5rem 0;
    }
    .plan-price span {
        font-size: 1rem;
        font-weight: 400;
        color: #64748B;
    }
    .plan-desc {
        color: #94A3B8;
        font-size: 14px;
        margin-bottom: 1.5rem;
    }
    .feature {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 0;
        font-size: 14px;
        color: #CBD5E1;
        text-align: left;
    }
    .feature-check { color: #22C55E; font-size: 16px; }
    .feature-x { color: #475569; font-size: 16px; }
    .section-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #F1F5F9;
        margin: 2rem 0 1rem;
        border-left: 3px solid #0066FF;
        padding-left: 12px;
    }
    .addon-card {
        background: #111118;
        border: 1px solid #1E1E2E;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 0.8rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .addon-card:hover { border-color: #0066FF; }
    .addon-name { font-size: 14px; color: #F1F5F9; font-weight: 500; }
    .addon-desc { font-size: 12px; color: #64748B; margin-top: 2px; }
    .addon-price { font-size: 1.1rem; font-weight: 700; color: #0066FF; white-space: nowrap; }
    .faq-card {
        background: #111118;
        border: 1px solid #1E1E2E;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 0.8rem;
    }
    .faq-q { font-size: 14px; font-weight: 600; color: #F1F5F9; margin-bottom: 6px; }
    .faq-a { font-size: 13px; color: #94A3B8; line-height: 1.6; }
    .contact-box {
        background: #111118;
        border: 1px solid #0066FF;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 102, 255, 0.15);
    }
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
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <h1>💰 Simple, Transparent Pricing</h1>
    <p>No hidden fees. No hourly billing surprises. Just flat rates and real results.<br>
    All prices in Australian Dollars (AUD).</p>
    <br>
    <span style="background:#0066FF22; border:1px solid #0066FF; padding:6px 16px; border-radius:99px; font-size:13px; color:#60A5FA;">
        <span class="glow"></span> Free 15 minute consultation included with every plan
    </span>
</div>
""", unsafe_allow_html=True)

# Pricing plans
st.markdown('<div class="section-title">📦 Packages</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="pricing-card">
        <div class="plan-name">🚀 Starter</div>
        <div class="plan-price">$799 <span>AUD</span></div>
        <div class="plan-desc">Perfect for small businesses getting started with AI</div>
        <div class="feature"><span class="feature-check">✓</span> 1 custom AI chatbot</div>
        <div class="feature"><span class="feature-check">✓</span> Trained on your business</div>
        <div class="feature"><span class="feature-check">✓</span> Deployed online</div>
        <div class="feature"><span class="feature-check">✓</span> 30 days support</div>
        <div class="feature"><span class="feature-check">✓</span> 3–5 day delivery</div>
        <div class="feature"><span class="feature-x">✗</span> Content tools</div>
        <div class="feature"><span class="feature-x">✗</span> Monthly retainer</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pricing-card popular">
        <div class="popular-badge">⭐ Most Popular</div>
        <div class="plan-name">💼 Growth</div>
        <div class="plan-price">$1,499 <span>AUD</span></div>
        <div class="plan-desc">For businesses ready to automate multiple workflows</div>
        <div class="feature"><span class="feature-check">✓</span> 1 custom AI chatbot</div>
        <div class="feature"><span class="feature-check">✓</span> Email writer tool</div>
        <div class="feature"><span class="feature-check">✓</span> FAQ generator</div>
        <div class="feature"><span class="feature-check">✓</span> Social media writer</div>
        <div class="feature"><span class="feature-check">✓</span> 60 days support</div>
        <div class="feature"><span class="feature-check">✓</span> 3–5 day delivery</div>
        <div class="feature"><span class="feature-x">✗</span> Monthly retainer</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="pricing-card">
        <div class="plan-name">🏆 Full Suite</div>
        <div class="plan-price">$2,499 <span>AUD</span></div>
        <div class="plan-desc">Everything you need to fully automate your business</div>
        <div class="feature"><span class="feature-check">✓</span> 1 custom AI chatbot</div>
        <div class="feature"><span class="feature-check">✓</span> All content tools</div>
        <div class="feature"><span class="feature-check">✓</span> Blog post writer</div>
        <div class="feature"><span class="feature-check">✓</span> Product description writer</div>
        <div class="feature"><span class="feature-check">✓</span> 90 days support</div>
        <div class="feature"><span class="feature-check">✓</span> Priority delivery</div>
        <div class="feature"><span class="feature-check">✓</span> Monthly retainer included</div>
    </div>
    """, unsafe_allow_html=True)

# Monthly retainers
st.markdown('<div class="section-title">🔄 Monthly Retainers</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
    <div class="pricing-card">
        <div class="plan-name">🛠️ Basic Retainer</div>
        <div class="plan-price">$199 <span>AUD/mo</span></div>
        <div class="plan-desc">Keep your tools updated and running perfectly</div>
        <div class="feature"><span class="feature-check">✓</span> Monthly chatbot updates</div>
        <div class="feature"><span class="feature-check">✓</span> Priority support</div>
        <div class="feature"><span class="feature-check">✓</span> Performance report</div>
        <div class="feature"><span class="feature-check">✓</span> Bug fixes included</div>
        <div class="feature"><span class="feature-x">✗</span> Content creation</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="pricing-card popular">
        <div class="popular-badge">⭐ Best Value</div>
        <div class="plan-name">🚀 Pro Retainer</div>
        <div class="plan-price">$399 <span>AUD/mo</span></div>
        <div class="plan-desc">Full ongoing support plus monthly content creation</div>
        <div class="feature"><span class="feature-check">✓</span> Everything in Basic</div>
        <div class="feature"><span class="feature-check">✓</span> 4 social media captions/week</div>
        <div class="feature"><span class="feature-check">✓</span> 2 blog posts/month</div>
        <div class="feature"><span class="feature-check">✓</span> Quarterly tool upgrade</div>
        <div class="feature"><span class="feature-check">✓</span> Dedicated support line</div>
    </div>
    """, unsafe_allow_html=True)

# Add-ons
st.markdown('<div class="section-title">⚡ Individual Tools</div>', unsafe_allow_html=True)

addons = [
    ("🤖 Business Chatbot", "Custom AI assistant for your website", "$799 AUD"),
    ("📄 Document Summarizer", "PDF and document summarization tool", "$599 AUD"),
    ("✉️ AI Email Writer", "Multi-tone, multi-language email writer", "$499 AUD"),
    ("🏨 Hotel Reservation Bot", "24/7 AI concierge for hotels", "$999 AUD"),
    ("🍽️ Restaurant Assistant", "Reservations and menu chatbot", "$849 AUD"),
    ("🏠 Real Estate Chatbot", "Property assistant for Melbourne agencies", "$799 AUD"),
    ("📱 Social Media Writer", "Instagram, Facebook and LinkedIn captions", "$399 AUD"),
    ("✍️ Blog Post Writer", "SEO-optimised blog posts for any industry", "$349 AUD"),
    ("🛍️ Product Description Writer", "Shopify, Amazon and eBay descriptions", "$349 AUD"),
    ("❓ FAQ Generator", "Professional FAQ section for your website", "$299 AUD"),
    ("🏷️ Business Name Generator", "Creative names and slogans", "$299 AUD"),
    ("⚙️ Custom AI Tool", "Fully custom solution for your business", "From $1,199 AUD"),
]

for name, desc, price in addons:
    st.markdown(f"""
    <div class="addon-card">
        <div>
            <div class="addon-name">{name}</div>
            <div class="addon-desc">{desc}</div>
        </div>
        <div class="addon-price">{price}</div>
    </div>
    """, unsafe_allow_html=True)

# FAQ
st.markdown('<div class="section-title">❓ Frequently Asked Questions</div>', unsafe_allow_html=True)

faqs = [
    ("How long does delivery take?", "Most tools are delivered within 3–5 business days. Complex custom projects may take up to 7 days. You will always get a clear timeline before we start."),
    ("Do I need to pay upfront?", "Yes — full payment is required before work begins. This ensures commitment from both sides and allows me to prioritize your project."),
    ("What if I am not happy with the result?", "I offer unlimited revisions within 30 days of delivery. Your satisfaction is guaranteed — I will keep refining until you are happy."),
    ("How do I embed the chatbot on my website?", "I provide a simple embed code you paste into your website. It works with any website builder including WordPress, Wix, Squarespace and Shopify."),
    ("Do you offer a free trial?", "I offer a free 15 minute consultation call where I show you a live demo similar to your business. No obligation — just a real look at what is possible."),
    ("Can I upgrade my plan later?", "Absolutely — you can upgrade from Starter to Growth or Full Suite at any time. You only pay the difference."),
    ("What payment methods do you accept?", "Bank transfer, PayPal and Stripe. Payment details are provided after your consultation call."),
]

for q, a in faqs:
    st.markdown(f"""
    <div class="faq-card">
        <div class="faq-q">❓ {q}</div>
        <div class="faq-a">{a}</div>
    </div>
    """, unsafe_allow_html=True)

# CTA
st.markdown('<div class="section-title">📬 Get Started Today</div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">
    <h3 style="color:#F1F5F9;">Not sure which plan is right for you?</h3>
    <p style="color:#94A3B8; margin-bottom: 1rem;">Book a free 15 minute call with Assyrian — I will recommend the best option for your business and budget.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

contact_name = st.text_input("Your name")
contact_email = st.text_input("Your email")
plan_interest = st.selectbox("Which plan interests you?", [
    "Not sure yet — need advice",
    "Starter — $799 AUD",
    "Growth — $1,499 AUD",
    "Full Suite — $2,499 AUD",
    "Basic Retainer — $199/month",
    "Pro Retainer — $399/month",
    "Individual tool"
])
contact_message = st.text_area("Tell me about your business", placeholder="e.g. I run a dental clinic in Melbourne with 3 staff and want to reduce front desk calls...")

if st.button("📩 Book Free Consultation"):
    if contact_name and contact_email and contact_message:
        with st.spinner("Sending your request..."):
            try:
                response = requests.post(
                    "https://formspree.io/f/meewqpqn",
                    data={
                        "name": contact_name,
                        "email": contact_email,
                        "plan": plan_interest,
                        "message": contact_message
                    },
                    headers={"Accept": "application/json"}
                )
                if response.status_code == 200:
                    st.success(f"Thanks {contact_name}! Assyrian will get back to you within 24 hours to book your free call. 🎉")
                    st.balloons()
                else:
                    st.error("Something went wrong. Please try again.")
            except Exception as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please fill in all fields.")

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses · ashuraya-ai.streamlit.app")