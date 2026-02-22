def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    user_input = input("Enter a number: ")
    number = int(user_input)

    result = check_even_odd(number)
    print(f"{number} is {result}")