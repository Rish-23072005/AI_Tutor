def extract_parameters(prompt: str):
    # Very small heuristic extractor for demo purposes
    params = {}
    lower = prompt.lower()
    if 'python' in lower:
        params['language'] = 'python'
    if 'explain' in lower or 'explanation' in lower:
        params['style'] = 'explanatory'
    # default
    if not params:
        params['language'] = 'generic'
    return params
