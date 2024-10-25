import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # preferred delivery date is the same as the order date 
    # order is called immediate 
    # else called scheduled

    filtered_immediate = delivery[(delivery["order_date"] == delivery["customer_pref_delivery_date"])]
    ans = (len(filtered_immediate) / len(delivery))*100
    
    value = pd.DataFrame({"immediate_percentage":[ans]})
    return value.round(2)
         