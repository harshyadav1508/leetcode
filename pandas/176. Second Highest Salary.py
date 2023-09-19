# https://leetcode.com/problems/second-highest-salary/description/?lang=pythondata

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary", keep='first', inplace=True)
    SecondHighestSalary = employee.sort_values(by='salary', ascending=False)
    empty_df = pd.DataFrame({'SecondHighestSalary':[None]})
    if len(SecondHighestSalary)<2:
        return empty_df
    return SecondHighestSalary.iloc[1:2]['salary'].to_frame().rename(columns={'salary': 'SecondHighestSalary'})
