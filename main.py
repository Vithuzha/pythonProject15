from Authentication import check
from hrm import Employee

def main():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if check(username, password):
            print("Authentication successful.\n")
            employees = Employee.load_and_save_employees()

            while True:
                print("Main Menu:")
                print("A. View Employee Information")
                print("B. Add New Employee information")
                print("C. Remove Employee")
                print("D. View All Employee Information")
                print("E. Update Personal Information")
                print("F. Submit Leave Requests")
                print("G. View Company Policies")
                print("H. Access Work Schedules")
                print("I. Logout")
                print("J. Exit")

                choice = input("Enter your choice: ").upper()

                if choice == "A":
                    print("")
                    current_user = Employee("E789", "Vithuzha", "Software Developer", "Department of Development", "10.09.2020", "currently working")
                    print(current_user.__view_emp_info__())

                elif choice == "B":
                    print("")
                    current_user.add_employee(employees)
                    current_user.save_employees(employees)

                elif choice == "C":
                    print("")
                    current_user.remove_employee(employees)

                elif choice == "D":
                    print("")
                    Employee.view_employees()

                elif choice == "E":
                    print("")
                    new_position = input("Enter new position: ")
                    new_department = input("Enter new department: ")
                    update_status = current_user.__update_personal_info__(new_position, new_department)
                    print(update_status)

                elif choice == "F":
                    leave_type = input("Enter leave type: ")
                    duration = input("Enter duration: ")
                    details = input("Enter more details: ")
                    leave_request = current_user.__submit_leave_request__(leave_type, duration, details)
                    print(leave_request)
                    print("")
                    print("Your request has been submitted successfully.....")

                elif choice == "G":
                    policies = current_user.__view_company_policies__()
                    print(policies)

                elif choice == "H":
                    schedules = current_user.__access_work_schedules__()
                    print(schedules)

                elif choice == "I":
                    print("Logging out...\n")
                    break

                elif choice == "J":
                    while True:
                        out = input("Do you want to exit?(yes / no): ").lower()
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
