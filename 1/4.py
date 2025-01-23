import os

os.system("clear")

print("Welcome to the Movie Ticket System!\n")

# Ticket prices
adult_weekday_price = 12.50
adult_weekend_holiday_price = 15.00
child_weekday_price = 8.00
child_weekend_holiday_price = 10.00
senior_weekday_price = 9.00
senior_weekend_holiday_price = 11.50

# Get user input
while True:
    try:
        num_adult_tickets = int(input("Number of adult tickets: "))
        num_child_tickets = int(input("Number of child tickets: "))
        num_senior_tickets = int(input("Number of senior tickets: "))

        # Check if the number of tickets is non-negative
        if num_adult_tickets < 0 or num_child_tickets < 0 or num_senior_tickets < 0:
            print("Number of tickets cannot be negative. Please enter a valid number.")
            continue  # Skip to the next iteration of the loop
        
        # Exit the loop if inputs are valid
        break
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# accept integer input for the number of tickets
while True:
    day_type = input("Is the movie showing on a weekday (w), weekend (e), or holiday (h)? ").strip().lower()
    if day_type in ('w', 'e', 'h'):
        break
    else:
        print("Invalid input. Please enter 'w', 'e', or 'h'.")

# Determine ticket prices based on the day type
if day_type in ('e', 'h'):
    adult_price = adult_weekend_holiday_price
    child_price = child_weekend_holiday_price
    senior_price = senior_weekend_holiday_price
else:
    adult_price = adult_weekday_price
    child_price = child_weekday_price
    senior_price = senior_weekday_price

# Calculate subtotal
subtotal = (num_adult_tickets * adult_price) + (num_child_tickets * child_price) + (num_senior_tickets * senior_price)

# Calculate discount
total_tickets = num_adult_tickets + num_child_tickets + num_senior_tickets
discount_percentage = 0.10 if total_tickets >= 5 else 0
discount_amount = subtotal * discount_percentage
total_price = subtotal - discount_amount

# Print detailed receipt
os.system("clear")
print("\nMovie Ticket Receipt:")
print(f"\nAdult Tickets ({num_adult_tickets}): ${adult_price:.2f} each")
print(f"Child Tickets ({num_child_tickets}): ${child_price:.2f} each")
print(f"Senior Tickets ({num_senior_tickets}): ${senior_price:.2f} each")
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discount (5+ tickets): {int(discount_percentage * 100)}%")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"\nTotal: ${total_price:.2f}")
print("\nThank you for coming to the movies!\n\n")
