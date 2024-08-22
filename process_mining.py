import pandas as pd
import pm4py
# from pm4py.visualization.dfg import visualizer as dfg_vis_factory

def ler_csv(nome, separador, case_id, activity_key, timestamp_key):

    df = pd.read_csv(nome, sep=separador, encoding='latin1')

    # ANVISA: '#NUM_EXPEDIENTE_PETICAO', 'DESC_GRUPO_ETAPA_CICLO_ANALISE', 'DATA_FIM_OCORRENCIA_GRP_ETAPA'
    df = df[[case_id, activity_key, timestamp_key]]

    df = df.rename(columns={case_id: 'case_id',
                            activity_key: 'activity',
                            timestamp_key: 'timestamp_log'})

    df = pm4py.format_dataframe(df, case_id='case_id', activity_key='activity', timestamp_key='timestamp_log')
    df = df.dropna()

    event_log = pm4py.convert_to_event_log(df)

    return event_log

def criar_dfg(event_log):

    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
    # pm4py.view_dfg(dfg, start_activities, end_activities, format='png')
    pm4py.save_vis_dfg(dfg, start_activities, end_activities, 'imgs/anvisa_dfg.png')

    # parameters = {
    #     dfg_vis_factory.Variants.FREQUENCY.value.Parameters.FORMAT: "svg",
    #     dfg_vis_factory.Variants.FREQUENCY.value.Parameters.START_ACTIVITIES: start_activities,
    #     dfg_vis_factory.Variants.FREQUENCY.value.Parameters.END_ACTIVITIES: end_activities
    # }
    # gviz = dfg_vis_factory.apply(dfg, parameters=parameters)
    # return gviz


nome = 'logs/anvisa.CSV'
event_log = ler_csv(nome, ";", '#NUM_EXPEDIENTE_PETICAO', 'DESC_GRUPO_ETAPA_CICLO_ANALISE', 'DATA_FIM_OCORRENCIA_GRP_ETAPA')
criar_dfg(event_log)