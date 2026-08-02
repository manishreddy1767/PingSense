import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="PingSense Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 PingSense Analytics Dashboard")
st.caption("AI-powered notification routing analytics")

try:
    df = pd.read_csv("outputs/results.csv")
except FileNotFoundError:
    st.error("Run 'python -m src.main' first to generate outputs/results.csv")
    st.stop()

st.success("✅ Analytics loaded successfully")

# ---------------------- OVERVIEW ----------------------

st.subheader("📈 Overview")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Messages", len(df))
c2.metric("Notify", (df.action=="notify").sum())
c3.metric("Summarize", (df.action=="summarize").sum())
c4.metric("Mute", (df.action=="mute").sum())

c5,c6,c7,c8 = st.columns(4)
c5.metric("Business", (df.message_type=="business").sum())
c6.metric("Promotion", (df.message_type=="promotion").sum())
c7.metric("Scam", (df.message_type=="scam").sum())
c8.metric("Average Confidence", f"{df.confidence.mean():.1%}")

st.divider()

left,right = st.columns(2)

with left:
    st.subheader("📬 Action Distribution")
    st.bar_chart(df.action.value_counts())

with right:
    st.subheader("📨 Message Type Distribution")
    st.bar_chart(df.message_type.value_counts())

st.divider()

left,right = st.columns(2)

with left:
    st.subheader("📉 Confidence Distribution")
    fig,ax=plt.subplots(figsize=(8,3))
    ax.hist(df.confidence,bins=10)
    ax.set_xlabel("Confidence")
    ax.set_ylabel("Messages")
    st.pyplot(fig)

with right:
    st.subheader("🥧 Action Breakdown")
    fig,ax=plt.subplots(figsize=(5,5))
    df.action.value_counts().plot(kind="pie",autopct="%1.1f%%",ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

st.divider()

st.subheader("🎯 Confidence")

avg=float(df.confidence.mean())
st.progress(avg)
st.metric("Average Confidence",f"{avg:.1%}")

st.divider()

st.subheader("🔍 Search & Filter")

f1,f2,f3=st.columns(3)

query=f1.text_input("Message ID")

action=f2.selectbox(
    "Action",
    ["All"]+sorted(df.action.unique().tolist())
)

mtype=f3.selectbox(
    "Message Type",
    ["All"]+sorted(df.message_type.unique().tolist())
)

filtered=df.copy()

if query:
    filtered=filtered[
        filtered.message_id.str.contains(query,case=False)
    ]

if action!="All":
    filtered=filtered[filtered.action==action]

if mtype!="All":
    filtered=filtered[filtered.message_type==mtype]

st.dataframe(
    filtered.sort_values("confidence",ascending=False),
    use_container_width=True,
    height=500,
)

st.divider()

st.subheader("📥 Export Results")

c1,c2=st.columns(2)

with c1:
    with open("outputs/results.csv","rb") as f:
        st.download_button(
            "⬇ Download CSV",
            f,
            "results.csv",
            "text/csv",
            use_container_width=True,
        )

with c2:
    with open("outputs/results.json","rb") as f:
        st.download_button(
            "⬇ Download JSON",
            f,
            "results.json",
            "application/json",
            use_container_width=True,
        )

st.divider()

st.caption(
    "PingSense • Analytics Dashboard • Hybrid Retrieval • Rule Engine • Claude • Confidence Engine"
)