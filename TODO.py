import streamlit as st 



# Initialize session state
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

# Title
st.title("Welcome to To-Do List.")


st.subheader('Interactive To-Do List')

# Input for new task
new_task = st.text_input('Add a new task',placeholder="1:00-2:00 am -> Cook Lunch")


select_option = st.selectbox("select a day",options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"])
st.write(select_option)
# Add task button
if st.button('Add Task'):
    st.session_state.todo_list.append(new_task)
    
# Display tasks
st.write('Your To-Do List:')
for i, task in enumerate(st.session_state.todo_list):
    col1, col2 = st.columns([1, 2])
    col1.write(f"{i+1}. {task}")
    if col2.button(f'Remove {i+1}', key=f'remove_{i}'):
        del st.session_state.todo_list[i]
