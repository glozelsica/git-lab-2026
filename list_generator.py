import random

<<<<<<< HEAD
# ВАРИАНТ 1: Функциональный подход
def generate_list(count, min_val, max_val):
    """Генерация списка через функцию"""
    print("Начинаем генерацию списка через функцию...")
    result = [random.randint(min_val, max_val) for _ in range(count)]
    print(f"Сгенерировано {count} элементов")
    return result

# ВАРИАНТ 2: Циклический подход
def generate_list_loop(count, min_val, max_val):
    """Генерация списка через цикл"""
    result = []
    print("=" * 40)
    print("ГЕНЕРАТОР СПИСКА ЧИСЕЛ (ЧЕРЕЗ ЦИКЛ)")
    print("=" * 40)
    
    for i in range(count):
        result.append(random.randint(min_val, max_val))
        print(f"  Элемент {i+1:2d}: {result[-1]:3d}")
    
    print("=" * 40)
    print(f"ИТОГО: {count} элементов")
    print(f"Список: {result}")
    print(f"Мин: {min(result)}, Макс: {max(result)}")
    print("=" * 40)
    return result

# Параметры
count = 14
min_val = 5
max_val = 400

# Тестируем оба подхода
print("\n" + "=" * 50)
print("ТЕСТИРУЕМ ФУНКЦИОНАЛЬНЫЙ ПОДХОД")
print("=" * 50)
numbers1 = generate_list(count, min_val, max_val)
print(f"Результат: {numbers1}")

print("\n" + "=" * 50)
print("ТЕСТИРУЕМ ЦИКЛИЧЕСКИЙ ПОДХОД")
print("=" * 50)
numbers2 = generate_list_loop(count, min_val, max_val)

print("\n" + "=" * 50)
print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ")
print("=" * 50)
print(f"Длина списка (функция): {len(numbers1)}")
print(f"Длина списка (цикл): {len(numbers2)}")
print(f"Списки {'совпадают' if numbers1 == numbers2 else 'различаются'}")

=======
def generate_list(count, min_val, max_val):
    """Генерация списка через функцию"""
    return [random.randint(min_val, max_val) for _ in range(count)]

# Пример использования
numbers = generate_list(14, 5, 400)
print(numbers)
>>>>>>> parent of 04dc6ad (,Добавление кода 2)
