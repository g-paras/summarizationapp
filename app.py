import streamlit as st

from gensim.summarization import summarize


st.title('Summarization app')
st.info('_Input should have more than one paragraph_')
sample_text = '''Machine learning involves computers discovering how they can perform tasks without being explicitly programmed to do so. It involves computers learning from data provided so that they carry out certain tasks. For simple tasks assigned to computers, it is possible to program algorithms telling the machine how to execute all steps required to solve the problem at hand; on the computer's part, no learning is needed. For more advanced tasks, it can be challenging for a human to manually create the needed algorithms. In practice, it can turn out to be more effective to help the machine develop its own algorithm, rather than having human programmers specify every needed step.'''
text = st.text_area('Text to analyze', value=sample_text, height=300)
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
