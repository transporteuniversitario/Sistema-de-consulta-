import streamlit as st
import sqlite3
import pandas as pd

def painel_consultas_screen():
    st.header("Painel de Consultas")
    conn = sqlite3.connect("users.db")
    df = pd.read_sql_query("SELECT * FROM agendamentos", conn)
    especialidade = st.selectbox("Filtrar por Médico", ["Todos"] + df['medico'].unique().tolist())
    data = st.date_input("Data da consulta")

    if especialidade != "Todos":
        df = df[df['medico'] == especialidade]
    df = df[df['data'] == data.strftime('%Y-%m-%d')]

    st.dataframe(df)
    conn.close()
