import streamlit as st
import sqlite3

def cadastro_medicos_screen():
    st.header("Cadastro de Médicos")
    nome = st.text_input("Nome do Médico")
    especialidade = st.text_input("Especialidade")
    if st.button("Cadastrar Médico"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS medicos (nome TEXT, especialidade TEXT)''')
        c.execute("INSERT INTO medicos (nome, especialidade) VALUES (?, ?)", (nome, especialidade))
        conn.commit()
        conn.close()
        st.success("Médico cadastrado com sucesso!")
