import streamlit as st
import os
from page_rep_trabalho import page_rep_trabalho
from tour_atividade import page_tour_atividades
from tour_atividades_iniciais import page_tour_atividades_iniciais
from tour_atividades_finais import page_tour_atividades_finais
from tour_elemento_inicio_processo import page_tour_elemento_inicio_processo
from tour_elemento_atividade_inicial import page_tour_elemento_atividade_inicial
from tour_elemento_atividade import page_tour_elemento_atividade
from tour_elemento_seta_transicao import page_tour_elemento_seta_transicao
from tour_elemento_transicao_atividades import page_tour_elemento_transicao_atividades
from tour_elemento_autotransicao import page_tour_elemento_autotransicao
from tour_elemento_loop import page_tour_elemento_loop
from tour_atividade_final import page_tour_elemento_atividade_final
from tour_elemento_final_processo import page_tour_elemento_final_processo
from navegar import page_navegar
from css.css import HOME_CSS

# Inicializar o estado das variáveis, se não estiverem definidos
if 'botao_anvisa' not in st.session_state:
    st.session_state.botao_anvisa = False
if 'botao_tjsp' not in st.session_state:
    st.session_state.botao_tjsp = False
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'nome_processo' not in st.session_state:
    st.session_state.nome_processo = ""


def home_page():    
    st.set_page_config(layout='wide')    
    
    st.markdown(HOME_CSS, unsafe_allow_html=True)

    st.markdown("<h1 class='centered-title'>Processos</h1>", unsafe_allow_html=True)

    # Botões
    anvisa, juridico = st.columns(2)
    with anvisa:         
        if st.button("ANVISA"):
            st.session_state.botao_anvisa = True
            st.session_state.botao_tjsp = False
            st.session_state.nome_processo = "Anvisa"        

    with juridico:
        if st.button("TJ-SP"):
            st.session_state.botao_anvisa = False
            st.session_state.botao_tjsp = True
            st.session_state.nome_processo = "TJ-SP" 
        
    # Área de texto
    if st.session_state.botao_anvisa:
        base_path = os.getcwd()
        path = base_path + "\\template_matching\\anvisa\\page_inicial.txt"
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        # st.write(f"""{data}""")
        st.markdown(f"""
            <div class="centralizado">
                <p>{data}</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("AVANÇAR"):
            st.session_state.page = "page_rep_trabalho"

    if st.session_state.botao_tjsp:
        st.markdown(f"""
            <div class="centralizado">
                <p>Log do Tribunal de Justiça do Estado de São Paulo</p>
            </div>
            """, unsafe_allow_html=True)

# Controlar a navegação entre as páginas
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "page_rep_trabalho":
    page_rep_trabalho()
elif st.session_state.page == "page_tour_atividades":
    page_tour_atividades()
elif st.session_state.page == "page_tour_atividades_iniciais":
    page_tour_atividades_iniciais()
elif st.session_state.page == "page_tour_atividades_finais":
    page_tour_atividades_finais()
elif st.session_state.page == "page_tour_elemento_inicio_processo":
    page_tour_elemento_inicio_processo()
elif st.session_state.page == "page_tour_elemento_atividade_inicial":
    page_tour_elemento_atividade_inicial()
elif st.session_state.page == "page_tour_elemento_atividade":
    page_tour_elemento_atividade()
elif st.session_state.page == "page_tour_elemento_seta_transicao":
    page_tour_elemento_seta_transicao()
elif st.session_state.page == "page_tour_elemento_transicao_atividades":
    page_tour_elemento_transicao_atividades()
elif st.session_state.page == "page_tour_elemento_autotransicao":
    page_tour_elemento_autotransicao()
elif st.session_state.page == "page_tour_elemento_loop":
    page_tour_elemento_loop()
elif st.session_state.page == "page_tour_elemento_atividade_final":
    page_tour_elemento_atividade_final()
elif st.session_state.page == "page_tour_elemento_final_processo":
    page_tour_elemento_final_processo()
elif st.session_state.page == "page_navegar":
    page_navegar()

