import streamlit as st
from auth import login_screen
from agendamentos import agendamento_screen
from cadastro_pacientes import cadastro_pacientes_screen
from cadastro_medicos import cadastro_medicos_screen
from painel_consultas import painel_consultas_screen
from database import init_db

st.set_page_config(page_title="Sistema de Agendamento Médico", layout="wide")
init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_screen()
else:
    menu = st.sidebar.radio("Menu", ["Agendamentos", "Pacientes", "Médicos", "Painel de Consultas"])
    if menu == "Agendamentos":
        agendamento_screen()
    elif menu == "Pacientes":
        cadastro_pacientes_screen()
    elif menu == "Médicos":
        cadastro_medicos_screen()
    elif menu == "Painel de Consultas":
        painel_consultas_screen()
