# Count Vowels
# ✅ Problem Statement

# Take a string input and count how many vowels (a, e, i, o, u) are inside it.


# Take input from user
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Counter variable
count = 0

# Loop through each character
for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
