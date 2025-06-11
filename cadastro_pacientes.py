import streamlit as st
import sqlite3

def cadastro_pacientes_screen():
    st.header("Cadastro de Pacientes")
    nome = st.text_input("Nome do Paciente")
    telefone = st.text_input("Telefone")
    observacoes = st.text_area("Observações")
    if st.button("Cadastrar Paciente"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS pacientes (nome TEXT, telefone TEXT, observacoes TEXT)''')
        c.execute("INSERT INTO pacientes (nome, telefone, observacoes) VALUES (?, ?, ?)", (nome, telefone, observacoes))
        conn.commit()
        conn.close()
        st.success("Paciente cadastrado com sucesso!")
