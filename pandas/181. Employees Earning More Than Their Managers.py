## https://leetcode.com/problems/employees-earning-more-than-their-managers/description/?source=submission-ac

import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(employee[['id', 'salary']], left_on='managerId', right_on='id',suffixes=['', '_manager'])
    high_salary_employees = merged_df[merged_df['salary'] > merged_df['salary_manager']]
    high_salary_employees = high_salary_employees.rename(columns={'name': 'Employee'})
    return high_salary_employees['Employee'].to_frame()

