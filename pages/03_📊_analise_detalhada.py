import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.header('Distribuição dos dados ',divider='gray')

if 'dados' not in st.session_state:
    st.error('Os dados não foram carregados')

else:
    dados = st.session_state['dados']
    col1,col2 =st.columns(2)

    with col1:
        fig1= px.histogram(dados,x='VALOREMPENHO',title='Histograma valor empenho')
        st.plotly_chart(fig1,use_container_width=True)
       
        fig2= px.box(dados,x='VALOREMPENHO',title='Boxsplot valor empenho')
        st.plotly_chart(fig2,use_container_width=True)
    

    with col2:
        fig3= px.histogram(dados,x='PIB',title='Histograma PIB')
        st.plotly_chart(fig3,use_container_width=True)
       
        fig4= px.box(dados,x='PIB',title='Boxsplot valor PIB')
        st.plotly_chart(fig4,use_container_width=True)
 
   
   

st.header(body='',divider='gray')
st.write("Joel Teixeira")