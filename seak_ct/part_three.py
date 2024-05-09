from typing import List, Tuple
from seak_ct.part_two import find_indexes


def find_group(inputs: List[int], length: int) -> List[Tuple]:
    output = []
    last_value = 0
    for idx, input in enumerate(inputs):
        if input < last_value:
            continue
        last_value = input
        for value in inputs[idx:]:
            if value >= last_value + length:
                break
            else:
                last_value = value
        last_value += length
        output.append((input, last_value))
    return output


def highlight_v2(text: str, query: str) -> str:
    idxes = find_indexes(text=text, query=query)
    groups = find_group(idxes, len(query))
    last_length = 0
    string = ""
    for start, end in groups:
        string += text[last_length:start] + "("
        string += text[start:end] + ")"
        last_length = end
    string += text[last_length:]
    return string or text
