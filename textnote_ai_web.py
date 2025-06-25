import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

st.set_page_config(page_title="TextNote.ai", page_icon="📝")
st.title("📝 TextNote.ai")
st.subheader("Summarize any long text into clear, short notes")

input_text = st.text_area("Paste your text here 👇", height=300)

if st.button("🔍 Summarize Text"):
    if input_text.strip():
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)
            st.success("✅ Summary:")
            st.write(summary[0]['summary_text'])
    else:
        st.warning("⚠️ Please enter some text to summarize.")
