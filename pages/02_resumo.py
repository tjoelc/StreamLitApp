import streamlit as st


st.header('Resumo Estatistico dos dados',divider='gray')

if 'dados' not in st.session_state:
    st.error('Os dados não foram carregados')

else:
    dados = st.session_state['dados']
    dados_filtrados = dados.describe().reset_index()
    #st.dataframe(dados_filtrados,width=600)
    st.write(dados_filtrados)



st.header(body='',divider='gray')
st.write("Joel Teixeira")