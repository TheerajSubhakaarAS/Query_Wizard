import streamlit as st
import requests
import hashlib
import json
import os


st.set_page_config(layout="wide")


CREDENTIALS_FILE = 'users.json'
README_FILE = 'README.md'

def load_users():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(users, file)

def load_readme():
    if os.path.exists(README_FILE):
        with open(README_FILE, 'r') as file:
            return file.read()
    return "README.md file not found."


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'users' not in st.session_state:
    st.session_state.users = load_users()


col1, col2 = st.columns([1, 4])

with col1:
    st.image(r"C:\Users\Theeraj\Desktop\sp\nl_ticket_filter\data\asset\logo.jpg", width=150)

with col2:
    st.title("Natural Language Ticket Query System")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])


if page == "About":
    st.title("About")
    readme_content = load_readme()
    st.markdown(readme_content)
else:

    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.write("**Please log in or register to continue**")

            tab1, tab2 = st.tabs(["Login", "Register"])

            with tab1:
                with st.form(key="login_form"):
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    login_button = st.form_submit_button("Login")

                if login_button:
                    if username in st.session_state.users and st.session_state.users[username] == hash_password(password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success(f"Logged in as {username}")
                    else:
                        st.error("Invalid credentials, please try again.")

            with tab2:
                with st.form(key="register_form"):
                    new_username = st.text_input("New Username")
                    new_password = st.text_input("New Password", type="password")
                    register_button = st.form_submit_button("Register")

                if register_button:
                    if new_username in st.session_state.users:
                        st.error("Username already exists. Please choose a different username.")
                    else:
                        st.session_state.users[new_username] = hash_password(new_password)
                        save_users(st.session_state.users)  
                        st.success(f"User {new_username} registered successfully. Please log in.")
    else:

        st.sidebar.header(f"Welcome, {st.session_state.username}!")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.sql_query = None
            st.session_state.initial_results = None
            st.success("You have successfully logged out.")
            st.rerun()  


        if st.session_state.logged_in:
            if 'sql_query' not in st.session_state:
                st.session_state.sql_query = None
            if 'initial_results' not in st.session_state:
                st.session_state.initial_results = None

            query = st.text_input("Enter your ticket-related question:", key="query_input")

            if st.button("Submit"):
                response = requests.post("http://localhost:8000/process_query/", json={"question": query})
                
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.sql_query = data['query']
                    st.session_state.initial_results = data['results']
                else:
                    st.write("Error in processing your request.")

            if st.session_state.sql_query:
                st.write("SQL Query Interpretation:")
                sql_query = st.text_area("Review/Refine the SQL Query:", value=st.session_state.sql_query, height=150)

                if st.button("Refine and Resubmit"):
                    refined_response = requests.post("http://localhost:8000/process_query/", json={"question": query, "refined_sql": sql_query})
                    if refined_response.status_code == 200:
                        refined_data = refined_response.json()
                        st.write("Refined Query Results:")
                        st.write(refined_data['results'])
                    else:
                        st.write("Error in processing the refined query.")
                
                st.markdown("### Initial Query Results:")
                st.write(st.session_state.initial_results)
