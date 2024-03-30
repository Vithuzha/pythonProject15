class EMPLOYEE:
    HRMFILE = "Hrm.txt"
    def __init__(self, emp_id, emp_name,emp_position,emp_department, emp_Hire_date, emp_status):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_position = emp_position
        self.emp_department = emp_department
        self.emp_Hire_date = emp_Hire_date
        self.emp_status = emp_status

    def view_emp_info(self):
        return f"ID:{self.emp_id}\nName:{self.emp_name}\nPosition:{self.emp_position}\nDepartment:{self.emp_department}\nHire_date:{self.emp_Hire_date}\nStatus:{self.emp_status}"

    def update_emp_info(self, new_position, new_Department):
        self.emp_position = new_position
        self.emp_department = new_Department
        return "Personal information Update Successfuly"

classmethod


def view_employees(cls):
        try:
            with open(cls.HRMFILE, "r") as file:
                print("Employee Details:")
                for line in file:
                    emp_id, emp_name, emp_position, emp_department, emp_hire_date, emp_status = line.strip().split(",")
                    print(f"Employee ID: {emp_id}")
                    print(f"Name: {emp_name}")
                    print(f"Position: {emp_position}")
                    print(f"Department: {emp_department}")
                    print(f"Hire Date: {emp_hire_date}")
                    print(f"Employment Status: {emp_status}")
                    print()  # Add a blank line for separation
        except FileNotFoundError:
            print("Employees file not found.")


classmethod
def load_and_save_employees(cls, employees=None):
        if employees is None:
            employees = []
        with open(cls.HRMFILE, "r") as file:
            for line in file:
                emp_id, emp_name, emp_position, emp_department, emp_hire_date, emp_status = line.strip().split(",")
                employees.append(employees(emp_id, emp_name, emp_position, emp_department, emp_hire_date, emp_status))
        return employees

def save_employees(self, employees):
        with open(self.HRMFILE, "w") as file:
            for employee in employees:
                file.write(
                    f"{employee.emp_id},{employee.emp_name},{employee.emp_position},{employee.emp_department},{employee.emp_hire_date},{employee.emp_status}\n")

def add_employee(self, employees):
        emp_id = input("Enter employee ID: ")
        emp_name = input("Enter employee name: ")
        emp_position = input("Enter employee position: ")
        emp_department = input("Enter employee department: ")
        emp_hire_date = input("Enter employee hire date (YYYY-MM-DD): ")
        emp_status = input("Enter employee status: ")
        new_employee = Employee(emp_id, emp_name, emp_position, emp_department, emp_hire_date, emp_status)
        employees.append(new_employee)
        self.save_employees(employees)
        print("Employee added successfully.")


def remove_employee(self, employees):
        emp_id = input("Enter employee ID to remove: ")
        for employee in employees:
            if employee.emp_id == emp_id:
                employees.remove(employee)
                self.save_employees(employees)
                print("Employee removed successfully.")
                return
        print("Employee not found.")


def __submit_leave_request__(self, leave_type, duration, details):
        leave_request = f"Leave Request: Type - {leave_type}, Duration - {duration}, Details - {details}"
        return leave_request

def __view_company_policies__(self):
        policies = """
            Company Policies:
            1. Employee conduct policies
            2. Health and safety Policies
            3. Attendance and time-off Policies
            4. Emergency Leave Policies
            5. Equal opportunity Policies
            6. Workplace Security Policies
            7. Harassment and discrimination Policies
            8. Travel Policies
            9. Professional Development and Training Policies
            10. Remote Work Policies
            11. Social Media and Internet Usage Policy 
                """
        return policies


def __access_work_schedules__(self):
        schedules = """
            Work Schedule:
            Monday: 8:00 AM - 5:00 PM
            Tuesday: 8:00 AM - 5:00 PM
            Wednesday: 8:00 AM - 5:00 PM
            Thursday: 8:00 AM - 5:00 PM
            Friday: 8:00 AM - 5:00 PM
                """
        return schedules

