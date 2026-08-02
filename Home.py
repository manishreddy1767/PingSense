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

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.title("🔔 PingSense")
st.caption("AI-Powered WhatsApp Notification Router")

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.header("Select Message")

message_ids = list(
    pipeline.data.messages["message_id"]
)

selected = st.sidebar.selectbox(
    "",
    message_ids,
)

analyze = st.sidebar.button(
    "Analyze",
    use_container_width=True,
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
### 🔔 PingSense

AI-powered WhatsApp Notification Router

### Pipeline

• Hybrid Retrieval

• Rule Engine

• LLM Reasoning

• Confidence Engine

• Override Engine

• Explainable AI
"""
)

# -------------------------------------------------------
# ANALYZE
# -------------------------------------------------------

if analyze:

    with st.spinner("Analyzing message..."):

        start = time.time()

        result = pipeline.run(selected)

        elapsed = time.time() - start

    context = result["context"]
    decision = result["decision"]
    llm = result["llm_result"]

    # -------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------

    st.subheader("📊 Decision Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Action",
        decision.action.upper(),
    )

    c2.metric(
        "Type",
        decision.message_type.upper(),
    )

    c3.metric(
        "Confidence",
        f"{decision.confidence:.1%}",
    )

    c4.metric(
        "Risk Score",
        f"{context.rule_features.risk_score:.2f}",
    )

    st.success(
        f"Analysis completed in {elapsed:.2f} seconds"
    )

    st.divider()

    # -------------------------------------------------------
    # TABS
    # -------------------------------------------------------

    tab1, tab2, tab3 = st.tabs(
        [
            "📩 Analysis",
            "🔍 Evidence",
            "⚙ Rules",
        ]
    )

    # -------------------------------------------------------
    # ANALYSIS TAB
    # -------------------------------------------------------

    with tab1:

        st.header("Incoming Message")

        st.info(context.effective_text)

        st.markdown("---")

        st.subheader("🤖 LLM Decision")

        c1, c2, c3 = st.columns(3)

        c1.metric("Action", llm.action.upper())
        c2.metric("Type", llm.message_type.upper())
        c3.metric(
            "Confidence",
            f"{llm.confidence:.1%}",
        )

        st.info(llm.reason)

        st.markdown("---")

        st.subheader("🎯 Final Decision")

        if decision.action == "notify":

            st.success("🟢 HIGH PRIORITY")

        elif decision.action == "summarize":

            st.warning("🟡 MEDIUM PRIORITY")

        else:

            st.error("🔴 LOW PRIORITY")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Action",
            decision.action.upper(),
        )

        c2.metric(
            "Type",
            decision.message_type.upper(),
        )

        c3.metric(
            "Confidence",
            f"{decision.confidence:.1%}",
        )

        st.progress(decision.confidence)

        if decision.override:

            st.warning(
                f"Override Applied: {decision.override}"
            )

        else:

            st.success("No override applied")

    # -------------------------------------------------------
    # EVIDENCE TAB
    # -------------------------------------------------------

    with tab2:

        st.header("Retrieved Evidence")

        for i, evidence in enumerate(
            result["retrieved_evidence"],
            start=1,
        ):

            with st.expander(
                f"Evidence {i}"
            ):

                st.write(
                    f"**Message ID:** {evidence.message_id}"
                )

                c1, c2 = st.columns(2)

                c1.metric(
                    "Score",
                    f"{evidence.score:.3f}",
                )

                c2.metric(
                    "Similarity",
                    f"{evidence.similarity:.3f}",
                )

                st.write(
                    "**Reason**"
                )

                st.info(evidence.reason)

                c3, c4, c5 = st.columns(3)

                c3.metric(
                    "Opened",
                    "✅" if evidence.opened else "❌",
                )

                c4.metric(
                    "Dismissed",
                    "✅" if evidence.dismissed else "❌",
                )

                c5.metric(
                    "Reported",
                    "✅" if evidence.reported else "❌",
                )

    # -------------------------------------------------------
    # RULES TAB
    # -------------------------------------------------------

    with tab3:

        st.header("Triggered Rules")

        st.metric(
            "Risk Score",
            f"{context.rule_features.risk_score:.2f}",
        )

        if context.rule_features.triggered_rules:

            for rule in context.rule_features.triggered_rules:

                st.success(
                    rule.replace(
                        "_",
                        " ",
                    ).title()
                )

        else:

            st.info(
                "No rules triggered."
            )