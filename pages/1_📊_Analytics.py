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

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

try:
    df = pd.read_csv("outputs/results.csv")
except FileNotFoundError:
    st.error(
        "Run 'python -m src.main' first to generate outputs."
    )
    st.stop()

# ----------------------------------------------------
# OVERVIEW
# ----------------------------------------------------

st.subheader("📈 Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Messages",
    len(df),
)

c2.metric(
    "Notify",
    (df.action == "notify").sum(),
)

c3.metric(
    "Summarize",
    (df.action == "summarize").sum(),
)

c4.metric(
    "Mute",
    (df.action == "mute").sum(),
)

c5, c6, c7, c8 = st.columns(4)

c5.metric(
    "Business",
    (df.message_type == "business").sum(),
)

c6.metric(
    "Promotion",
    (df.message_type == "promotion").sum(),
)

c7.metric(
    "Scam",
    (df.message_type == "scam").sum(),
)

c8.metric(
    "Avg Confidence",
    f"{df.confidence.mean():.1%}",
)

st.divider()

# ----------------------------------------------------
# BAR CHARTS
# ----------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📬 Action Distribution")

    st.bar_chart(
        df.action.value_counts()
    )

with right:

    st.subheader("📨 Message Types")

    st.bar_chart(
        df.message_type.value_counts()
    )

st.divider()

# ----------------------------------------------------
# CONFIDENCE HISTOGRAM
# ----------------------------------------------------

st.subheader("📉 Confidence Distribution")

fig, ax = plt.subplots(figsize=(10, 4))

ax.hist(
    df.confidence,
    bins=10,
)

ax.set_xlabel("Confidence")

ax.set_ylabel("Messages")

st.pyplot(fig)

st.divider()

# ----------------------------------------------------
# PIE CHART
# ----------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🥧 Action Breakdown")

    fig, ax = plt.subplots(figsize=(5, 5))

    df.action.value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax,
    )

    ax.set_ylabel("")

    st.pyplot(fig)

with right:

    st.subheader("🎯 Average Confidence")

    st.progress(float(df.confidence.mean()))

    st.metric(
        "Average",
        f"{df.confidence.mean():.1%}",
    )

st.divider()

# ----------------------------------------------------
# FILTERS
# ----------------------------------------------------

st.subheader("🔍 Search & Filter")

col1, col2 = st.columns(2)

query = col1.text_input(
    "Search Message ID"
)

action_filter = col2.selectbox(
    "Filter Action",
    ["All"] + sorted(df.action.unique()),
)

filtered = df.copy()

if query:

    filtered = filtered[
        filtered.message_id.str.contains(
            query,
            case=False,
        )
    ]

if action_filter != "All":

    filtered = filtered[
        filtered.action == action_filter
    ]

st.dataframe(
    filtered,
    use_container_width=True,
    height=450,
)

st.divider()

# ----------------------------------------------------
# EXPORT
# ----------------------------------------------------

st.subheader("📥 Export Results")

col1, col2 = st.columns(2)

with col1:

    with open(
        "outputs/results.csv",
        "rb",
    ) as f:

        st.download_button(
            "⬇ Download CSV",
            f,
            file_name="results.csv",
            mime="text/csv",
            use_container_width=True,
        )

with col2:

    with open(
        "outputs/results.json",
        "rb",
    ) as f:

        st.download_button(
            "⬇ Download JSON",
            f,
            file_name="results.json",
            mime="application/json",
            use_container_width=True,
        )

st.divider()

st.caption(
    "PingSense • AI-powered WhatsApp Notification Router • Analytics Dashboard"
)