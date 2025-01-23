import os

os.system("clear")

# Get user input
input_string = input("Enter a string: ")

# Remove spaces and convert to lowercase for comparison
input_string = ''.join(char.lower() for char in input_string if char.isalnum())

# Initialize variables
length = len(input_string)
is_palindrome = True

# Compare characters from start and end
for i in range(length // 2):
    if input_string[i] != input_string[length - 1 - i]:
        is_palindrome = False
        break

# Output the result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
