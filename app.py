import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from prediction import predict_future
from anomaly import detect_anomalies
from utils import generate_insights

st.set_page_config(page_title="AI Smart Dashboard", layout="wide")

# Session state
if "data_uploaded" not in st.session_state:
    st.session_state.data_uploaded = False

# ------------------ PAGE 1 ------------------
if not st.session_state.data_uploaded:
    st.title("🚀 AI Smart Dashboard")
    st.markdown("### 📂 Upload your dataset")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview:", df.head())

        if st.button("🔍 Analyze Data"):
            st.session_state.df = df
            st.session_state.data_uploaded = True
            st.rerun()

# ------------------ PAGE 2 ------------------
else:
    df = st.session_state.df

    st.title("📊 Dashboard")

    if st.button("⬅️ Upload New File"):
        st.session_state.data_uploaded = False
        st.rerun()

    column = st.selectbox("Select column", df.columns[1:])

    # Visualization
    st.subheader("📈 Visualization")

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        plt.figure(figsize=(8, 4))
        plt.plot(df[column])
        plt.title("Data Visualization")
        plt.xlabel("Index")
        plt.ylabel(column)
        st.pyplot(plt)

    # Prediction
    st.subheader("🔮 Prediction")
    pred = predict_future(df[column])
    st.line_chart(pred)

    # Anomaly
    st.subheader("⚠️ Anomaly Detection")
    anomalies = detect_anomalies(df[column])

    if anomalies:
        st.error(f"Anomalies detected: {anomalies}")
    else:
        st.success("No anomalies detected ✅")

    # Insights
    st.subheader("🤖 AI Insights")
    insights = generate_insights(df[column])
    st.info(insights)

# ------------------ FOOTER (FOR BOTH PAGES) ------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <h4>👨‍💻 Made by Harshit Singh</h4>
        <p>
            🔗 <a href="https://www.linkedin.com/in/harshitsinghnitc/" target="_blank">LinkedIn</a> |
            💻 <a href="https://github.com/Harshit-0018" target="_blank">GitHub</a>
        </p>
        <p>
    ❓ Need help? 
    <a href="https://mail.google.com/mail/?view=cm&fs=1&to=harshitsingh8157@gmail.com" target="_blank">
        Contact me via Email
    </a>
</p>
    </div>
    """,
    unsafe_allow_html=True
)