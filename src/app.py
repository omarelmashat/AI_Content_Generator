import streamlit as st

from generator import generate_content
from prompts import CONTENT_TYPES, TONES, LENGTHS

st.set_page_config(page_title="AI Content Generator", page_icon="✍️")

st.title("✍️ AI Content Generator")
st.caption("Pick a content type, tone and length, then let the AI write it.")

content_type = st.selectbox(
    "Content type",
    options=list(CONTENT_TYPES.keys()),
    format_func=lambda key: CONTENT_TYPES[key]["label"],
)

col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Tone", options=list(TONES.keys()), format_func=str.capitalize)
with col2:
    length = st.selectbox("Length", options=list(LENGTHS.keys()), format_func=str.capitalize)

topic = st.text_area("Topic", placeholder="e.g. launching a student coding club")

if st.button("Generate", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating..."):
            try:
                st.session_state["result"] = generate_content(content_type, topic, tone, length)
                st.session_state["result_type"] = content_type
            except Exception as e:
                st.error(f"Something went wrong: {e}")

if "result" in st.session_state:
    st.subheader("Result")
    st.write(st.session_state["result"])
    st.download_button(
        "Download as .txt",
        data=st.session_state["result"],
        file_name=f"{st.session_state['result_type']}.txt",
    )