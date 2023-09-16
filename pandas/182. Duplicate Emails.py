# https://leetcode.com/problems/duplicate-emails/description/

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
  person = person.rename(columns={'email':'Email'})
  return person[person['Email'].duplicated()]['Email'].to_frame().drop_duplicates()

