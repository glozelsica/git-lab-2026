# Редактируем файл в generator-function
cat > list_generator.py << 'EOF'
import random

def generate_list(count, min_val, max_val):
    """Генерация списка через функцию (УЛУЧШЕННАЯ ВЕРСИЯ)"""
    print("Начинаем генерацию списка через функцию...")
    result = [random.randint(min_val, max_val) for _ in range(count)]
    print(f"Сгенерировано {count} элементов")
    return result

# Пример использования
count = 14
min_val = 5
max_val = 400
numbers = generate_list(count, min_val, max_val)
print(f"Итоговый список: {numbers}")
print(f"Минимум: {min(numbers)}, Максимум: {max(numbers)}")


