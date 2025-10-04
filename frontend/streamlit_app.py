import streamlit as st
import os, requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
API_BASE = os.getenv('API_BASE', 'http://localhost:8000')

st.set_page_config(page_title='AI Tutor (Local)', layout='centered')

st.title('AI Tutor — Local Orchestrator Demo')

prompt = st.text_area('Enter a prompt for the AI Tutor', height=200)
if st.button('Send'):
    if not prompt.strip():
        st.warning('Please enter a prompt.')
    else:
        try:
            with st.spinner('Contacting backend...'):
                resp = requests.post(f"{API_BASE}/orchestrate", json={'prompt': prompt}, timeout=10)
                data = resp.json()
            if data.get('ok'):
                st.success('Received response from orchestrator')
                st.json(data['result'])
            else:
                st.error('Backend returned an error')
                st.write(data)
        except Exception as e:
            st.error(f'Error contacting backend: {e}')
