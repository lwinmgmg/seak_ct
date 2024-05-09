def highlight(text: str, query: str) -> str:
    query_length = len(query)
    if query in text:
        idx = text.index(query)
        return f"{text[:idx]}({query}){text[idx + query_length:]}"
    return text
