import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # report number of csutomers who had at least one bill wtih an amount greater than 500 
    # grouo by customer id 
    store.groupby(by="customer_id")
    # sort values by amount descending
    store.sort_values(by="amount", inplace=True, ascending=False)
    # drop duplicates based on customer_id and only keep first  
    # print(store)
    store.drop_duplicates(subset="customer_id", inplace=True)
    # print(store)
    # filter based on if amount is greater than 500
    answer = len(store[(store["amount"] > 500)])
    return pd.DataFrame({'rich_count':[answer]})
    
    