from src.pre_built.sorting import sort_by

unordered_jobs = [
    {"min_salary": 1000, "max_salary": 4200, "date_posted": "2020-05-08"},
    {"min_salary": 1500, "max_salary": 4000, "date_posted": "2020-05-11"},
    {"min_salary": 700, "max_salary": 2200, "date_posted": "2020-05-15"}
]

min_ordered = [
    {"min_salary": 700, "max_salary": 4200, "date_posted": "2020-05-15"},
    {"min_salary": 1000, "max_salary": 2000, "date_posted": "2020-05-08"},
    {"min_salary": 1500, "max_salary": 4000, "date_posted": "2020-05-11"}
]

max_ordered = [
    {"min_salary": 1000, "max_salary": 2000, "date_posted": "2020-05-08"},
    {"min_salary": 1500, "max_salary": 4000, "date_posted": "2020-05-11"},
    {"min_salary": 700, "max_salary": 4200, "date_posted": "2020-05-15"}
]

date_ordered = [
    {"min_salary": 1000, "max_salary": 2000, "date_posted": "2020-05-08"},
    {"min_salary": 1500, "max_salary": 4000, "date_posted": "2020-05-11"},
    {"min_salary": 700, "max_salary": 4200, "date_posted": "2020-05-15"}
]


def test_sort_by_criteria():
    assert sort_by(unordered_jobs, "min_salary") == min_ordered
    assert sort_by(unordered_jobs, "max_ordered") == max_ordered
    assert sort_by(unordered_jobs, "date_ordered") == date_ordered
