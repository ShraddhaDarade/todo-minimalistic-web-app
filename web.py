import streamlit as st
import functions

# Fetch the todos from the file
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)
    
    # Clear the input field
    st.session_state["new_todo"] = ""

# Set up the app title and description
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Create a list to store todos that need to be removed
todos_to_remove = []

# Display todos with checkboxes
for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    
    # If the checkbox is checked, add the todo to the removal list
    if checkbox:
        todos_to_remove.append(todo)

# Remove checked todos after the loop
for todo in todos_to_remove:
    todos.remove(todo)

# Write the updated todos list back to the file
if todos_to_remove:
    functions.write_todos(todos)

# Input field to add a new todo
st.text_input(label="Add a new todo", 
              placeholder="Enter your new todo", 
              on_change=add_todo, 
              key="new_todo")
