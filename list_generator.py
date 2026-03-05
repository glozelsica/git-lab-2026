import random

# Поэлементное заполнение списка
count = 14
min_val = 5
max_val = 400
numbers = []

for i in range(count):
    numbers.append(random.randint(min_val, max_val))

print(numbers)
# This is a comment
