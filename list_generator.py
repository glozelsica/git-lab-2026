import random

# Поэлементное заполнение списка
count = 14
min_val = 5
max_val = 400
numbers = []

print("Генерация списка случайных чисел:")
for i in range(count):
    numbers.append(random.randint(min_val, max_val))
    print(f"  Элемент {i+1}: {numbers[-1]}")

print(f"\nИтоговый список из {count} элементов:")
print(numbers)
print(f"Минимальное значение в списке: {min(numbers)}")
print(f"Максимальное значение в списке: {max(numbers)}")
