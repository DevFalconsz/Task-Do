# Gerenciador de Tarefas Streamlit

Um aplicativo web de gerenciamento de tarefas simples e elegante, construído com Streamlit. Organize suas tarefas em múltiplos projetos, atribua prioridades e acompanhe o progresso de cada item em “To Do”, “In Progress” e “Done”.

---

## 🔧 Tecnologias

- **Python 3.8+**  
- **Streamlit**  
- **JSON** para armazenamento local (`tasks.json`)  
- **CSS inline** para tema escuro e “task cards” estilizados  

---

## ⚙️ Funcionalidades

- 📁 **Projetos**  
  - Crie quantos projetos desejar  
  - Exclua projetos (menos o projeto padrão “My Tasks”)  

- 📝 **Tarefas**  
  - Adicione tarefas com título e prioridade (Alta, Média, Baixa)  
  - Movimente tarefas entre status: To Do → In Progress → Done  
  - Exclua tarefas individualmente  

- 🎨 **Interface**  
  - Tema escuro com “glassmorphism” simplificado  
  - Cards de tarefa com data de criação e prioridade  
  - Layout responsivo em colunas (uma coluna para cada status)  

---

## 🚀 Como Executar

1. **Clone este repositório**  
   ```bash
   git clone https://github.com/DevFalconsz/Task-Do
   cd gerenciador-tarefas-streamlit
   ```
2. **Instale as dependências**
   ```bash
   pip install streamlit
   ```
3. **Execute a aplicação**
   ```bash
   streamlit run main.py
   ```
4. **Acesse no navegador**
   ```bash
   http://localhost:8501
   ```

## 📂 Estrutura de Arquivos
```bash
.
├── app.py            # Código principal (Streamlit)
└── README.md         # Documentação
```

## 📝 Licença
Distribuído sob a Licença MIT.
