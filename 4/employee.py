# Employee class definition
class Employee:
    def __init__(self, name: str, emp_id: int, dept_num: int, age: int) -> None:
        self.__name = name
        self.__id = emp_id
        self.__dept_num = dept_num
        self.__age = age

    def __str__(self) -> str:
        return f"Name: {self.__name}, ID: {self.__id}, Department: {self.__dept_num}, Age: {self.__age}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def id(self) -> int:
        return self.__id

    @property
    def department(self) -> int:
        return self.__dept_num

    @property
    def age(self) -> int:
        return self.__age


# Company class definition
class Company:
    def __init__(self) -> None:
        self.__employees = []

    def add_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)

    def show_employees(self) -> None:
        if not self.__employees:
            print("No employees available.")
            return
        for emp in self.__employees:
            print(emp)

    def search_employee(self, name: str) -> Employee:
        for emp in self.__employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

def main():
    print("\nEmployee Management System")

    company = Company()

    while True:
        print("\nOptions Menu:")
        print("e - Enter a new employee's information")
        print("a - Display all employees information")
        print("d - Display an employee's information")
        print("q - Quit")

        choice = input("\nChoose an option: ").lower()

        if choice == 'e':
            name = input("Enter employee's name: ")
            emp_id = int(input("Enter employee ID: "))
            dept_num = int(input("Enter department number: "))
            age = int(input("Enter employee's age: "))

            new_employee = Employee(name, emp_id, dept_num, age)
            company.add_employee(new_employee)
            print("Employee added successfully.")

        elif choice == 'a':
            print("\nAll Employees:")
            company.show_employees()

        elif choice == 'd':
            name = input("Enter the employee's name to display their information: ")
            employee = company.search_employee(name)

            if employee:
                print("\nEmployee Details:")
                print(employee)
            else:
                print("Employee not found. Would you like to add this employee? (yes/no)")
                if input().lower() == 'yes':
                    emp_id = int(input("Enter the employee ID: "))
                    dept_num = int(input("Enter the department number: "))
                    age = int(input("Enter the employee's age: "))
                    new_emp = Employee(name, emp_id, dept_num, age)
                    company.add_employee(new_emp)
                    print("Employee added successfully.")

        elif choice == 'q':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
