import random

# Поэлементное заполнение списка (УЛУЧШЕННАЯ ВЕРСИЯ)
count = 14
min_val = 5
max_val = 400
numbers = []

print("=" * 40)
print("ГЕНЕРАТОР СПИСКА ЧИСЕЛ")
print("=" * 40)

for i in range(count):
    numbers.append(random.randint(min_val, max_val))
    print(f"  Элемент {i+1:2d}: {numbers[-1]:3d}")

print("=" * 40)
print(f"ИТОГО: {count} элементов")
print(f"Список: {numbers}")
print(f"Мин: {min(numbers)}, Макс: {max(numbers)}")
print("=" * 40)

