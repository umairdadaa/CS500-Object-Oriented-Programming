def get_digit(letter):
    # Define the code-breaking key using lists
    set1 = ['A', 'D', 'G', 'J', 'M']
    set2 = ['E', 'F', 'T', 'U', 'V']
    set3 = ['B', 'E', 'K', 'L', 'O']
    set4 = ['H', 'S', 'W', 'X', 'Y']
    set5 = ['C', 'F', 'N', 'P', 'Q']
    set6 = ['I', 'Y', 'Z']
    set7 = ['H', 'I', 'R', 'S', 'T']
    set8 = ['Z']

    # Check the corresponding digit for the input letter
    if letter in set8:
        return 8
    elif letter in set7:
        return 7
    elif letter in set6:
        return 6
    elif letter in set5:
        return 5
    elif letter in set4:
        return 4
    elif letter in set3:
        return 3
    elif letter in set2:
        return 2
    elif letter in set1:
        return 1
    else:
        return None  # No matching digit exists

def main():
    # Prompt the user for a letter
    letter = input("Enter a letter to decipher: ").upper()

    # Echo the letter back to the user
    print(f"You entered: {letter}")

    # Get the corresponding digit
    digit = get_digit(letter)

    # Output the result
    if digit is not None:
        print(f"The corresponding digit is {digit}.")
    else:
        print("No matching digit exists for this character.")

# Run the program
if __name__ == "__main__":
    main()
