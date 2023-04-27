import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("tests/mocks/jobs_with_types.csv", "end") == 3
    assert count_ocurrences("tests/mocks/jobs_with_types.csv", "END") == 3
    with pytest.raises(TypeError):
        count_ocurrences("tests/mocks/jobs_with_types.csv", 4)
