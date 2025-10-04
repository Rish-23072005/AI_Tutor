@echo off
echo Starting local MCP mock + backend + frontend (Windows)
start cmd /k "cd backend && uvicorn app.mcp_mock_server:app --port 8001 --reload"
start cmd /k "cd backend && uvicorn app.main:app --port 8000 --reload"
start cmd /k "cd frontend && streamlit run streamlit_app.py --server.port 8501"
echo All processes started.
