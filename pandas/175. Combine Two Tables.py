# https://leetcode.com/problems/combine-two-tables/description/?lang=pythondata

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # merged_df = pd.merge(person, address, left_on='personId', right_on='personId', how='left',suffixes=('_left', '_right'))
    # return merged_df[['firstName','lastName','city','state']]

    # return pd.merge(person, address, on='personId',how='left')[['firstName','lastName','city','state']]
    
    return pd.merge(left=person, right=address, how='left', on='personId')[['firstName', 'lastName', 'city', 'state']]
    
