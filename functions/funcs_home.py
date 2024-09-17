import os
import streamlit as st

def texto_inicial(processo):
    base_path = os.getcwd()
    path = base_path + "/template_matching/" + processo + "/page_inicial.txt"
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        st.markdown(f"""
            <div class="centralizado">
                <p>{data}</p>
            </div>
            """, unsafe_allow_html=True)