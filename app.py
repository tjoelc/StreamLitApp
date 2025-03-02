import streamlit as st
import pandas as pd


st.set_page_config(page_title="Aplicação Analise exploratoria de dados")
st.title('Bem vindo a Analise Exploratoria de Despesas')

@st.cache_resource
def load_data():
    dados= pd.read_csv('dados.csv',sep=';')
    dados['PROPORCAO'] = dados['VALOREMPENHO'] / dados['PIB']
    return dados

dados = load_data()
st.session_state['dados'] = dados

with st.sidebar:
    st.header('Configurações globais')
    if 'top_n' in st.session_state:
        default_top_n = st.session_state['top_n']
    
    else:
        default_top_n = 10
    
    if 'dados' in st.session_state:
        top_n = st.number_input('Selecione o numero de dados para exibir',
                                min_value =1, max_value = len(st.session_state['dados']),
                                value= default_top_n)
        st.session_state['top_n'] = top_n
    else:
        st.write("Aguardando o carregamento dos dados...")
        st.session_state['top_n'] = default_top_n # Garante que top_n seja definido.