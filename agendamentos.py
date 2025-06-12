import streamlit as st
import sqlite3
import pandas as pd

def agendamento_screen():
    st.header("Agendamento de Consultas")
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS agendamentos (paciente TEXT, medico TEXT, data TEXT, hora TEXT, status TEXT)")

    pacientes = [r[0] for r in c.execute("SELECT nome FROM pacientes").fetchall()]
    medicos = [r[0] for r in c.execute("SELECT nome FROM medicos").fetchall()]

    paciente = st.selectbox("Paciente", pacientes)
    medico = st.selectbox("Médico", medicos)
    data = st.date_input("Data")
    hora = st.time_input("Hora")
    status = st.selectbox("Status", ["Agendado", "Confirmado", "Cancelado", "Retorno"])

    if st.button("Agendar Consulta"):
        c.execute("INSERT INTO agendamentos (paciente, medico, data, hora, status) VALUES (?, ?, ?, ?, ?)", 
                  (paciente, medico, data.strftime('%Y-%m-%d'), hora.strftime('%H:%M'), status))
        conn.commit()
        st.success("Consulta agendada com sucesso!")
    conn.close()
