import random

def generate_list(count, min_val, max_val):
    """Генерация списка через функцию"""
    return [random.randint(min_val, max_val) for _ in range(count)]

# Пример использования
numbers = generate_list(14, 5, 400)
print(numbers)
