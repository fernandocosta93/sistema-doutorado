import streamlit as st
from css.css import *
# from tour import page_tour

def page_navegar():

    # Inicializar o estado das variáveis, se não estiverem definidos
    if 'botao_atividades' not in st.session_state:
        st.session_state.botao_atividades = False
    if 'botao_atividades_iniciais' not in st.session_state:
        st.session_state.botao_atividades_iniciais = False
    if 'botao_atividades_finais' not in st.session_state:
        st.session_state.botao_atividades_finais = False
    if 'botao_transicoes' not in st.session_state:
        st.session_state.botao_transicoes = False

    st.markdown(HOME_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>Navegar</h1>", unsafe_allow_html=True)
    # st.title("Navegar")

    dfg_col, navegar_col = st.columns([2, 1])

    with dfg_col: 
        st.image(st.session_state.dfg, use_column_width=True)

    with navegar_col:

        btn_atd, btn_atd_ini, btn_atd_fin, btn_tra = st.columns(4)
        with btn_atd:
            if st.button("Atividades"):
                st.session_state.botao_atividades = True
                st.session_state.botao_atividades_iniciais = False
                st.session_state.botao_atividades_finais = False
                st.session_state.botao_transicoes = False
        with btn_atd_ini:
            if st.button("Atividades iniciais"):
                st.session_state.botao_atividades = False
                st.session_state.botao_atividades_iniciais = True
                st.session_state.botao_atividades_finais = False
                st.session_state.botao_transicoes = False
        with btn_atd_fin:
            if st.button("Atividades finais"):
                st.session_state.botao_atividades = False
                st.session_state.botao_atividades_iniciais = False
                st.session_state.botao_atividades_finais = True
                st.session_state.botao_transicoes = False
        with btn_tra:
            if st.button("Transições"):
                st.session_state.botao_atividades = False
                st.session_state.botao_atividades_iniciais = False
                st.session_state.botao_atividades_finais = False
                st.session_state.botao_transicoes = True

        if st.session_state.botao_atividades:

            left, center, right = st.columns(3)
            with center:
                st.image('imgs/anvisa/atividade.png')

            # colocando o texto
            with open('template_matching/anvisa/texto_atividades.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)
        
        if st.session_state.botao_atividades_iniciais:

            left, right = st.columns(2)

            with left:
                st.image('imgs/inicio_processo.png')
            with right:
                st.image('imgs/anvisa/atividade_inicial.png')

            # colocando o texto
            with open('template_matching/anvisa/texto_atividades_iniciais.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)
        
        if st.session_state.botao_atividades_finais:

            left, right = st.columns(2)
            with left:
                st.image('imgs/fim_processo.png')
            with right:
                st.image('imgs/anvisa/atividade_final.png')

            # colocando o texto
            with open('template_matching/anvisa/texto_atividades_finais.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

        if st.session_state.botao_transicoes:

            
            left, center, right = st.columns(3)
            with center:
                st.image('imgs/anvisa/seta_transicao.png')
            # colocando o texto
            with open('template_matching/anvisa/navegar_seta_transicao.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

            left, center, right = st.columns(3)
            with center:
                st.image('imgs/anvisa/transicao_atividades.png')
            # colocando o texto
            with open('template_matching/anvisa/navegar_transicao_atividades.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

            left, center, right = st.columns(3)
            with center:
                st.image('imgs/anvisa/auto_transicao.png')
            # colocando o texto
            with open('template_matching/anvisa/navegar_auto_transicao.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

            left, center, right = st.columns(3)
            with center:
                st.image('imgs/anvisa/transicao_loop.png')
            # colocando o texto
            with open('template_matching/anvisa/navegar_transicao_loop.txt', 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)


    if "selected_section" not in st.session_state:
        st.session_state.selected_section = None

    # Criar botões para simular a navegação entre seções
    st.sidebar.title("Navegação")
    sections = {
        "Fila de Análise": "fila_analise",
        "Exigência": "exigencia",
        "Análise de Cumprimento de Exigência": "analise_cumprimento",
        "Análise em Andamento": "analise_andamento",
        "Finalização": "finalizacao",
        "Recurso": "recurso",
        "Outras Etapas": "outras_etapas",
        "Sobrestado Anvisa": "sobrestado_anvisa",
        "Sobrestado Externo": "sobrestado_externo"
    }

    for label, section in sections.items():
        if st.sidebar.button(label):
            st.session_state.selected_section = section

    # Mostrar o conteúdo com base na seleção
    if st.session_state.selected_section == "fila_analise":
        st.write("Conteúdo detalhado sobre a Fila de Análise.")
    elif st.session_state.selected_section == "exigencia":
        st.write("Detalhes sobre a Exigência.")
    elif st.session_state.selected_section == "analise_cumprimento":
        st.write("Informações sobre Análise de Cumprimento de Exigência.")
    elif st.session_state.selected_section == "analise_andamento":
        st.write("Detalhes sobre Análise em Andamento.")
    elif st.session_state.selected_section == "finalizacao":
        st.write("Informações sobre Finalização.")
    elif st.session_state.selected_section == "recurso":
        st.write("Detalhes sobre Recurso.")
    elif st.session_state.selected_section == "outras_etapas":
        st.write("Informações sobre Outras Etapas.")
    elif st.session_state.selected_section == "sobrestado_anvisa":
        st.write("Detalhes sobre Sobrestado Anvisa.")
    elif st.session_state.selected_section == "sobrestado_externo":
        st.write("Informações sobre Sobrestado Externo.")
    else:
        st.write("Selecione uma opção no menu lateral para ver detalhes.")
    
   

    col1, col2 = st.columns(2)

    with col1:

        if st.button("voltar"):
            st.session_state.page = "home"
            st.session_state.show_second_button = False

    with col2:

        if st.button("tour"):
            st.session_state.page = "page_tour_atividades"