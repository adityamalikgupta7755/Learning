# Using Loop


s = "aditya"
reversed_s = ""

for i in range(len(s)-1, -1, -1):
    print("i", i)
    reversed_s += s[i]

print(reversed_s)


# 🔎 Explanation:

# range(start, stop, step)
# start = len(s)-1
# stop = -1 (exclusive)
# step = -1 (go backward)

# ⚡ Which One Should You Use?
# Method	Speed	Clean Code	Interview Value
# Slicing	Fast	✅ Very clean	Medium
# Loop	Slightly slower	Manual	⭐ High

# For real projects → use slicing
# For interviews → know both
