# https://leetcode.com/problems/second-highest-salary/description/?lang=pythondata

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    SecondHighestSalary=employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(SecondHighestSalary)<2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return pd.DataFrame({'SecondHighestSalary':[SecondHighestSalary.iloc[1]]})
