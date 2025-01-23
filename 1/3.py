import os

os.system("clear")

# Constants
BASE_RATE = 14.50
REGULAR_HOURS = 40
OVERTIME_1_RATE = BASE_RATE * 1.5
OVERTIME_2_RATE = BASE_RATE * 2
TAX_RATE = 28

print("Welcome to the Payroll System!")

while True:
    # Prompt the user for hours worked
    try:
        hours_worked = float(input("\nEnter the number of hours worked: "))
        if hours_worked < 0:
            print("Hours worked cannot be negative. Please enter a valid number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        continue

    # Initialize pay variables
    regular_pay = 0
    overtime_1_pay = 0
    overtime_2_pay = 0

    # Calculate regular pay and overtime pay
    if hours_worked > REGULAR_HOURS:
        regular_pay = REGULAR_HOURS * BASE_RATE
        overtime_hours = hours_worked - REGULAR_HOURS
        if overtime_hours > 5:
            overtime_1_hours = 5
            overtime_2_hours = overtime_hours - 5
        else:
            overtime_1_hours = overtime_hours
            overtime_2_hours = 0
        overtime_1_pay = overtime_1_hours * OVERTIME_1_RATE
        overtime_2_pay = overtime_2_hours * OVERTIME_2_RATE
    else:
        regular_pay = hours_worked * BASE_RATE

    # Calculate gross pay, taxes withheld, and net pay
    gross_pay = regular_pay + overtime_1_pay + overtime_2_pay
    taxes_withheld = gross_pay * TAX_RATE / 100
    net_pay = gross_pay - taxes_withheld

    # Display the pay summary
    print("\n**Employee Pay Summary**")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Taxes Withheld (28%): ${taxes_withheld:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

    # Ask if there's another employee
    another_employee = input("\nDo you have another employee (yes/no)? ").strip().lower()
    if another_employee != 'yes':
        print("Thank you for using the payroll system. Goodbye!")
        break
