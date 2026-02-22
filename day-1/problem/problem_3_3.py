rules = {
    3: "Fizz",
    5: "Buzz",
    7: "Pop",
    11: "Boom"
}

for i in range(1, 101):
    result = ""

    for divisor, word in rules.items():
        if i % divisor == 0:
            result += f"{i}-{word}"

    print(result if result else i)