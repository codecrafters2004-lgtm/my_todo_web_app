import streamlit as st
import functions


def add_todo():
    todo = st.session_state.get('new_todo', '').strip()
    if not todo:
        return

    todos = functions.get_todos()
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title("My ToDo App")
st.subheader("This is my ToDo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(functions.get_todos()):
    todo_text = todo.strip()
    checkbox_key = f'todo_{index}_{todo_text}'
    checkbox = st.checkbox(todo_text, key=checkbox_key)
    if checkbox:
        todos = functions.get_todos()
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()


st.text_input(
    label="Enter a todo",
    placeholder="Add a new Todo...",
    on_change=add_todo,
    key='new_todo',
)