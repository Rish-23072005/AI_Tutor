def safe_truncate(text: str, length: int = 120):
    return text if len(text) <= length else text[:length] + '...'
