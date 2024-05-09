from seak_ct.part_three import highlight_v2, find_group


def test_highlight_v2():
    # Arrange
    expected_results = [
        {"input": ("bana", "ana"), "output": "b(ana)"},
        {"input": ("banana", "ana"), "output": "b(anana)"},
        {"input": ("banana anana anna", "ana"), "output": "b(anana) (anana) anna"},
        {"input": ("banana", "hell"), "output": "banana"},
    ]
    # Act
    for expected_result in expected_results:
        input = expected_result["input"]
        output = expected_result["output"]
        res = highlight_v2(*input)
        # Assert
        assert res == output


def test_find_group():
    # Arrange
    expected_results = [
        {"input": ([1], 3), "output": [(1, 4)]},
        {"input": ([2, 4], 1), "output": [(2, 3), (4, 5)]},
        {"input": ([2, 4, 10], 3), "output": [(2, 7), (10, 13)]},
        {"input": ([2, 4, 10], 2), "output": [(2, 4), (4, 6), (10, 12)]},
    ]
    # Act
    for expected_result in expected_results:
        input = expected_result["input"]
        output = expected_result["output"]
        res = find_group(*input)
        # Assert
        assert len(res) == len(output)
        for idx in range(len(res)):
            assert res[idx] == output[idx]
