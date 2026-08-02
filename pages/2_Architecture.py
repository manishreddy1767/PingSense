import streamlit as st

st.set_page_config(
    page_title="PingSense Architecture",
    page_icon="🏗️",
    layout="wide",
)

st.title("🏗️ PingSense System Architecture")
st.caption("End-to-End AI Notification Routing Pipeline")

st.markdown("---")

# ---------------------------------------------------
# OVERVIEW
# ---------------------------------------------------

st.header("📌 Overview")

st.write(
    """
PingSense is an AI-powered WhatsApp notification routing system.
It combines **hybrid retrieval**, **rule-based reasoning**, **LLM reasoning**,
and **confidence scoring** to determine whether a message should:

- 🔔 Notify immediately
- 📝 Summarize later
- 🔕 Mute
"""
)

st.markdown("---")

# ---------------------------------------------------
# PIPELINE
# ---------------------------------------------------

st.header("⚙️ Processing Pipeline")

st.code(
"""
Incoming WhatsApp Message
          │
          ▼
 Context Builder
          │
          ▼
 Multimodal Normalizer
(Text / Image / Voice)
          │
          ▼
 Hybrid Evidence Retrieval
(Token + Semantic Search)
          │
          ▼
 Rule Engine
(Scam / OTP / Payments /
Urgency / Promotions)
          │
          ▼
 Claude LLM
(Context-Aware Decision)
          │
          ▼
 Override Engine
(User Preferences)
          │
          ▼
 Confidence Engine
(Rule + LLM + Evidence)
          │
          ▼
 Final Notification Decision
""",
language="text",
)

st.markdown("---")

# ---------------------------------------------------
# COMPONENTS
# ---------------------------------------------------

st.header("🧩 Components")

components = [

    ("📥 Context Builder",
     "Collects the selected message and gathers all related metadata."),

    ("🖼️ Multimodal Normalizer",
     "Converts images, voice notes and text into a unified representation."),

    ("🔍 Hybrid Retrieval",
     "Retrieves similar historical messages using token overlap and semantic embeddings."),

    ("⚙️ Rule Engine",
     "Applies deterministic business rules such as OTP detection, payment requests, scams, urgency and promotions."),

    ("🤖 Claude LLM",
     "Uses contextual reasoning to classify the message and recommend an action."),

    ("🛡️ Override Engine",
     "Applies user preferences or safety overrides before finalizing the decision."),

    ("📈 Confidence Engine",
     "Combines rule confidence, LLM confidence and evidence quality into a final confidence score."),

    ("🎯 Decision Formatter",
     "Produces the final explainable output shown in the dashboard."),
]

for title, desc in components:

    with st.expander(title):

        st.write(desc)

st.markdown("---")

# ---------------------------------------------------
# DECISION FLOW
# ---------------------------------------------------

st.header("🎯 Decision Logic")

st.success(
"""
Incoming Message

↓

Context Creation

↓

Evidence Retrieval

↓

Rule Evaluation

↓

LLM Decision

↓

Override Checks

↓

Confidence Scoring

↓

Notify / Summarize / Mute
"""
)

st.markdown("---")

# ---------------------------------------------------
# FEATURES
# ---------------------------------------------------

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
- ✅ Hybrid Retrieval
- ✅ Semantic Search
- ✅ Explainable AI
- ✅ Rule-Based Reasoning
- ✅ LLM Classification
""")

with col2:

    st.markdown("""
- ✅ Confidence Scoring
- ✅ Override Engine
- ✅ Analytics Dashboard
- ✅ Export Results
- ✅ Streamlit Interface
""")

st.markdown("---")

# ---------------------------------------------------
# TECH STACK
# ---------------------------------------------------

st.header("🛠️ Technology Stack")

st.table(
{
    "Layer": [
        "Frontend",
        "Backend",
        "LLM",
        "Retrieval",
        "Analytics",
        "Language",
    ],
    "Technology": [
        "Streamlit",
        "Python",
        "Claude",
        "Semantic + Token Search",
        "Pandas / Matplotlib",
        "Python 3",
    ],
}
)

st.markdown("---")

st.info(
"""
PingSense demonstrates an explainable AI pipeline that combines
retrieval, deterministic rules, and large language models to make
transparent notification routing decisions.
"""
)