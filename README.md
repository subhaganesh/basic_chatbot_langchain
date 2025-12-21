# 🚀 Basic LangGraph + LangChain Chatbot (with Tools) — Streamlit Application

A modular and extensible chatbot application built using:

- **LangGraph** – for agent workflows  
- **LangChain** – for LLM orchestration  
- **Streamlit** – for the UI  
- **Groq** – fast, free LLM inference  
- **Tools (optional)** – extend the chatbot with additional actions  

This project demonstrates how to build a basic chatbot using a graph-based pipeline that processes user messages through a configurable LLM setup.

---

## ✨ Features

- **Modular Architecture** — Clear separation of UI, graph logic, nodes, and model configs  
- **LangGraph Integration** — Build agent workflows using nodes & edges  
- **Dynamic Streamlit UI** — Select LLM provider, model, use case, and enter API keys  
- **Supports Multiple LLM Models** — LLaMA 3, Mixtral, and more  
- **Easy to Extend** — Add new use cases, nodes, or tool-enabled agents  

---

## 🏗️ Project Structure
```mermaid
graph TD

    A[basic_chatbot_langchain] --> B[app.py]

    A --> C[src]
    C --> D[langgraphagenticai]

    %% UI
    D --> E[ui]
    E --> F[streamlitui]
    F --> F1[loadui.py]
    F --> F2[display_result.py]
    E --> E1[uiconfigfile.ini]
    E --> E2[uiconfigfile.py]

    %% Graph
    D --> G[graph]
    G --> G1[graph_builder.py]

    %% Nodes
    D --> H[nodes]
    H --> H1[basic_chatbot_node.py]
    H --> H2[chatbot_with_tool_node.py]

    %% LLMs
    D --> I[llms]
    I --> I1[groqllm.py]

    %% State
    D --> J[state]
    J --> J1[state.py]

    %% Tools
    D --> K[tools]
    K --> K1[search_tool.py]

    %% Main file
    D --> L[main.py]

    %% Root-level app
    A --> M[app.py]
---
## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/<your-username>/basic_chatbot_langchain.git  
cd basic_chatbot_langchain

---
### 2️⃣ Create a virtual environment

**Option A — Using Conda**  
conda create -p venv python=3.13  
conda activate ./venv  

**Option B — Using Python venv**  
python -m venv venv  

**Activate the environment:**  
Windows: venv\Scripts\activate  
Mac/Linux: source venv/bin/activate  

---

### 3️⃣ Install dependencies
pip install -r requirements.txt

---

### 4️⃣ Run the Streamlit app
streamlit run app.py
