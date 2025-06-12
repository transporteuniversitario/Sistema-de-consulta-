import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS medicos (nome TEXT, especialidade TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS pacientes (nome TEXT, telefone TEXT, observacoes TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS agendamentos (paciente TEXT, medico TEXT, data TEXT, hora TEXT, status TEXT)''')
    conn.commit()
    conn.close()
