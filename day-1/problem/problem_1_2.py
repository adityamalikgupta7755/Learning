def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"{number} is {check_even_odd(number)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")