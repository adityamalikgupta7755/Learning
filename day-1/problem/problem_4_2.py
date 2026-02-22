# Using Loop

s = "aditya"
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

print(reversed_s)

# How it works:

# Iteration flow:
# char	reversed_s
# a	a
# d	da
# i	ida
# t	tida
# y	ytida
# a	aytida

# We keep adding the new character in front.

