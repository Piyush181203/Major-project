import streamlit as st
import sqlite3
import jwt
from datetime import datetime, timedelta

# ---------------- CONFIG ----------------
SECRET = "secret123"

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

db = get_db()

def init_db():
    db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    db.commit()

init_db()

# ---------------- AUTH FUNCTIONS ----------------
def create_user(username, password):
    try:
        db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        db.commit()
        return True
    except:
        return False

def get_user(username, password):
    return db.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()

def generate_token(user_id):
    return jwt.encode({
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=5)
    }, SECRET, algorithm="HS256")

# ---------------- UI ----------------
st.set_page_config(page_title="Auth System", layout="centered")

if "token" not in st.session_state:
    st.session_state.token = None

menu = st.sidebar.radio("Menu", ["Register", "Login", "Dashboard"])

# ---------------- REGISTER ----------------
if menu == "Register":
    st.title("📝 Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if create_user(username, password):
            st.success("User registered ✅")
        else:
            st.error("User already exists ❌")

# ---------------- LOGIN ----------------
elif menu == "Login":
    st.title("🔑 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user(username, password)

        if not user:
            st.error("Invalid credentials ❌")
        else:
            token = generate_token(user["id"])
            st.session_state.token = token
            st.success("Login successful 🎉")

# ---------------- DASHBOARD ----------------
elif menu == "Dashboard":
    st.title("📊 Dashboard")

    if not st.session_state.token:
        st.warning("Please login first ⚠️")
    else:
        st.success("Welcome to dashboard 🚀")

        decoded = jwt.decode(
            st.session_state.token,
            SECRET,
            algorithms=["HS256"]
        )

        st.write(f"User ID: {decoded['user_id']}")