
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program
while True:
    print("Options")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mult' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'end' to end the program")

    user_input = input(": ")

    if user_input == "end":
        break
    elif user_input in ("add", "sub", "mult", "div"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "sub":
            print("Result:", subtract(num1, num2))
        elif user_input == "mult":
            print("Result:", multiply(num1, num2))
        elif user_input == "div":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
