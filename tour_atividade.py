import streamlit as st
from css.css import *

def page_tour_atividades():
    # st.title("Atividades")
    st.markdown(HOME_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>Atividades</h1>", unsafe_allow_html=True)

    nome_dfg = st.session_state.nome_processo
    nome_dfg = nome_dfg.lower()
    nome_dfg = "imgs/" + nome_dfg + "_dfg.png"

    img_dfg, info_texto = st.columns(2)

    with img_dfg:
        st.image(nome_dfg, use_column_width=True)
    with info_texto:
        # TODO: padronizar para o formato da anvisa
        with open('template_matching/texto_atividades_tour.txt', 'r', encoding='utf-8') as file:
                data = file.read()
        st.markdown(data, unsafe_allow_html=True)  

    col1, col2 = st.columns(2)

    with col1:

        if st.button("voltar"):
            st.session_state.page = "page_rep_trabalho"
            st.session_state.show_second_button = False
    
    with col2:  
    
        if st.button("avançar"):
            st.session_state.page = "page_tour_atividades_iniciais"