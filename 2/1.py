def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    method = input("Enter the method + - / *: ")

    if method == "+":
        print("The result is: ", a+b)
    elif method == "-":
        print("The result is: ", a-b)
    elif method == "/":
        if b == 0:
            print("Invalid operation")
        else:
            print("The result is: ", a/b)
    elif method == "*":
        print("The result is: ", a*b)
    else:
        print("Invalid method")

if __name__ == "__main__":
    main()