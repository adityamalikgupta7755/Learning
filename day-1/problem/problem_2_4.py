numbers = []
for i in range(3):
    numbers.append(float(input(f"Enter number {i+1}: ")))

largest = numbers[0]
for num in numbers[1:]:
    if num > largest:
        largest = num

print("Largest number is:", largest)

# Now you can easily change 3 to N numbers, and the program will still work.