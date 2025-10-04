def validate_prompt(prompt: str):
    if not prompt or not prompt.strip():
        raise ValueError('Prompt must not be empty')
    if len(prompt) > 5000:
        raise ValueError('Prompt too long (limit 5000 chars)')
