# https://leetcode.com/problems/customers-who-never-order/?lang=pythondata

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left',suffixes=('_left', '_right'))
    return merged_df.loc[merged_df["customerId"].isna(),["name"]].rename(columns={'name': 'Customers'})

    
