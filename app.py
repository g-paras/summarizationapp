import streamlit as st

from gensim.summarization import summarize


st.title('Summarization app')

text = st.text_area('Enter text here')
if st.button('Summarize'):
    st.write(summarize(text))
