from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    file = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert "title" in file
    assert "salary" in file
    assert "type" in file
