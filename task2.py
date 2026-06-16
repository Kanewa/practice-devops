import math

def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел.")
 
    return math.factorial(n)


def get_number_from_user() -> int:
    while True:
        user_input = input("Введите положительное целое число: ").strip()
        
        if not user_input:
            print("Ошибка: ввод не может быть пустым. Попробуйте ещё раз.")
            continue
        try:
            number = int(user_input)
        except ValueError:
            print(f"Ошибка: '{user_input}' не является целым числом. Введите целое число.")
            continue
        if number <= 0:
            print(f"Ошибка: число должно быть положительным (больше нуля). Вы ввели: {number}.")
            continue
        
        return number


def main():
    print("=" * 50)
    print("  Программа вычисления факториала числа")
    print("=" * 50)
    print("Факториал числа N (обозначается N!) — это произведение")
    print("всех натуральных чисел от 1 до N включительно.")
    print("Например: 5! = 1 × 2 × 3 × 4 × 5 = 120")
    print("-" * 50)
    number = get_number_from_user()
    
    try:
        result = calculate_factorial(number)
        print("-" * 50)
        print(f"Результат: {number}! = {result}")
        if number > 20:
            print(f"(Число содержит {len(str(result))} цифр)")
            
    except ValueError as e:
        print(f"Ошибка вычисления: {e}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
