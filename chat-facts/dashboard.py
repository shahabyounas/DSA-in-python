import streamlit as st
import numpy as np
import pandas as pd
from datapipeline import DataPipeLine
import nltk
from nltk.text import Text



title = "Analyze your chat with friends"


st.sidebar.title('Your Files')

class Dashboard:
    
    def __init__(self, title = title):
        self.is_data_processing = False
        self.title = title
        self.text = ''

    def chat_upload(self):
        chat_files = st.file_uploader('Your chat file e.g Whatsapp', accept_multiple_files=True)
        for cf in chat_files:
            st.sidebar.caption(cf.name)
            self.text += cf.getvalue().decode('utf-8')
        return chat_files

    def process_chat(self):
        if self.text:
            pipeline = DataPipeLine()
            st.sidebar.title(type(self.text))
            tokens = pipeline.tokenize_text(self.text)
            st.session_state.tokens = tokens

    def sub_heading1(self):
        col1, col2 = st.columns(2)
        col1.subheader('Process your data')
        col2.button('Process', type='primary', on_click=self.process_chat)




if __name__ == '__main__':
    dashboard = Dashboard(title=title)
    pipeline = DataPipeLine()
    st.title(dashboard.title)
    dashboard.chat_upload()
    dashboard.sub_heading1()
    
    if "tokens" not in st.session_state:
        st.session_state.tokens = []
        st.session_state.df = []
        st.session_state.words_length = []
        st.session_state.fav_words = ["love"]
    
    tokens = st.session_state.tokens
    df = st.session_state.df
    fav_words = st.session_state.fav_words
    words_length = []
    
    if len(tokens):
        tokens = pipeline.clean_text(dashboard.text)
        df = nltk.FreqDist(tokens)
        words_length = nltk.FreqDist([len(w) for w in tokens])
        
    st.line_chart(words_length)
    st.line_chart(nltk.FreqDist(tokens))
    