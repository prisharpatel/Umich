import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:


    # sort values
    # return nth value 
    unique_salaries = employee.drop_duplicates(subset="salary")
    sorted_salaries = unique_salaries.sort_values(ascending=False, by=['salary']).reset_index(drop=True)

    if N > len(sorted_salaries) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    ans = sorted_salaries['salary'].iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [ans]})




