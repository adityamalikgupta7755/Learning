num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print("Largest number is:", largest)

# This approach is easier to extend to N numbers.
# Works for any number of inputs if you use a list.