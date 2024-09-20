def variaveis_necessarias(nome_processo):

    img_inicio_processo = 'imgs/inicio_processo.png'
    img_fim_processo = 'imgs/fim_processo.png'
    img_seta_transicao = 'imgs/seta_transicao.png'
    texto_seta_transicao = 'template_matching/anvisa/navegar_seta_transicao.txt'

    if nome_processo == "ANVISA":

        img_atividade = 'imgs/anvisa/atividade.png'
        texto_atividade = 'template_matching/anvisa/texto_atividades.txt'
        img_atividade_inicial = 'imgs/anvisa/atividade_inicial.png'
        texto_atividade_inicial = 'template_matching/anvisa/texto_atividades_iniciais.txt'
        img_atividade_final = 'imgs/anvisa/atividade_final.png'
        texto_atividade_final = 'template_matching/anvisa/texto_atividades_finais.txt'
        img_transicao_atividades = 'imgs/anvisa/transicao_atividades.png'
        texto_transicao_atividade = 'template_matching/anvisa/navegar_transicao_atividades.txt'
        img_autotransicao = 'imgs/anvisa/auto_transicao.png'
        texto_autotransicao = 'template_matching/anvisa/navegar_auto_transicao.txt'
        img_transicao_loop = 'imgs/anvisa/transicao_loop.png'
        texto_transicao_loop = 'template_matching/anvisa/navegar_transicao_loop.txt'

    elif nome_processo == 'TJ-SP':
        img_atividade = ''
        texto_atividade = ''
        img_atividade_inicial = ''
        texto_atividade_inicial = ''
        img_atividade_final = ''
        texto_atividade_final = ''
        img_transicao_atividades = ''
        texto_transicao_atividade = ''
        img_autotransicao = ''
        texto_autotransicao = ''
        img_transicao_loop = ''
        texto_transicao_loop = ''

    return img_inicio_processo, img_fim_processo, img_seta_transicao, texto_seta_transicao, img_atividade, texto_atividade, img_atividade_inicial, \
          texto_atividade_inicial, img_atividade_final, texto_atividade_final, img_transicao_atividades, texto_transicao_atividade, \
          img_autotransicao, texto_autotransicao, img_transicao_loop, texto_transicao_loop


    

        
