#Asks the user to input two numbers and convert these inputs from strings to floats.
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
#Asks the user to choose an operation (+, -, *, /)
operation = input("Choose an operation (+, -, *, /):")
# Performs the chosen operation on the two numbers.
if operation == "+":
    results = num1 + num2
    print(f"{num1} + {num2} = {results}")
elif operation == "-":
    results  = num1 - num2
    print(f"{num1} - {num2} = {results}")
elif operation == "*":
    results  = num1 * num2
    print(f"{num1} * {num2} = {results}")
elif operation == "/":
    #Basic input handling for division by zero
    if num2 != 0:
        results  = num1 / num2
        print(f"{num1} / {num2} = {results}")
    else:
        print("Error: Division by 0 is not allowed.")
else: print("Error: Unsuported operation symbol entered.")
