import streamlit as st
from css.css import *

def page_rep_trabalho():

    # query_params = st.experimental_get_query_params()
    nome_processo = st.query_params['process']

    if nome_processo == "ANVISA":
         nome_dfg = "imgs/anvisa/anvisa_dfg.png"
         template = 'template_matching/anvisa/page_rep_trabalho.txt'
    elif nome_processo == "TJ-SP":
         nome_dfg = 'imgs/tjsp/dfg_principal.png'
         template = 'template_matching/tjsp/page_rep_trabalho.txt'

    st.markdown(HOME_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>Representação do trabalho</h1>", unsafe_allow_html=True)     

    
    st.image(nome_dfg, use_column_width=True)

    # colocando o texto
    with open(template, 'r', encoding='utf-8') as file:
            data = file.read()

    # Centralizando o texto em uma div usando HTML/CSS
    st.markdown(
        f"""
        <div 
            style="
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100px; 
                border: 1px solid #ccc;
                margin-top: 50px;
                margin-bottom: 50px;
            "
        >
                <p style="text-align: center;">{data}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("voltar"):
            st.session_state.page = "home"
            st.session_state.botao_anvisa = False
            st.session_state.botao_tjsp = False
    
    with col2:  
    
        if st.button("tour"):
            st.session_state.page = "page_tour_atividades"

    with col3:

        if st.button("navegar"):
            st.session_state.page = "page_navegar"
            st.session_state.dfg = nome_dfg
            # st.experimental_rerun()

    
            