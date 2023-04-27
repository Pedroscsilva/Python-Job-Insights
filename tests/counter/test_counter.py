import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "end") == 5889
    assert count_ocurrences("data/jobs.csv", "END") == 5889
    with pytest.raises(AttributeError):
        count_ocurrences("data/jobs.csv", 4)
