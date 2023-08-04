from collections import defaultdict

# Create a defaultdict with int as the default value type
number_counts = defaultdict(int)
# number_counts = {}

numbers = [1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 1]

# Count the occurrences of each number
for num in numbers:
    number_counts[num] += 1

print(number_counts)
