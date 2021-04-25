import streamlit as st

from gensim.summarization import summarize


st.title('Summarization app')
st.info('_Input should have more than one paragraph_')
text = st.text_area('Text to analyze', height=300)
if st.button('Summarize'):
    if len(text) < 500:
        st.error('Text should have more than 500 words')
    else:
        # text = text.replace('.', '\n')
        try:
            st.write(summarize(text))
        except:
            st.error('ValueError: Input must have more than one sentence')
    # st.write(len(text))
