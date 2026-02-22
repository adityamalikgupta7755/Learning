# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Check largest number
if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)

else:
    print("Largest number is:", num3)

# 🔎 How It Works

# num1 >= num2 and num1 >= num3
# → Check if num1 is greater than or equal to both

# elif
# → If first condition fails, check second

# else
# → If both fail, then third number is largest

