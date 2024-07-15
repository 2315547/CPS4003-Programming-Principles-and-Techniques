import json
from data_handler import df


def export_summary_to_json(department, summary):
    """
    Export summarized data for a specific department to JSON format.

    Parameters:
    - department (str): The department for which the summary is generated.
    - summary (dict): A dictionary containing summarized data for the department.
    """
    filename = f"{department}_summary.json"
    with open(filename, 'w') as file:
        json.dump(summary, file, indent=4)
    print(f"Summary for department '{department}' exported to {filename}.")


def generate_department_summary(department):
    """
    Generate a summary of data for a specific department.

    Parameters:
    - department (str): The department for which to generate the summary.

    Returns:
    - summary (dict): A dictionary containing summarized data for the department.
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
