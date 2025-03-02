import streamlit as st


st.header('Visualização de dados',divider='gray')

if 'dados' not in st.session_state:
    st.error('Os dados não foram carregados')

else:
    top_n = st.session_state.get('top_n',10)
    dados = st.session_state['dados']
    dados_filtrados = dados.head(top_n)
    st.dataframe(dados_filtrados)

st.header(body='',divider='gray')
st.write("Joel Teixeira")