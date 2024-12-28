import streamlit as st

def get_todos():
    """Retrieve todos from session state or initialize empty list"""
    if "todos" not in st.session_state:
        st.session_state.todos = []  # Initialize if not already set
    return st.session_state.todos

def write_todos(todos):
    """Write todos to session state"""
    st.session_state.todos = todos
