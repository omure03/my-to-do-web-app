import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos((todos))



st.title("TO-DO WEBAPP")
st.subheader("This is my first webapp")
Len = len(todos)
st.write("This page's aim is to increase your productivity." +
         " The number of remaining todos: "+ str(Len))


for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(idx)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")