import streamlit as st
from auth import login_screen
from screens.home import home_screen
from screens.cadastro_medico import cadastro_medico_screen
from screens.cadastro_paciente import cadastro_paciente_screen
from screens.agendamento import agendamento_screen
from screens.consultas import consultas_screen
from screens.usuarios import cadastro_usuario_screen
from screens.agenda_medicos import agenda_medicos_screen

st.set_page_config(page_title="Sistema de Agendamento", layout="wide")

if 'usuario' not in st.session_state:
    st.session_state.usuario = None

if st.session_state.usuario is None:
    login_screen()  # Exibe a tela de login
else:
    # Menu lateral
    menu = st.sidebar.selectbox("Menu", [
        "🏠 Início",
        "📋 Cadastro de Paciente",
        "🩺 Cadastro de Médico",
        "🗓️ Agendar Consulta",
        "📑 Consultas por Especialidade",
        "📆 Agenda dos Médicos"
    ])

    if st.session_state.usuario == "admin":
        if st.sidebar.button("➕ Cadastrar Novo Usuário"):
            cadastro_usuario_screen()

    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Sair"):
        st.session_state.usuario = None
        st.experimental_rerun()

    # Roteamento
    if menu == "🏠 Início":
        home_screen()
    elif menu == "📋 Cadastro de Paciente":
        cadastro_paciente_screen()
    elif menu == "🩺 Cadastro de Médico":
        cadastro_medico_screen()
    elif menu == "🗓️ Agendar Consulta":
        agendamento_screen()
    elif menu == "📑 Consultas por Especialidade":
        consultas_screen()
    elif menu == "📆 Agenda dos Médicos":
        agenda_medicos_screen()
