from typing import Union, List, Dict
from src.insights.jobs import read
import math


def int_conv(num):
    try:
        return int(num)
    except ValueError:
        return math.nan


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    all_jobs = read(path)
    max_salaries = [
        int_conv(job["max_salary"]) for job in all_jobs if job["max_salary"]
        ]
    return max(filter(lambda x: not math.isnan(x), max_salaries))
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """

    all_jobs = read(path)
    min_salaries = [
        int_conv(job["min_salary"]) for job in all_jobs if job["min_salary"]
        ]
    return min(filter(lambda x: not math.isnan(x), min_salaries))
    # raise NotImplementedError


def validate_salary_filter(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        print(type(job["min_salary"]))
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if type(salary) == "string" and not salary.isnumeric():
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    validate_salary_filter(job, salary)

    return job["min_salary"] <= int(salary) <= job["max_salary"]
    #     return True
    # else:
    #     return False
    # raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
