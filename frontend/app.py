import streamlit as st
import requests

API = "http://127.0.0.1:5000/api"

st.set_page_config(page_title="Premium Dashboard", layout="wide")

# Session state
if "token" not in st.session_state:
    st.session_state.token = None

st.title("🚀 Partner Management System")

menu = st.sidebar.radio("Navigation", ["Login", "Register", "Dashboard"])

# ---------------- REGISTER ----------------
if menu == "Register":
    st.subheader("Create Account")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Register"):
        res = requests.post(f"{API}/auth/register", json={"username": u, "password": p})
        st.success(res.json().get("msg", "Done"))

# ---------------- LOGIN ----------------
elif menu == "Login":
    st.subheader("Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{API}/auth/login", json={"username": u, "password": p})

        if res.status_code == 200:
            st.session_state.token = res.json()["token"]
            st.success("Logged in 🎉")
        else:
            st.error("Invalid credentials")

# ---------------- DASHBOARD ----------------
elif menu == "Dashboard":
    st.subheader("Dashboard")

    if not st.session_state.token:
        st.warning("Please login first")
    else:
        headers = {"Authorization": st.session_state.token}
        res = requests.get(f"{API}/dashboard/data", headers=headers)

        if res.status_code == 200:
            data = res.json()
            st.success(data["message"])
            st.write(f"User ID: {data['user_id']}")
        else:
            st.error("Session expired")
