# main.py

import data_handler as dh
import data_visualiser as dv

def display_menu():
    print("\n===== Nurse Attrition Analysis Tool =====")
    print("1. Load Data")
    print("2. Display Total Number of Records")
    print("3. List Unique Departments")
    print("4. Retrieve Employee Record by ID")
    print("5. Retrieve Employees by Department")
    print("6. Retrieve Employees by Department and Role")
    print("7. Group Employees by Job Role")
    print("8. Summary of Attrition Data for a Department")
    print("9. Visualize Data: Pie Chart of Employees per Department")
    print("0. Exit")

def process_option(option):
    if option == '1':
        file_path = input("Enter the file path of the CSV: ")
        dh.load_data(file_path)
    elif option == '2':
        total_records = dh.get_total_records()
        print(f"Total number of records loaded: {total_records}")
    elif option == '3':
        unique_departments = dh.get_unique_departments()
        print("Unique departments:")
        for dept in unique_departments:
            print(dept)
    elif option == '4':
        employee_id = int(input("Enter Employee ID: "))
        employee_record = dh.get_employee_by_id(employee_id)
        if not employee_record.empty:
            print(employee_record)
        else:
            print(f"No employee found with ID {employee_id}.")
    elif option == '5':
        department = input("Enter Department Name: ")
        employees_by_dept = dh.get_employees_by_department(department)
        print(employees_by_dept)
    elif option == '6':
        department = input("Enter Department Name: ")
        role = input("Enter Job Role: ")
        employees_by_dept_role = dh.get_employees_by_department_and_role(department, role)
        print(employees_by_dept_role)
    elif option == '7':
        grouped_by_role = dh.group_employees_by_job_role()
        print("Employees grouped by job role:")
        print(grouped_by_role)
    elif option == '8':
        department = input("Enter Department Name: ")
        summary = dh.summarize_attrition_data(department)
        if summary:
            for key, value in summary.items():
                print(f"{key}: {value}")
        else:
            print(f"No data found for department {department}.")
    elif option == '9':
        dv.visualize_department_pie_chart()
    elif option == '0':
        print("Exiting the program...")
        return False
    else:
        print("Invalid option. Please choose again.")
    return True

def main():
    while True:
        display_menu()
        option = input("Enter your choice (0-9): ")
        if not process_option(option):
            break

if __name__ == "__main__":
    main()
