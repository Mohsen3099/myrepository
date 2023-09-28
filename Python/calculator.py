def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def exponentiation(x , y):
    return x ** y
def calculate():
    while True:
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("0. Exit")
       
        choice = input("Enter your choice (0-5): ")
       
        if choice == "0":
            print("Calculator is turned off. Goodbye!")
            break
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
       
        if choice == "1":
            print(f"\n{num1} + {num2} = {add(num1, num2)}\n")
        elif choice == "2":
            print(f"\n{num1} - {num2} = {subtract(num1, num2)}\n")
        elif choice == "3":
            print(f"\n{num1} * {num2} = {multiply(num1, num2)}\n")
        elif choice == "4":
            print(f"\n{num1} / {num2} = {divide(num1, num2)}\n")
        elif choice == "5":
            print(f"\n{num1} ^ {num2} = {exponentiation(num1, num2)}\n")
        else:
            print("Invalid input. Please try again.")
calculate()
