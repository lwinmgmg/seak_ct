def find_indexes(text: str, query: str) -> list:
    output = []
    last_idx = 0
    while query in text:
        idx = text.index(query)
        last_idx += idx
        output.append(last_idx)
        text = text[idx + 1 :]
        last_idx += 1
    return output
