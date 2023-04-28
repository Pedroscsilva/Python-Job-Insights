import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def unordered_jobs():
    return [
        {"date_posted": "2020-05-08", "max_salary": 2000, "min_salary": 1000},
        {"date_posted": "2020-05-11", "max_salary": 4000, "min_salary": 1500},
        {"date_posted": "2020-05-15", "max_salary": 4200, "min_salary": 700}
    ]


def test_sort_by_criteria(unordered_jobs):
    copy_of_jobs = unordered_jobs.copy()

    sort_by(copy_of_jobs, "min_salary")
    assert copy_of_jobs[0]["min_salary"] == 700
    assert copy_of_jobs[1]["min_salary"] == 1000
    assert copy_of_jobs[2]["min_salary"] == 1500

    sort_by(copy_of_jobs, "max_salary")
    assert copy_of_jobs[0]["max_salary"] == 4200
    assert copy_of_jobs[1]["max_salary"] == 4000
    assert copy_of_jobs[2]["max_salary"] == 2000

    sort_by(copy_of_jobs, "date_posted")
    assert copy_of_jobs[0]["date_posted"] == "2020-05-15"
    assert copy_of_jobs[1]["date_posted"] == "2020-05-11"
    assert copy_of_jobs[2]["date_posted"] == "2020-05-08"
