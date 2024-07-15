import pandas as pd

# Global variable to hold the loaded dataframe
df = None


def load_data(file_path):
    """
    Loads data from CSV file into memory as a pandas DataFrame.

    Args:
    - file_path (str): Path to the CSV file.
    """
    global df
    df = pd.read_csv(file_path)
    print("Data loaded successfully.")


def get_total_records():
    """
    Retrieves the total number of records loaded.

    Returns:
    - int: Total number of records in the DataFrame.
    """
    global df
    if df is not None:
        return len(df)
    else:
        return 0


def get_unique_departments():
    """
    Retrieves a list of unique department names.

    Returns:
    - list: List of unique department names.
    """
    global df
    if df is not None:
        return df['Department'].unique()
    else:
        return []


def get_employee_by_id(employee_id):
    """
    Retrieves employee record(s) based on EmployeeID.

    Args:
    - employee_id (int): EmployeeID to search for.

    Returns:
    - pandas.DataFrame: DataFrame containing employee record(s).
    """
    global df
    if df is not None:
        return df[df['EmployeeID'] == employee_id]
    else:
        return pd.DataFrame()


def get_employees_by_department(department):
    """
    Retrieves employee records for a specific department.

    Args:
    - department (str): Name of the department.

    Returns:
    - pandas.DataFrame: DataFrame containing employee records for the specified department.
    """
    global df
    if df is not None:
        return df[df['Department'] == department]
    else:
        return pd.DataFrame()


def get_employees_by_department_and_role(department, role):
    """
    Retrieves employee records for a specific department and role.

    Args:
    - department (str): Name of the department.
    - role (str): Job role within the department.

    Returns:
    - pandas.DataFrame: DataFrame containing employee records for the specified department and role.
    """
    global df
    if df is not None:
        return df[(df['Department'] == department) & (df['JobRole'] == role)]
    else:
        return pd.DataFrame()


def group_employees_by_job_role():
    """
    Groups employees by job role and returns the count of employees per role.

    Returns:
    - pandas.Series: Series containing counts of employees grouped by job role.
    """
    global df
    if df is not None:
        return df.groupby('JobRole').size()
    else:
        return pd.Series()


def summarize_attrition_data(department):
    """
    Summarizes attrition data for a specific department.

    Args:
    - department (str): Name of the department.

    Returns:
    - dict: Dictionary containing summarized attrition data for the specified department.
    """
    global df
    if df is not None:
        department_data = df[df['Department'] == department]
        summary = {
            'Number of employees': len(department_data),
            'Number of male employees': (department_data['Gender'] == 'Male').sum(),
            'Number of female employees': (department_data['Gender'] == 'Female').sum(),
            'Min age': department_data['Age'].min(),
            'Max age': department_data['Age'].max(),
            'Avg age': department_data['Age'].mean(),
            'Min distance from home': department_data['DistanceFromHome'].min(),
            'Max distance from home': department_data['DistanceFromHome'].max(),
            'Avg distance from home': department_data['DistanceFromHome'].mean(),
            'Min hourly rate': department_data['HourlyRate'].min(),
            'Max hourly rate': department_data['HourlyRate'].max(),
            'Avg hourly rate': department_data['HourlyRate'].mean(),
            'Percentage single': (department_data['MaritalStatus'] == 'Single').mean() * 100,
            'Percentage married': (department_data['MaritalStatus'] == 'Married').mean() * 100,
            'Percentage divorced': (department_data['MaritalStatus'] == 'Divorced').mean() * 100,
            'Percentage frequent business travel': (department_data['BusinessTravel'] == 'Frequently').mean() * 100,
            'Percentage rare business travel': (department_data['BusinessTravel'] == 'Rarely').mean() * 100,
            'Percentage no business travel': (department_data['BusinessTravel'] == 'Never').mean() * 100,
            'Hourly rate mean': department_data['HourlyRate'].mean(),
            'Hourly rate std': department_data['HourlyRate'].std(),
            'Hourly rate variance': department_data['HourlyRate'].var(),
            'Avg work-life balance': department_data['WorkLifeBalance'].mean(),
            'Avg attrition rate': department_data['Attrition'].mean() * 100
        }
        return summary
    else:
        return {}
