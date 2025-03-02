import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.header('Maiores Valores ',divider='gray')

if 'dados' not in st.session_state:
    st.error('Os dados não foram carregados')

else:
    top_n = st.session_state.get('top_n',10)
    dados = st.session_state['dados']
    col1,col2,col3 =st.columns(3)

    with col1:
        mempenho =dados.nlargest(top_n,'VALOREMPENHO')
        fig1= px.bar(mempenho,x='MUNICIPIO',y='VALOREMPENHO',title='Maiores valores empenho')
        st.plotly_chart(fig1,use_container_width=True)
       
        
    with col2:
        mpibs= dados.nlargest(top_n,'PIB')
        fig3= px.pie(mpibs, values='PIB', names='MUNICIPIO',title= 'Maiores Empenhos')
        st.plotly_chart(fig3,use_container_width=True)
 
    with col3:
        mprobp= dados.nlargest(top_n,'PROPORCAO')
        fig4= px.bar(mprobp,x='MUNICIPIO',y='PROPORCAO',title= 'Maiores Gastos em proporção ao PIB')
        st.plotly_chart(fig4,use_container_width=True)
       
 
   
   

st.header(body='',divider='gray')
st.write("Joel Teixeira")