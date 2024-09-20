import streamlit as st
from css.css import *
from functions.funcs_navegar import variaveis_necessarias

def page_navegar():

    nome_processo = st.query_params['process']
    img_inicio_processo, img_fim_processo, img_seta_transicao, texto_seta_transicao, img_atividade, texto_atividade, img_atividade_inicial, \
    texto_atividade_inicial, img_atividade_final, texto_atividade_final, img_transicao_atividades, texto_transicao_atividade, \
    img_autotransicao, texto_autotransicao, img_transicao_loop, texto_transicao_loop = variaveis_necessarias(nome_processo)
         

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
                st.image(img_atividade)

            # colocando o texto
            with open(texto_atividade, 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)
        
        if st.session_state.botao_atividades_iniciais:

            left, right = st.columns(2)

            with left:
                st.image(img_inicio_processo)
            with right:
                st.image(img_atividade_inicial)

            # colocando o texto
            with open(texto_atividade_inicial, 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)
        
        if st.session_state.botao_atividades_finais:

            left, right = st.columns(2)
            with left:
                st.image(img_fim_processo)
            with right:
                st.image(img_atividade_final)

            # colocando o texto
            with open(texto_atividade_final, 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

        if st.session_state.botao_transicoes:

            
            left, center, right = st.columns(3)
            with center:
                st.image(img_seta_transicao)
            # colocando o texto
            with open(texto_seta_transicao, 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

            left, center, right = st.columns(3)
            with center:
                st.image(img_transicao_atividades)
            # colocando o texto
            with open(texto_transicao_atividade, 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

            left, center, right = st.columns(3)
            with center:
                st.image(img_autotransicao)
            # colocando o texto
            with open(texto_autotransicao, 'r', encoding='utf-8') as file:
                    data = file.read()
            st.markdown(data, unsafe_allow_html=True)

            left, center, right = st.columns(3)
            with center:
                st.image(img_transicao_loop)
            # colocando o texto
            with open(texto_transicao_loop, 'r', encoding='utf-8') as file:
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