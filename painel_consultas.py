import streamlit as st
import sqlite3
import pandas as pd

def painel_consultas_screen():
    st.header("Painel de Consultas")
    conn = sqlite3.connect("users.db")
    df = pd.read_sql_query("""
    SELECT 
        a.paciente, 
        a.medico, 
        m.especialidade,
        a.data, 
        a.hora, 
        a.status
    FROM agendamentos a
    LEFT JOIN medicos m ON a.medico = m.nome
""", conn)
    if df.empty:
        st.info("Nenhuma consulta agendada.")
        return

    especialidade = st.selectbox("Filtrar por Médico", ["Todos"] + df['medico'].unique().tolist())
    data = st.date_input("Data da consulta")

    if especialidade != "Todos":
        df = df[df['medico'] == especialidade]
    df = df[df['data'] == data.strftime('%Y-%m-%d')]

    st.dataframe(df)
    conn.close()

import io

# Exportar como Excel
if not df.empty:
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine='openpyxl')
    st.download_button(
        label="📥 Baixar agenda em Excel",
        data=buffer.getvalue(),
        file_name=f"agenda_{especialidade}_{data}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
