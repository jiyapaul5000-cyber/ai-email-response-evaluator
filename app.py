import streamlit as st

from services.gemini_service import generate_reply
from prompts.prompts import EMAIL_REPLY_PROMPT
from services.evaluator import evaluate_reply

st.set_page_config(page_title="AI Email Response Evaluator")

st.title("📧 AI Email Response Evaluator")

email = st.text_area("Paste Email")

if st.button("Generate Reply"):

    if email:

        reply = generate_reply(email, EMAIL_REPLY_PROMPT)
        evaluation = evaluate_reply(email, reply)

        st.subheader("Suggested Reply")
        st.write(reply)
        st.subheader("📊 AI Evaluation")

        st.metric("Accuracy", f"{evaluation['accuracy']}%")

        st.write("**Tone:**", evaluation["tone"])

        st.write("**Completeness:**", evaluation["completeness"])

        st.write("**Reason:**")

        st.info(evaluation["reason"])

        st.write("**Suggestions:**")

        st.success(evaluation["suggestions"])

        

    else:

        st.warning("Please enter an email.")