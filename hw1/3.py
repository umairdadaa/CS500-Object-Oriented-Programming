import random

def roll_dice():
    """Simulate a dice roll and return a random result"""
    # Ensure random behavior by not setting a seed, and generate a random number between 1 and 6
    return random.randint(1, 6)

def view_total_rolls():
    """Display the total number of rolls"""
    print(f"Total rolls made: {total_rolls}")

def view_roll_statistics():
    """Display statistics of the dice rolls"""
    print("Roll statistics:")
    for i in range(6):
        count = roll_counts[i]
        percentage = (count / total_rolls * 100) if total_rolls > 0 else 0
        print(f"Number {i + 1}: Rolled {count} times ({percentage:.2f}%)")
    print(f"Explosions: {explosion_count} triggered by rolling {explosion_trigger}!")

def menu():
    """Display the menu options"""
    print("\nMenu:")
    print("1. Roll Dice")
    print("2. View Total Rolls")
    print("3. View Roll Statistics")
    print("4. Exit")

def main():
    global total_rolls, explosion_count

    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Roll the dice
            roll = roll_dice()
            total_rolls += 1
            roll_counts[roll - 1] += 1  # Increment the count for the rolled number
            print(f"You rolled a {roll}!")
            
            # Check for explosion
            if roll == explosion_trigger:
                print("The die explodes!")
                explosion_count += 1
                print("(Rolling again for explosion...)")
                roll = roll_dice()  # Roll again due to explosion
                total_rolls += 1
                roll_counts[roll - 1] += 1
                print(f"You rolled a {roll}!")
                
        elif choice == "2":
            view_total_rolls()
            
        elif choice == "3":
            view_roll_statistics()
            
        elif choice == "4":
            print("Thanks for playing!")
            break
            
        else:
            print("Invalid choice, please enter 1, 2, 3, or 4.")

# Initialize counters for each possible die roll and total rolls
roll_counts = [0] * 6  # To store counts for 1-6
total_rolls = 0
explosion_trigger = 6  # Number 6 is the trigger for explosion
explosion_count = 0

# Run the program
if __name__ == "__main__":
    main()

