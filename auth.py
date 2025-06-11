import streamlit as st
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", 
              ("admin", hash_password("admin")))
    conn.commit()
    conn.close()

def login_screen():
    create_users_table()
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                  (username, hash_password(password)))
        result = c.fetchone()
        conn.close()
        if result:
            st.session_state.logged_in = True
        else:
            st.error("Usuário ou senha incorretos.")
