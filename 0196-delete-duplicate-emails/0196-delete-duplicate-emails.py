import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # drop_duplicates()
    # delete all duplicate emails - keep one with smallest id 
    # sort by emails and then sort by ids and then do drop duplicates with keep first and delete rest
    person.sort_values(by="id", inplace=True)
    # print(person)
    person.drop_duplicates(subset="email", inplace=True)
    
    # return person
    