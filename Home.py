# NOTE:
# This template is based on the latest version discussed in chat.
# Replace your existing Home.py (or app.py) with this file and adjust
# any field names if your pipeline API differs.

import json
import time
import streamlit as st

from src.pipeline.orchestrator import PipelineOrchestrator

st.set_page_config(
    page_title="PingSense",
    page_icon="🔔",
    layout="wide",
)

@st.cache_resource
def load_pipeline():
    return PipelineOrchestrator()

pipeline = load_pipeline()

st.title("🔔 PingSense")
st.caption("AI-Powered WhatsApp Notification Router")

st.markdown("""
<div style="padding:18px;border-radius:12px;border:1px solid #444;background:#1E1E1E;">
<h3>📲 Smart Notification Intelligence</h3>
<p>
PingSense analyzes WhatsApp messages using <b>Hybrid Retrieval</b>,
<b>Rule Engine</b>, <b>LLM Reasoning</b>, and
<b>Confidence Scoring</b> to decide whether a message should be
<b>Notify</b>, <b>Summarize</b>, or <b>Mute</b>.
</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.header("Select Message")

message_ids = list(pipeline.data.messages["message_id"])

selected = st.sidebar.selectbox("", message_ids)

analyze = st.sidebar.button("Analyze", use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.info("""
### 🔔 PingSense

AI-powered WhatsApp Notification Router

### Pipeline

• Hybrid Retrieval
• Rule Engine
• Claude LLM
• Confidence Engine
• Override Engine
• Explainable AI
""")

st.sidebar.metric("Dataset Size", len(message_ids))
st.sidebar.metric("Pipeline", "Ready ✅")

if analyze:

    with st.spinner("Analyzing message..."):
        start = time.time()
        result = pipeline.run(selected)
        elapsed = time.time() - start

    context = result["context"]
    decision = result["decision"]
    llm = result["llm_result"]

    st.subheader("📊 Decision Summary")

    c1,c2,c3 = st.columns(3)
    c4,c5,c6 = st.columns(3)

    c1.metric("Action", decision.action.upper())
    c2.metric("Type", decision.message_type.upper())
    c3.metric("Confidence", f"{decision.confidence:.1%}")
    c4.metric("Risk Score", f"{context.rule_features.risk_score:.2f}")
    c5.metric("Evidence", len(result["retrieved_evidence"]))
    c6.metric("Triggered Rules", len(context.rule_features.triggered_rules))

    st.success(f"Analysis completed in {elapsed:.2f} seconds")

    tab1, tab2, tab3 = st.tabs(["📩 Analysis","🔍 Evidence","⚙️ Rules"])

    with tab1:
        st.header("📩 Incoming Message")
        st.text_area(
            "Message",
            context.effective_text,
            height=180,
            disabled=True,
        )

        st.subheader("🤖 LLM Decision")

        a,b,c = st.columns(3)
        a.metric("Action", llm.action.upper())
        b.metric("Type", llm.message_type.upper())
        c.metric("Confidence", f"{llm.confidence:.1%}")

        st.info(llm.reason)

        st.subheader("🎯 Final Decision")

        if decision.action == "notify":
            st.success("🔔 Notify Immediately")
        elif decision.action == "summarize":
            st.warning("📝 Add to Summary")
        else:
            st.error("🔕 Mute Notification")

        x,y,z = st.columns(3)
        x.metric("Action", decision.action.upper())
        y.metric("Type", decision.message_type.upper())
        z.metric("Confidence", f"{decision.confidence:.1%}")

        st.progress(decision.confidence)

        if decision.confidence >= 0.80:
            st.success("Very High Confidence")
        elif decision.confidence >= 0.60:
            st.info("High Confidence")
        else:
            st.warning("Medium Confidence")

        if getattr(decision, "override", None):
            st.warning(f"Override Applied: {decision.override}")
        else:
            st.success("No override applied.")

    with tab2:
        st.header("🔍 Retrieved Evidence")

        if result["retrieved_evidence"]:
            for i, evidence in enumerate(result["retrieved_evidence"], start=1):
                with st.expander(f"Evidence {i}"):
                    st.write(f"**Message ID:** {evidence.message_id}")

                    a,b = st.columns(2)
                    a.metric("Score", f"{evidence.score:.3f}")
                    b.metric("Similarity", f"{evidence.similarity:.3f}")

                    st.progress(evidence.score)
                    st.caption(f"Evidence Score: {evidence.score:.1%}")

                    st.info(evidence.reason)

                    c,d,e = st.columns(3)
                    c.metric("Opened", "✅" if evidence.opened else "❌")
                    d.metric("Dismissed", "✅" if evidence.dismissed else "❌")
                    e.metric("Reported", "✅" if evidence.reported else "❌")
        else:
            st.info("No evidence retrieved.")

    with tab3:
        st.header("⚙️ Triggered Rules")

        st.metric("Risk Score", f"{context.rule_features.risk_score:.2f}")

        if context.rule_features.triggered_rules:
            for rule in context.rule_features.triggered_rules:
                st.success(rule.replace("_"," ").title())
        else:
            st.info("No rules triggered.")

    st.divider()

    payload = result.get(
        "formatted",
        {
            "action": decision.action,
            "message_type": decision.message_type,
            "confidence": decision.confidence,
            "reason": getattr(decision, "reason", ""),
        },
    )

    st.download_button(
        "📥 Download Decision (JSON)",
        data=json.dumps(payload, indent=4),
        file_name=f"{selected}_decision.json",
        mime="application/json",
        use_container_width=True,
    )

    st.markdown("---")

    st.caption(
        "PingSense • AI-powered WhatsApp Notification Router • "
        "Hybrid Retrieval • Rule Engine • Claude LLM • Confidence Scoring"
    )