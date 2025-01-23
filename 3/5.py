def main():
    employees = []  # List to store employee information

    while True:
        print("\nMenu:")
        print("1 - Enter a new employee's information")
        print("2 - Display all employees’ information")
        print("3 - Find employees’ information by name")
        print("4 - Display all employees' information in chronological order by age")
        print("5 - Remove the employee by ID")
        print("6 - Quit")

        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            name = input("Enter employee's name: ")
            emp_id = input("Enter employee's ID: ")
            dept_number = input("Enter department number: ")
            age = int(input("Enter employee's age: "))
            employees.append([name, emp_id, dept_number, age])
            print(f"Employee {name} added successfully.")

        elif choice == '2':
            if not employees:
                print("No employee information available.")
            else:
                print("\nAll Employees' Information:")
                for emp in employees:
                    print(f"Name: {emp[0]}, ID: {emp[1]}, Department: {emp[2]}, Age: {emp[3]}")

        elif choice == '3':
            name = input("Enter the employee's name to search: ")
            found_employees = [emp for emp in employees if emp[0].lower() == name.lower()]
            if found_employees:
                print("\nFound Employees:")
                for emp in found_employees:
                    print(f"Name: {emp[0]}, ID: {emp[1]}, Department: {emp[2]}, Age: {emp[3]}")
            else:
                print("No employee found with that name.")
                add_option = input("Would you like to add this employee? (y/n): ")
                if add_option.lower() == 'y':
                    emp_id = input("Enter employee's ID: ")
                    dept_number = input("Enter department number: ")
                    age = int(input("Enter employee's age: "))
                    employees.append([name, emp_id, dept_number, age])
                    print(f"Employee {name} added successfully.")

        elif choice == '4':
            if not employees:
                print("No employee information available.")
            else:
                # Simple selection sort implementation based on age
                sorted_employees = employees[:]
                for i in range(len(sorted_employees)):
                    min_index = i
                    for j in range(i + 1, len(sorted_employees)):
                        if sorted_employees[j][3] < sorted_employees[min_index][3]:  # Compare ages
                            min_index = j
                    # Swap the found minimum element with the first element
                    sorted_employees[i], sorted_employees[min_index] = sorted_employees[min_index], sorted_employees[i]

                print("\nEmployees Sorted by Age:")
                for emp in sorted_employees:
                    print(f"Name: {emp[0]}, ID: {emp[1]}, Department: {emp[2]}, Age: {emp[3]}")

        elif choice == '5':
            emp_id = input("Enter the employee's ID to remove: ")
            for emp in employees:
                if emp[1] == emp_id:
                    employees.remove(emp)
                    print(f"Employee with ID {emp_id} has been removed.")
                    break
            else:
                print("No employee found with that ID.")

        elif choice == '6':
            exit_option = input("Are you sure you want to quit? (y/n): ")
            if exit_option.lower() == 'y':
                print("Exiting the program. Goodbye!")
                break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
