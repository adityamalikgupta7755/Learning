print("Simple CLI Calculator")
print("----------------------")

# Ask user for operation
operation = input("Choose operation (+, -, *, /): ")

# Ask for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        exit()
    result = num1 / num2
else:
    print("Invalid operation!")
    exit()

print("Result:", result)