import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
API_BASE = os.getenv('API_BASE', 'http://localhost:8000')

st.set_page_config(page_title='AI Tutor (Local)', layout='centered')

st.title('AI Tutor — Local Orchestrator Demo')


prompt = st.text_area('Enter a prompt for the AI Tutor', height=200)
teaching_style = st.selectbox('Teaching Style', ['Direct', 'Socratic', 'Visual', 'Flipped Classroom'])
emotional_state = st.selectbox('Emotional State', ['Focused', 'Anxious', 'Confused', 'Tired'])
mastery_level = st.slider('Mastery Level (1-10)', 1, 10, 5)
tool = st.selectbox('Tool', ['note_maker', 'flashcard_generator', 'concept_explainer'])


# Mock user_info for demo/testing
user_info = {
    "user_id": "student123",
    "name": "Demo Student",
    "grade_level": "7",
    "learning_style_summary": "Prefers outlines and structured notes",
    "emotional_state_summary": emotional_state,
    "mastery_level_summary": f"Level {mastery_level}: Foundation"
}
# Mock chat_history for demo/testing
chat_history = [
    {"role": "user", "content": prompt}
]

extra_params = {}
if tool == 'note_maker':
    extra_params['topic'] = st.text_input('Note Topic', '')
    extra_params['subject'] = st.text_input('Note Subject', '')
    extra_params['chat_history'] = chat_history
    extra_params['user_info'] = user_info
    extra_params['note_taking_style'] = st.selectbox('Note Taking Style', ['outline', 'bullet_points', 'narrative', 'structured'])
    extra_params['include_examples'] = st.checkbox('Include Examples', value=True)
    extra_params['include_analogies'] = st.checkbox('Include Analogies', value=False)
elif tool == 'flashcard_generator':
    extra_params['topic'] = st.text_input('Flashcard Topic', '')
    extra_params['subject'] = st.text_input('Flashcard Subject', '')
    extra_params['count'] = st.slider('Number of Flashcards', 1, 20, 5)
    extra_params['difficulty'] = st.selectbox('Difficulty', ['easy', 'medium', 'hard'])
    extra_params['include_examples'] = st.checkbox('Include Examples', value=True)
    extra_params['user_info'] = user_info
    extra_params['chat_history'] = chat_history
elif tool == 'concept_explainer':
    extra_params['concept_to_explain'] = st.text_input('Concept to Explain', '')
    extra_params['current_topic'] = st.text_input('Current Topic', '')
    extra_params['chat_history'] = chat_history
    extra_params['user_info'] = user_info
    extra_params['desired_depth'] = st.selectbox('Desired Depth', ['basic', 'intermediate', 'advanced', 'comprehensive'])

if st.button('Send'):
    if not prompt.strip():
        st.warning('Please enter a prompt.')
    else:
        try:
            with st.spinner('Contacting backend...'):
                payload = {
                    'prompt': prompt,
                    'teaching_style': teaching_style,
                    'emotional_state': emotional_state,
                    'mastery_level': mastery_level,
                    'tool': tool,
                    'extra_params': extra_params
                }
                resp = requests.post(f"{API_BASE}/orchestrate", json=payload, timeout=15)
                data = resp.json()
            if data.get('ok'):
                st.success('Received response from orchestrator')
                st.json(data['result'])
            else:
                st.error('Backend returned an error')
                st.write(data)
        except requests.RequestException as e:
            st.error(f'Error contacting backend: {e}')
