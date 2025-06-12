import streamlit as st
import sqlite3
import pandas as pd
import io

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

    especialidades = ["Todos"] + sorted(df["especialidade"].dropna().unique().tolist())
    filtro_especialidade = st.selectbox("Filtrar por Especialidade", especialidades)
    data = st.date_input("Data da consulta")

    df["data"] = pd.to_datetime(df["data"])

    if filtro_especialidade != "Todos":
        df = df[df["especialidade"] == filtro_especialidade]

    df = df[df["data"] == pd.to_datetime(data)]

    st.dataframe(df)

    # Exportar como Excel
    if not df.empty:
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, engine='openpyxl')
        st.download_button(
            label="📥 Baixar agenda em Excel",
            data=buffer.getvalue(),
            file_name=f"agenda_{filtro_especialidade}_{data}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    conn.close()
