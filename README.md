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

basic_chatbot_langchain/
│
├── app.py
└── src/
└── langgraphagenticai/
├── ui/
│ ├── streamlitui/
│ │ ├── loadui.py
│ │ └── display_result.py
│ └── uiconfigfile.ini
| |__ uiconfigfile.py
│
├── graph/
│ └── graph_builder.py
│
├── nodes/
│ └── basic_chatbot_node.py
| |__chatbot_with_tool_node.py
│
├── llms/
│ └── groqllm.py
│
├── state/
│ └── state.py
|
|__ tools/
| |__search_tool.py
│
└── main.py
|
|__app.py

## 🛠️ Installation & Setup

### **1️⃣ Clone the repository**

git clone https://github.com/<your-username>/basic_chatbot_langchain.git
cd basic_chatbot_langchain


### **2️⃣ Create a virtual environment**

conda create -p venv python=3.13
conda activate ./venv


python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

### **3️⃣ Install dependencies**
pip install -r requirements.txt

### **4️⃣ Run the Streamlit app**
streamlit run app.py