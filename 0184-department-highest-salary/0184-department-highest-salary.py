import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # group by departmentID
    # select highest salary from that 

    df = employee.merge(department, left_on="departmentId", right_on="id", how="left")

    # group by department column
    # max_salary = df.groupby("Department")['Salary'].transform("max")

    df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)

    max_salary = df.groupby('Department')['Salary'].transform('max')


    df = df[df['Salary'] == max_salary]
    return df[['Department', 'Employee', 'Salary']]

