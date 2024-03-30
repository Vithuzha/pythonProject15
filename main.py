from Authentication import authenticate
from HRM import Employee

def main():
    employees = Employee.load_and_save_employees()
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if authenticate(username, password):  # Assuming authenticate function exists
            print("Authentication successful.\n")
            current_user = Employee("E789", "Vithuzha", "Software Developer", "Department of Development", "10.09.2020", "currently working")

            print("Main Menu:")
            print("A. View Personal Information")
            print("B. Add New Employee information")
            print("C. Remove Employee")
            print("D. View All Employee Information")
            print("E. Update Personal Information")
            print("F. Submit Leave Requests")
            print("G. View Company Policies")
            print("H. Access Work Schedules")
            print("I. Logout")
            print("J. Exit")
            while True:
                choice = input("Enter your choice: ")

                if choice == "A":
                    print("")
                    print(current_user.view_emp_info())  # Corrected method call

                elif choice == "B":
                    print("")
                    current_user.add_employee(employees)  # Corrected method call
                    current_user.save_employees(employees)

                elif choice == "C":
                    print("")
                    current_user.remove_employee(employees)  # Corrected method call

                elif choice == "D":
                    print("")
                    Employee.view_employees()

                elif choice == "E":
                    print("")
                    new_position = input("Enter new position: ")
                    new_department = input("Enter new department: ")
                    update_status = current_user.update_emp_info(new_position, new_department)  # Corrected method call
                    print(update_status)

                elif choice == "F":
                    leave_type = input("Enter leave type: ")
                    duration = input("Enter leave duration: ")
                    details = input("Enter leave details: ")
                    leave_request = current_user.submit_leave_request(leave_type, duration, details)  # Corrected method call
                    print(leave_request)
                    print("")
                    print("Your request has been submitted successfully.....")

                elif choice == "G":
                    policies = current_user.view_company_policies()  # Corrected method call
                    print(policies)

                elif choice == "H":
                    schedules = current_user.access_work_schedules()  # Corrected method call
                    print(schedules)

                elif choice == "I":
                    log = input("Do you want to logout ?(yes/no): ")
                    if log == "yes":
                        print("Logging out...\n")
                        break
                    elif log == "no":
                        print("Cancelled....")
                        print("")
                        pass
                    else:
                        print("Invalid input. Please try again....")
                elif choice == "J":
                    while True:
                        out = input("Do you want to exit?(yes / no): ")
                        if out == "no":
                            print("Cancelled....")
                            print("")
                            break
                        elif out == "yes":
                            print("Exiting from the session...")
                            exit()
                        else:
                            print("Invalid input. Please try again......")

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Authentication failed. Please try again.\n")

if __name__ == "__main__":
    main()
