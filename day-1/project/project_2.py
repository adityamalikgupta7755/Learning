print("Simple CLI Calculator")
print("----------------------")

# Ask operation
operation = input("Choose operation (+, -, *, /): ")

if operation not in ["+", "-", "*", "/"]:
    print("Invalid operation selected!")
    exit()

# Get numbers safely
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid number entered!")
    exit()

# Calculation
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

print("Result:", result)