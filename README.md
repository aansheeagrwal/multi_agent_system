# Multi-Agent System with Contextual Decisioning & Chained Actions

![Project Logo](https://img.shields.io/badge/Multi--Agent%20System-AI-blue?style=flat-square)

---

## 🚀 Project Overview

The **Multi-Agent System** is an autonomous AI-driven backend that intelligently processes multi-format inputs — including Emails, JSON payloads, and PDF documents — using specialized agents. Each agent extracts structured, meaningful data and chains context-aware follow-up actions dynamically, enabling efficient, automated workflows for complex document handling.

---

## 🎯 Problem Statement

Handling diverse document formats like invoices, emails, and webhooks requires specialized parsing and processing. Manually managing these documents is time-consuming, error-prone, and hard to scale. There is a need for an intelligent system that can:

- 🧠 Detect document type automatically  
- 🔍 Extract key information reliably  
- 🚦 Route data to appropriate handlers (agents)  
- 🤖 Perform context-driven follow-up actions in a seamless chain  

---

## 💡 Solution

Our **Multi-Agent System** solves these challenges by:

- Implementing modular agents for each input format: `email_agent`, `json_agent`, `pdf_agent`  
- Using a **classifier agent** to route incoming files intelligently  
- Extracting structured data like invoice totals, dates, recipients, etc.  
- Dynamically chaining subsequent actions based on extracted content  
- Providing a simple web UI for uploading files and viewing extracted results instantly  

---

## 🔧 Features

✅ Multi-format input support: `.txt`, `.json`, `.pdf`  
✅ Autonomous document classification and routing  
✅ Structured data extraction tailored per document type  
✅ Contextual decision-making and chained task execution  
✅ Lightweight web interface for file upload and result visualization  

---

## 🛠️ Technologies Used

- 🐍 Python 3.10+
- ⚡ FastAPI (backend framework)
- 🔥 Uvicorn (ASGI server)
- 📄 PDF parsing: `PyPDF2`, `pdfminer.six`
- 🧾 JSON and plain text parsing
- 🌐 HTML/CSS/JS (frontend UI)
- 🔑 Environment variables for API key handling
- 🔁 Git (version control)

---

## ⚙️ Getting Started

### ✅ Prerequisites

- Python 3.10 or higher
- Git
- API keys (if using external LLMs like OpenAI or Gemini)

| Service        | Purpose                        | Where to get it                             |
|----------------|--------------------------------|---------------------------------------------|
| OpenAI API     | Language model processing      | https://platform.openai.com                 |
| Google Gemini  | (Optional) Advanced NLP agent  | https://console.cloud.google.com            |

---

### 📦 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/aansheeagrwal/multi_agent_system.git
cd multi_agent_system
```
2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set your API keys as environment variables (example):
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
# On Windows Powershell:
setx OPENAI_API_KEY "your_openai_api_key_here"
```
Alternatively, create a .env file (if your code supports it):
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
▶️Running the Application
-> Start the FastAPI server with Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
Open your browser and go to:
```cpp
http://127.0.0.1:8000/
```
Upload your file (PDF, JSON, or TXT) through the UI and see extracted data in real-time.

📁 Project Structure
```graphql multi_agent_system/
├── agents/                  # Specialized agents for each input type
│   ├── classifier_agent.py
│   ├── email_agent.py
│   ├── json_agent.py
│   └── pdf_agent.py
├── api/                     # API endpoints and routing
│   └── endpoints.py
├── memory/                  # Persistent memory store for context
│   └── memory_store.py
├── router/                  # Action routing logic
│   └── action_router.py
├── static/                  # Frontend static files
│   ├── index.html           # Main UI file for upload & results
│   └── sample_inputs/       # Sample files for testing
├── main.py                  # App entrypoint
├── requirements.txt         # Python dependencies
└── README.md                # This file
```
🤝 Contribution
Contributions are welcome! Feel free to open issues or submit pull requests for enhancements, bug fixes, or new features.

❓ FAQ
Q: Can I add support for more document types?
A: Yes! Simply add a new specialized agent inside agents/ and update the classifier logic to route that type.

Q: Does this system support authentication?
A: Not yet — but it can be integrated easily using FastAPI's security modules or middleware.

🧑‍💻 Author
Made with ❤️ by Anshi Agarwal

