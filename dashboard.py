import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="Client Dashboard", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0A0A0F; color: #E2E8F0; }
    .stButton>button {
        background: linear-gradient(135deg, #0066FF, #0044CC);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 14px;
    }
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div {
        background-color: #111118 !important;
        color: #E2E8F0 !important;
        border: 1px solid #1E1E2E !important;
        border-radius: 8px !important;
    }
    .metric-card {
        background: #111118;
        border: 1px solid #1E1E2E;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #0066FF;
    }
    .metric-label {
        font-size: 13px;
        color: #64748B;
        margin-top: 4px;
    }
    .client-card {
        background: #111118;
        border: 1px solid #1E1E2E;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 0.8rem;
    }
    .client-card:hover { border-color: #0066FF; }
    .status-active {
        background: #064E3B;
        color: #6EE7B7;
        padding: 3px 10px;
        border-radius: 99px;
        font-size: 12px;
    }
    .status-pending {
        background: #451A03;
        color: #FCD34D;
        padding: 3px 10px;
        border-radius: 99px;
        font-size: 12px;
    }
    .status-completed {
        background: #1E1B4B;
        color: #A5B4FC;
        padding: 3px 10px;
        border-radius: 99px;
        font-size: 12px;
    }
    .status-lead {
        background: #1C1917;
        color: #94A3B8;
        padding: 3px 10px;
        border-radius: 99px;
        font-size: 12px;
    }
    hr { border-color: #1E1E2E !important; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "clients" not in st.session_state:
    st.session_state.clients = []

# Header
st.title("📊 Assyrian AI — Client Dashboard")
st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
st.divider()

# Metrics
total_clients = len(st.session_state.clients)
active = len([c for c in st.session_state.clients if c["status"] == "Active"])
completed = len([c for c in st.session_state.clients if c["status"] == "Completed"])
total_revenue = sum([c["value"] for c in st.session_state.clients if c["status"] in ["Active", "Completed"]])
pending_revenue = sum([c["value"] for c in st.session_state.clients if c["status"] == "Pending payment"])

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{total_clients}</div>
        <div class="metric-label">Total Clients</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{active}</div>
        <div class="metric-label">Active Projects</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{completed}</div>
        <div class="metric-label">Completed</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${total_revenue:,}</div>
        <div class="metric-label">Total Revenue (AUD)</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color:#F59E0B">${pending_revenue:,}</div>
        <div class="metric-label">Pending Payment</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Two columns layout
left, right = st.columns([2, 1])

with right:
    st.subheader("➕ Add New Client")
    with st.container():
        client_name = st.text_input("Business name", placeholder="e.g. SmileCare Dental")
        contact_name = st.text_input("Contact person", placeholder="e.g. Dr. John Smith")
        contact_email = st.text_input("Email", placeholder="info@smilecare.com.au")
        contact_phone = st.text_input("Phone", placeholder="+61 3 9000 0000")
        service = st.selectbox("Service", [
            "Business Chatbot",
            "Document Summarizer",
            "Email Writer",
            "Hotel Reservation Bot",
            "Restaurant Assistant",
            "Real Estate Chatbot",
            "Social Media Writer",
            "FAQ Generator",
            "Business Name Generator",
            "Custom AI Tool"
        ])
        value = st.number_input("Project value (AUD)", min_value=0, value=799, step=50)
        status = st.selectbox("Status", [
            "Lead",
            "Active",
            "Pending payment",
            "Completed"
        ])
        notes = st.text_area("Notes", placeholder="Any important details...", height=80)

        if st.button("➕ Add Client"):
            if client_name.strip() == "":
                st.warning("Please enter a business name.")
            else:
                new_client = {
                    "id": len(st.session_state.clients) + 1,
                    "business": client_name,
                    "contact": contact_name,
                    "email": contact_email,
                    "phone": contact_phone,
                    "service": service,
                    "value": value,
                    "status": status,
                    "notes": notes,
                    "date": datetime.now().strftime("%d %b %Y")
                }
                st.session_state.clients.append(new_client)
                st.success(f"✅ {client_name} added!")
                st.rerun()

with left:
    st.subheader("👥 All Clients")

    if len(st.session_state.clients) == 0:
        st.markdown("""
        <div class="client-card" style="text-align:center; padding:2rem;">
            <p style="color:#475569;">No clients yet — add your first one on the right!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        filter_status = st.selectbox("Filter by status", ["All", "Lead", "Active", "Pending payment", "Completed"])

        filtered = st.session_state.clients
        if filter_status != "All":
            filtered = [c for c in st.session_state.clients if c["status"] == filter_status]

        for i, client in enumerate(filtered):
            status_class = {
                "Active": "status-active",
                "Pending payment": "status-pending",
                "Completed": "status-completed",
                "Lead": "status-lead"
            }.get(client["status"], "status-lead")

            st.markdown(f"""
            <div class="client-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <strong style="color:#F1F5F9; font-size:16px;">{client["business"]}</strong>
                    <span class="{status_class}">{client["status"]}</span>
                </div>
                <div style="font-size:13px; color:#64748B; line-height:2;">
                    👤 {client["contact"]} &nbsp;|&nbsp;
                    📧 {client["email"]} &nbsp;|&nbsp;
                    📞 {client["phone"]}<br>
                    🛠️ {client["service"]} &nbsp;|&nbsp;
                    💰 ${client["value"]:,} AUD &nbsp;|&nbsp;
                    📅 {client["date"]}
                </div>
                {"<div style='margin-top:8px; font-size:13px; color:#94A3B8;'>📝 " + client["notes"] + "</div>" if client["notes"] else ""}
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b = st.columns([1, 4])
            with col_a:
                if st.button("🗑️ Remove", key=f"del_{i}"):
                    st.session_state.clients.pop(i)
                    st.rerun()

st.divider()
st.caption("© 2026 Assyrian · AI Solutions for Melbourne Businesses")