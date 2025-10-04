@echo off
for /f "tokens=1,2 delims==" %%a in (frontend\.env) do (set %%a=%%b)
echo Starting Streamlit on port %STREAMLIT_PORT%...
start cmd /k "streamlit run streamlit_app.py --server.port %STREAMLIT_PORT%"
