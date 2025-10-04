@echo off
REM Load .env variables for Windows (simple)
for /f "tokens=1,2 delims==" %%a in (backend\.env) do (set %%a=%%b)
echo Starting MCP mock server on port 8001...
start cmd /k "uvicorn app.mcp_mock_server:app --port 8001 --reload"
echo Starting backend FastAPI on port %API_PORT%...
start cmd /k "uvicorn app.main:app --port %API_PORT% --reload"
