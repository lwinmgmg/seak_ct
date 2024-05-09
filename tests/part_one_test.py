from seak_ct.part_one import highlight


def test_highlight():
    # Arrange
    expected_results = [
        {"input": ("banana", "ana"), "output": "b(ana)na"},
        {"input": ("hello world", "ana"), "output": "hello world"},
        {"input": ("hello world", "hell"), "output": "(hell)o world"},
    ]
    # Act
    for expected_result in expected_results:
        input = expected_result["input"]
        output = expected_result["output"]
        res = highlight(*input)
        # Assert
        assert res == output
