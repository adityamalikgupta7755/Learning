text = input("Enter a string: ")
count = sum(1 for char in text if char.lower() in "aeiou")
print("Number of vowels:", count)


# Extra Challenge (For You)
# Count each vowel separately (how many a, e, i, o, u)
# Ignore spaces and numbers.
# Make it case-insensitive.