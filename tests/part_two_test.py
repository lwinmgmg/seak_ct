from seak_ct.part_two import find_indexes


def test_find_indexes():
    # Arrange
    expected_results = [
        {"input": ("banana", "ana"), "output": [1, 3]},
        {"input": ("hello world", "ana"), "output": []},
        {"input": ("hello world", "hell"), "output": [0]},
    ]
    # Act
    for expected_result in expected_results:
        input = expected_result["input"]
        output = expected_result["output"]
        res = find_indexes(*input)
        # Assert
        assert len(res) == len(output)
        for idx in range(len(res)):
            assert res[idx] == output[idx]
