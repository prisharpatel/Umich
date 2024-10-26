import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # number of bank accounts for each salary category
    low_sal = len(accounts[accounts["income"] < 20000])
    
    avg_sal = len(accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)])
    # print(accounts[(accounts["income"] > 20000) & (accounts["income"] < 50000)])
    high_sal = len(accounts[accounts["income"] > 50000])
    return pd.DataFrame({"category": ["Low Salary", "Average Salary", "High Salary"], "accounts_count": [low_sal, avg_sal, high_sal]})    