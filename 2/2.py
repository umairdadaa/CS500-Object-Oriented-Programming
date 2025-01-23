import os

os.system("clear") 

def calculate_cd_value(investment, apy, months, frequency):
    """Calculate the CD value based on the compounding frequency."""
    if frequency == 'monthly':
        n = 12
    elif frequency == 'quarterly':
        n = 4
    elif frequency == 'annually':
        n = 1
    else:
        raise ValueError("Invalid compounding frequency")

    r = apy / 100
    cd_values = []
    
    for period in range(1, months + 1):
        time = period / 12
        value = investment * (1 + r / n) ** (n * time)
        cd_values.append((period, value))
    
    return cd_values

def print_cd_table(cd_values, frequency):
    """Print the CD value table."""
    if frequency == 'monthly':
        print(f"{'Month':<10}{'CD Value':<15}")
    else:
        print(f"{'Period':<10}{'CD Value':<15}")
    
    print('-' * 25)

    for period, value in cd_values:
        print(f"{period:<10}{value:,.2f}")

def main():
    # Get user inputs
    investment = float(input("Enter initial investment amount: "))
    apy = float(input("Enter annual percentage yield (APY): "))
    months = int(input("Enter number of months for the CD term: "))
    frequency = input("Enter compounding frequency (monthly, quarterly, annually): ").strip().lower()

    if months < 0:
        raise ValueError("Number of months must be a positive integer")
    elif apy < 0:
        raise ValueError("APY must be a positive number")
    elif investment < 0:
        raise ValueError("Initial investment amount must be a positive number")
    elif frequency not in ['monthly', 'quarterly', 'annually']:
        raise ValueError("Invalid compounding frequency")
    else:
        pass

    # Calculate CD values
    cd_values = calculate_cd_value(investment, apy, months, frequency)

    # Print the CD table
    print_cd_table(cd_values, frequency)

    # Calculate total interest earned
    final_value = cd_values[-1][1]
    total_interest = final_value - investment
    print(f"\nTotal interest earned: ${total_interest:,.2f}")

if __name__ == "__main__":
    main()
