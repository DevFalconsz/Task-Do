import streamlit as st
import json
import os
from datetime import datetime

# === CONFIGURAÇÕES DE INTERFACE ===
st.set_page_config(page_title="Gerenciador de Tarefas", layout="wide")
st.markdown(
    """
    <style>
    body { background-color: #121212; color: white; }
    .task-card { background-color: #1e1e1e; padding: 15px; margin-bottom: 10px; border-radius: 10px; box-shadow: 0 0 5px rgba(255,255,255,0.05); }
    .task-actions { margin-top: 10px; }
    .task-button { background-color: #333; color: white; border: 1px solid #444; border-radius: 6px; padding: 5px 10px; margin-right: 6px; }
    .task-button:hover { background-color: #555; }
    .delete-project { background-color: #cc0000; margin-top: 10px; }
    .delete-project:hover { background-color: #990000; }
    </style>
    """,
    unsafe_allow_html=True
)

# === FUNÇÕES ===
DATA_FILE = "tasks.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"My Tasks": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task(project, title, priority):
    data = load_data()
    data.setdefault(project, [])
    data[project].append({
        "title": title,
        "priority": priority,
        "status": "To Do",
        "created": datetime.now().strftime("%d %b %H:%M")
    })
    save_data(data)

def update_task(project, index, status):
    data = load_data()
    data[project][index]["status"] = status
    save_data(data)

def delete_task(project, index):
    data = load_data()
    data[project].pop(index)
    save_data(data)

def delete_project(project):
    data = load_data()
    # Remove projeto inteiro
    data.pop(project, None)
    save_data(data)

# === INTERFACE ===
st.sidebar.header("📁 Projetos")

data = load_data()
project_names = list(data.keys())
selected_project = st.sidebar.radio("Selecionar projeto", project_names)

# Botão de exclusão de projeto
if selected_project != "My Tasks":
    if st.sidebar.button("🗑️ Excluir projeto", key="del_proj"):
        delete_project(selected_project)
        st.rerun()  # ([docs.streamlit.io](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun?utm_source=chatgpt.com))

new_project = st.sidebar.text_input("Novo projeto")
if st.sidebar.button("Criar projeto") and new_project:
    if new_project not in data:
        data[new_project] = []
        save_data(data)
        st.rerun()  # ([docs.streamlit.io](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun?utm_source=chatgpt.com))

# === DASHBOARD ===
st.markdown(f"## 🎯 {selected_project}")

statuses = ["To Do", "In Progress", "Done"]
cols = st.columns(3)

for i, status in enumerate(statuses):
    with cols[i]:
        st.markdown(f"### {status}")
        for idx, task in enumerate(data[selected_project]):
            if task["status"] == status:
                with st.container():
                    st.markdown(
                        f"<div class='task-card'><strong>{task['title']}</strong><br>"
                        f"<small>Prioridade: {task['priority']} • Criado: {task['created']}</small></div>",
                        unsafe_allow_html=True
                    )
                    # Ações da tarefa
                    colA, colB, colC = st.columns([1, 1, 1])
                    with colA:
                        if status != "In Progress" and st.button("→ In Progress", key=f"to_in_{idx}"):
                            update_task(selected_project, idx, "In Progress")
                            st.rerun()  # ([docs.streamlit.io](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun?utm_source=chatgpt.com))
                    with colB:
                        if status != "Done" and st.button("→ Done", key=f"to_done_{idx}"):
                            update_task(selected_project, idx, "Done")
                            st.rerun()  # ([docs.streamlit.io](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun?utm_source=chatgpt.com))
                    with colC:
                        if st.button("❌", key=f"del_{idx}"):
                            delete_task(selected_project, idx)
                            st.rerun()  # ([docs.streamlit.io](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun?utm_source=chatgpt.com))

# === ADICIONAR NOVA TAREFA ===
with st.expander("Adicionar nova tarefa"):
    col1, col2 = st.columns([4, 2])
    with col1:
        new_task = st.text_input("Tarefa", key="nova_tarefa")
    with col2:
        new_priority = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"], key="nova_prioridade")
    if st.button("Adicionar tarefa"):
        if new_task:
            add_task(selected_project, new_task, new_priority)
            st.rerun()  # ([docs.streamlit.io](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun?utm_source=chatgpt.com))
