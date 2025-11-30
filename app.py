import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import tensorflow as tf
import os

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="NIDS_FORENSIC_TOOL", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SESSION STATE (Navigation Logic)
if 'page' not in st.session_state:
    st.session_state.page = "DASHBOARD"

def set_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# 3. LOAD RESOURCES
@st.cache_resource 
def load_system():
    try:
        model = tf.keras.models.load_model("nids_autoencoder.keras")
        scaler = joblib.load("scaler.save")
        return model, scaler
    except Exception as e:
        return None, None

model, scaler = load_system()

# 4. NOTHING OS STYLING (CSS)
st.markdown("""
<style>
    /* GLOBAL FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;500;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto Mono', 'Courier New', monospace !important;
        color: #000000;
    }
    .stApp { background-color: #e6e6e6; }

    /* HIDE DEFAULT HEADER ELEMENTS */
    header[data-testid="stHeader"] { background-color: transparent !important; }
    div[data-testid="stDecoration"] { display: none; }
    
    /* LAYOUT SPACING */
    .block-container {
        padding-top: 2rem !important; 
        padding-left: 3rem;
        padding-right: 3rem;
        padding-bottom: 3rem;
    }

    /* NAVIGATION BUTTON STYLING */
    /* This targets the buttons in the top row specifically */
    div[data-testid="stHorizontalBlock"]:nth-of-type(1) button {
        background-color: transparent !important;
        border: none !important;
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important; /* Slightly smaller for better fit */
        text-transform: uppercase;
        margin-top: 10px;
        width: 100%;
        white-space: nowrap !important;
        padding: 0px !important;
    }
    div[data-testid="stHorizontalBlock"]:nth-of-type(1) button:hover {
        color: #D71920 !important; /* Red Hover */
        text-decoration: underline !important; /* FIXED: Line goes under */
        text-underline-offset: 5px; /* FIXED: Pushes line down away from text */
        text-decoration-thickness: 2px;
        box-shadow: none !important;
    }
    div[data-testid="stHorizontalBlock"]:nth-of-type(1) button:focus {
        color: #D71920 !important;
        outline: none !important;
        text-decoration: underline !important;
    }

    /* TYPOGRAPHY */
    .big-title {
        font-size: 2.2rem !important; 
        font-weight: 900 !important;
        color: #000000 !important;    
        letter-spacing: -1.5px;
        line-height: 1.0;
        white-space: nowrap;
    }
    .subtitle {
        font-size: 0.9rem;
        font-weight: 500;
        color: #444;
        letter-spacing: 1px;
    }
    
    .status-text {
        font-size: 1.1rem;
        font-weight: 700;
        color: #000000 !important;    
        text-align: right;
        margin-top: 10px; 
    }

    /* SHARP EDGES GLOBAL */
    div, button, input, select, textarea, div[data-testid="stMetric"], div[data-testid="stAlert"] {
        border-radius: 0px !important;
    }

    /* SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #d9d9d9;
        border-right: 2px solid #000000;
        top: 0rem !important; 
    }
    section[data-testid="stSidebar"] h2 { color: #000000 !important; }
    button[data-testid="stSidebarCollapseButton"] svg, 
    button[data-testid="stSidebarExpandButton"] svg {
        fill: #000000 !important; color: #000000 !important;
    }

    /* METRICS & WIDGETS */
    div[data-testid="stMetric"] {
        background-color: #f2f2f2;
        border: 1px solid #000000;
        box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
        padding: 10px;
    }
    div[data-testid="stMetric"] label, div[data-testid="stMetricValue"] { color: #000000 !important; }
    div[data-testid="stSlider"] p, div[data-testid="stMarkdownContainer"] p { color: #000000 !important; }
    h3 { color: #000000 !important; }

    /* ACTION BUTTONS (Download, etc - NOT Header) */
    div:not([data-testid="stHorizontalBlock"]:nth-of-type(1)) > div.stButton > button {
        background-color: #000000;
        color: #f2f2f2;
        border: 1px solid #000000;
        text-transform: uppercase;
        font-weight: 700;
    }
    div:not([data-testid="stHorizontalBlock"]:nth-of-type(1)) > div.stButton > button:hover {
        background-color: #D71920; 
        border-color: #D71920;
    }

    /* AWAITING BOX */
    .awaiting-box {
        border: 1px solid #000000;
        color: #ff6600; 
        padding: 40px;
        text-align: center;
        font-weight: 700;
        letter-spacing: 1px;
        background-color: transparent;
        margin-top: 40px;
        width: 100%;
    }
    
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 5. NAVIGATION BAR (Top Right)
c_spacer, c_nav1, c_nav2, c_nav3, c_nav4 = st.columns([5, 1.2, 1.2, 1.2, 1.2])

with c_spacer:
    st.write("") 
with c_nav1:
    if st.button("DASHBOARD"): set_page("DASHBOARD")
with c_nav2:
    if st.button("HISTORY"): set_page("HISTORY")
with c_nav3:
    if st.button("SETTINGS"): set_page("SETTINGS")
with c_nav4:
    if st.button("LOGOUT"): set_page("LOGOUT")


# 6. PAGE CONTENT
if st.session_state.page == "DASHBOARD":
    
    st.markdown("---") 

    # --- TITLE ROW ---
    col_title, col_status = st.columns([2, 1])
    with col_title:
        st.markdown('<div class="big-title">NIDS.OS // SYSTEM_ACTIVE</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">DETECTING_ANOMALIES_IN_REALTIME...</div>', unsafe_allow_html=True)
    with col_status:
        st.markdown('<div class="status-text">[ SYSTEM_LOAD : NOMINAL ]</div>', unsafe_allow_html=True)
    
    st.markdown("---")

    # SIDEBAR
    st.sidebar.markdown("## // CONFIGURATION")
    uploaded_file = st.sidebar.file_uploader("INPUT_SOURCE [.CSV]", type=["csv"])
    threshold = st.sidebar.slider("SENSITIVITY_THRESHOLD", 0.0, 0.1, 0.05, 0.001)
    st.sidebar.markdown("---")
    st.sidebar.markdown("SYSTEM_STATUS: **ONLINE**")
    st.sidebar.markdown("VERSION: **5.4.0**")

    # NIDS LOGIC
    if model is None or scaler is None:
        st.error("CRITICAL ERROR: 'nids_autoencoder.keras' or 'scaler.save' not found. Please run training first.")
        st.stop()

    if uploaded_file is not None:
        try:
            df_test = pd.read_csv(uploaded_file)
            input_data = df_test.values
            try:
                x_test = scaler.transform(input_data)
            except ValueError:
                st.error("DATA MISMATCH: Input columns do not match training data.")
                st.stop()

            reconstructions = model.predict(x_test)
            mse = np.mean(np.power(x_test - reconstructions, 2), axis=1)
            anomalies = mse > threshold
            num_anomalies = np.sum(anomalies)
            attack_ratio = (num_anomalies / len(df_test)) * 100

            st.markdown("### // ANALYSIS_REPORT")
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("TOTAL_FLOWS", len(df_test))
            with col2: st.metric("ANOMALIES_DETECTED", num_anomalies)
            with col3: st.metric("THREAT_LEVEL", f"{attack_ratio:.2f}%")

            st.markdown("<br>### // VISUAL_FEED", unsafe_allow_html=True)
            plt.style.use('grayscale')
            fig, ax = plt.subplots(figsize=(10, 3.5))
            fig.patch.set_facecolor('#e6e6e6')
            ax.set_facecolor('#e6e6e6')
            
            ax.scatter(range(len(mse)), mse, s=15, color="#666666", alpha=0.5, label="SIGNAL")
            attack_indices = np.where(anomalies)[0]
            if len(attack_indices) > 0:
                ax.scatter(attack_indices, mse[anomalies], s=30, color="#D71920", label="THREAT")
            
            ax.axhline(y=threshold, color='black', linestyle='-', linewidth=1.5, label="LIMIT")
            ax.set_yscale('log')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(True, linestyle='--', alpha=0.4, color='#000000')
            for label in (ax.get_xticklabels() + ax.get_yticklabels()):
                label.set_fontname('Courier New')
                label.set_fontsize(8)
            st.pyplot(fig)

            if num_anomalies > 0:
                st.markdown("### // FORENSIC_LOGS")
                attack_df = df_test[anomalies]
                st.dataframe(attack_df, use_container_width=True)
                csv = attack_df.to_csv(index=False).encode('utf-8')
                st.download_button("DOWNLOAD_LOGS [.CSV]", csv, "threat_report.csv", "text/csv", key='download-csv')
            else:
                st.success("SYSTEM CLEAN: NO THREATS DETECTED.")
        except Exception as e:
            st.error(f"ERROR READING FILE: {e}")
    else:
        st.markdown("""<div class="awaiting-box">AWAITING_INPUT: UPLOAD .CSV TO INITIATE SCAN</div>""", unsafe_allow_html=True)

# --- OTHER PAGES ---
elif st.session_state.page == "HISTORY":
    st.markdown("---")
    st.markdown('<div class="big-title">ARCHIVE_LOGS</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### // PREVIOUS_SCANS")
    history_data = pd.DataFrame({
        'DATE': ['2023-11-20', '2023-11-21', '2023-11-22'],
        'FILE': ['monday_capture.pcap', 'tuesday_test.csv', 'wednesday_dos.csv'],
        'THREAT_LEVEL': ['0.00%', '0.05%', '18.63%'],
        'STATUS': ['CLEAN', 'WARNING', 'CRITICAL']
    })
    st.dataframe(history_data, use_container_width=True)
    st.info("ARCHIVE DATA IS READ-ONLY.")

elif st.session_state.page == "SETTINGS":
    st.markdown("---")
    st.markdown('<div class="big-title">SYSTEM_CONFIG</div>', unsafe_allow_html=True)
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### // CORE_SETTINGS")
        st.toggle("ENABLE_DEEP_PACKET_INSPECTION", value=True)
        st.toggle("AUTO_BLOCK_MALICIOUS_IPS", value=False)
    with c2:
        st.markdown("### // NOTIFICATIONS")
        st.toggle("EMAIL_ALERTS", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("RESET_SYSTEM_PARAMETERS"):
        st.toast("SYSTEM RESET INITIATED...", icon="⚠️")

elif st.session_state.page == "LOGOUT":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; border: 1px solid black; padding: 50px;">
        <h2>SESSION_TERMINATED</h2>
        <p>SECURE CONNECTION CLOSED.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("RECONNECT_SYSTEM"):
        set_page("DASHBOARD")