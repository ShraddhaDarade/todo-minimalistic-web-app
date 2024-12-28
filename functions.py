import os


# Update the filepath to point to the renamed file
filepath = "/Users/shraddhadarade/Desktop/PROJECTS WINTER BREAK/Todo_web_app/todos.txt"


def get_todos():
    """Read the text file and return the list of todo items."""
    if not os.path.exists(filepath):  # Check if the file exists
        return []  # Return an empty list if file does not exist

    with open(filepath, 'r') as file:
        todos = file.readlines()
    
    todos = [todo.strip() for todo in todos]  # Remove trailing whitespace
    return todos

def write_todos(todos):
    """Write the to-do items list to the text file."""
    with open(filepath, 'w') as file:
        file.writelines([f"{todo}\n" for todo in todos])


print(f"Writing todos to: {filepath}")
