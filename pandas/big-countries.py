# https://leetcode.com/problems/big-countries/?lang=pythondata

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # return world.query('(area >= 3_000_000) | (population >=25_000_000)')[['name','population','area']]
    # return world[
    #     (world['area'] >= 3_000_000)
    #     |
    #    (world['population'] >= 25_000_000)
    # ][['name','population','area']]
    return world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ['name','population','area']]
    
