# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?lang=pythondata

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # customer_counts = orders['customer_number'].value_counts()
    # if len(customer_counts)==0:
    #     empty_df = pd.DataFrame()
    #     empty_df['customer_number'] = []
    #     return empty_df
    # return pd.DataFrame({'customer_number': [customer_counts.idxmax()]})
    return orders["customer_number"].mode().to_frame()
    
