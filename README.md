# 🧠 AI Tutor Orchestrator — MVP

A **minimal local implementation** of the **Autonomous AI Tutor Orchestrator** — combining a **FastAPI backend**, **Streamlit frontend**, and a **mock MCP server** for rapid prototyping and hackathon demos.

Empowers students and educational platforms with **autonomous multi-tool AI orchestration**.

---

## 📂 Project Structure

```
ai-tutor-orchestrator/
├── backend/
│   ├── app/                 # FastAPI application modules
│   ├── .env                 # Environment variables (API keys, configs)
│   ├── requirements.txt     # Python dependencies
│   └── run_backend.bat      # Start backend + MCP mock server
├── frontend/
│   ├── streamlit_app.py     # Streamlit frontend UI
│   ├── .env                 # Environment variables
│   └── requirements.txt     # Python dependencies
├── run_local.bat            # Run both backend and frontend together
└── ai_tutor_local.zip       # ZIP archive for local deployment
```

---

## ⚡ Quick Start (Windows)

### 1️⃣ Setup Virtual Environments (Recommended)

```bat
python -m venv venv_backend
python -m venv venv_frontend
```

Activate the environment before installing dependencies.

---

### 2️⃣ Install Dependencies

```bat
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

---

### 3️⃣ Start Services

* **Run both together:**

```bat
run_local.bat
```

* **Or individually:**

```bat
backend\run_backend.bat   # Starts MCP mock + FastAPI backend
frontend\run_frontend.bat # Starts Streamlit frontend
```

---

### 4️⃣ Access the Frontend

Open your browser at:
[http://localhost:8501](http://localhost:8501)

---

## ⚙️ Configuration

* **Environment Variables:**
  `.env` files contain placeholders like:

  ```
  OPENAI_API_KEY=your_key_here
  ```

  Replace with your actual keys for real service integration.

* **MCP (Model Context Protocol):**

  * Local mock server URL: `http://localhost:8001/mcp/process`
  * Backend automatically falls back to a **local simple plan** if MCP is unreachable.

* **LangGraph:**
  Calls are currently mocked in `langgraph_wrapper.py`. Replace with real API calls for full functionality.

---

## 🛠️ Key Files to Inspect / Extend

| File                               | Purpose                           |
| ---------------------------------- | --------------------------------- |
| `backend/app/orchestrator.py`      | Core orchestration logic          |
| `backend/app/mcp_client.py`        | MCP client wrapper                |
| `backend/app/langgraph_wrapper.py` | LangGraph API wrapper (mocked)    |
| `frontend/streamlit_app.py`        | Streamlit UI for user interaction |

---

## 🧩 Workflow Overview

1. **Student Input:** Text, file, or question submitted.
2. **AI Tutor LLM:** Understands intent & context.
3. **Context Analyzer:** Extracts key parameters.
4. **Parameter Extractor & Validator:** Converts input into structured tool parameters.
5. **Tool Handler (MCP):** Routes parameters to appropriate educational tools.
6. **LangGraph Workflow:** Dynamically manages multi-tool workflows.
7. **Tool Execution:** Generates quizzes, summaries, or explanations.
8. **LLM Post-Processing:** Integrates outputs into coherent response.
9. **Response Delivery:** Displayed on Streamlit UI.
10. **Logging & Feedback:** Stores session for adaptive learning and analytics.

---

## ✅ Notes

* **MVP-ready**: Ideal for hackathon demos and local prototyping.
* **Extensible**: Easily integrate real AI agents, LangGraph workflows, and multiple educational tools.
* **Lightweight & Deployable**: Runs on local machines or cloud servers.
* **Designed for Education**: Personalizes learning by orchestrating multiple AI-powered tools seamlessly.

---

## 📌 Future Improvements

* Real-time LangGraph integration with multiple agent workflows.
* Advanced personalization based on student mastery and engagement.
* Support for multiple AI tool APIs beyond the mock setup.
* Analytics dashboard for performance and usage metrics.

---

