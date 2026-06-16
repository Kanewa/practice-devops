"""
Кейс-задача №4 — Игра "Угадай число"
Компьютер загадывает случайное число от 1 до 100, а пользователь
должен его угадать за ограниченное количество попыток.
Игра поддерживает подсказки, валидацию ввода и повторный запуск.
"""

import random


# Константы игры
MIN_NUMBER = 1         # Минимальное возможное число
MAX_NUMBER = 100      # Максимальное возможное число
MAX_ATTEMPTS = 10     # Максимальное количество попыток
HINT_THRESHOLD = 5   # После скольких попыток давать расширенную подсказку


def generate_number() -> int:
    """
    Генерирует случайное целое число в заданном диапазоне.
    
    Возвращает:
        int: Случайное число от MIN_NUMBER до MAX_NUMBER включительно.
    """
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_range_hint(secret: int, attempt: int) -> str:
    """
    Формирует расширенную подсказку о диапазоне, в котором находится число.
    Подсказка выдаётся после HINT_THRESHOLD попыток.
    
    Параметры:
        secret (int): Загаданное число.
        attempt (int): Номер текущей попытки (начиная с 1).
    
    Возвращает:
        str: Строка с подсказкой или пустая строка, если ещё рано.
    """
    if attempt <= HINT_THRESHOLD:
        return ""
    
    # Делим диапазон на четыре равных части и определяем, в какой из них число
    step = (MAX_NUMBER - MIN_NUMBER) // 4
    lower = MIN_NUMBER
    upper = MIN_NUMBER + step

    for _ in range(4):
        if lower <= secret <= upper:
            return f"💡 Подсказка: число находится в диапазоне от {lower} до {upper}."
        lower = upper + 1
        upper = min(lower + step - 1, MAX_NUMBER)

    return ""


def get_user_input(attempt: int, remaining: int) -> int | None:
    """
    Запрашивает у пользователя число с полной валидацией ввода.
    Возвращает None, если пользователь хочет выйти.
    
    Параметры:
        attempt (int): Номер текущей попытки.
        remaining (int): Количество оставшихся попыток.
    
    Возвращает:
        int | None: Введённое число или None при вводе 'выход'.
    """
    while True:
        hint_text = f"Попытка {attempt}/{MAX_ATTEMPTS} (осталось {remaining})"
        print(f"\n{hint_text}")
        user_input = input(f"Введите число от {MIN_NUMBER} до {MAX_NUMBER} (или 'выход' для выхода): ").strip().lower()
        
        # Проверка команды выхода
        if user_input in ("выход", "exit", "q", "quit"):
            return None
        
        # Проверка: ввод не пустой
        if not user_input:
            print("⚠️  Ввод не может быть пустым. Попробуйте ещё раз.")
            continue
        
        # Попытка преобразовать в число
        try:
            number = int(user_input)
        except ValueError:
            print(f"⚠️  '{user_input}' — не целое число. Введите целое число от {MIN_NUMBER} до {MAX_NUMBER}.")
            continue
        
        # Проверка диапазона
        if is_out_of_range(number):
            print(f"⚠️  Число должно быть в диапазоне от {MIN_NUMBER} до {MAX_NUMBER}.")
            continue
        
        return number


def is_out_of_range(number: int) -> bool:
    """
    Проверяет, выходит ли число за допустимый диапазон.
    
    Параметры:
        number (int): Проверяемое число.
    
    Возвращает:
        bool: True если число вне диапазона, False если в диапазоне.
    """
    return number < MIN_NUMBER or number > MAX_NUMBER


def play_game() -> bool:
    """
    Проводит одну партию игры "Угадай число".
    
    Возвращает:
        bool: True если игрок угадал число, False если проиграл или вышел.
    """
    # Загадываем число
    secret = generate_number()
    attempt_counter = 0
    
    print("\n" + "🎮 " * 10)
    print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}.")
    print(f"У вас {MAX_ATTEMPTS} попыток. После {HINT_THRESHOLD}-й попытки — подсказка!")
    print("🎮 " * 10)
    
    while attempt_counter < MAX_ATTEMPTS:
        attempt_counter += 1
        remaining = MAX_ATTEMPTS - attempt_counter + 1
        
        # Получаем ввод пользователя
        guess = get_user_input(attempt_counter, remaining)
        
        # Пользователь хочет выйти
        if guess is None:
            print(f"\n👋 Выход из игры. Загаданное число было: {secret}.")
            return False
        
        # Проверяем догадку
        if guess == secret:
            print(f"\n🎉 Поздравляю! Вы угадали число {secret}!")
            print(f"Это заняло {attempt_counter} {'попытку' if attempt_counter == 1 else 'попытки' if 2 <= attempt_counter <= 4 else 'попыток'}.")
            return True
        elif guess < secret:
            print("📉 Слишком маленькое! Загаданное число больше.")
        else:
            print("📈 Слишком большое! Загаданное число меньше.")
        
        # Выдаём расширенную подсказку после порогового количества попыток
        hint = get_range_hint(secret, attempt_counter)
        if hint:
            print(hint)
        
        # Предупреждение о последних попытках
        remaining_after = MAX_ATTEMPTS - attempt_counter
        if remaining_after == 2:
            print("⚠️  Осторожно! Осталось всего 2 попытки!")
        elif remaining_after == 1:
            print("🚨 Последняя попытка!")
    
    # Попытки закончились
    print(f"\n😞 Попытки закончились! Загаданное число было: {secret}.")
    return False


def ask_play_again() -> bool:
    """
    Спрашивает пользователя, хочет ли он сыграть ещё раз.
    
    Возвращает:
        bool: True если пользователь хочет сыграть снова.
    """
    while True:
        answer = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        elif answer in ("нет", "н", "no", "n"):
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")


def main():
    """
    Главная функция: управляет главным циклом игры, отображает
    общую статистику и приветствует/прощается с пользователем.
    """
    print("=" * 55)
    print("       🎯 ИГРА 'УГАДАЙ ЧИСЛО' 🎯")
    print("=" * 55)
    print("Правила игры:")
    print(f"  • Компьютер загадывает число от {MIN_NUMBER} до {MAX_NUMBER}")
    print(f"  • У вас {MAX_ATTEMPTS} попыток, чтобы его угадать")
    print(f"  • После {HINT_THRESHOLD}-й попытки вы получите подсказку о диапазоне")
    print("  • После каждой попытки — подсказка 'больше' или 'меньше'")
    print("=" * 55)
    
    # Статистика нескольких партий
    total_games = 0
    wins = 0
    
    while True:
        total_games += 1
        result = play_game()
        if result:
            wins += 1
        
        # Показываем текущую статистику
        print(f"\n📊 Статистика: побед {wins} из {total_games} игр "
              f"({wins * 100 // total_games}%)")
        
        # Предлагаем сыграть ещё раз
        if not ask_play_again():
            break
    
    # Итоговое сообщение
    print("\n" + "=" * 55)
    print(f"Итог: сыграно игр: {total_games}, побед: {wins}.")
    if total_games > 0:
        percentage = wins * 100 // total_games
        if percentage == 100:
            print("🏆 Превосходно! Вы выиграли все партии!")
        elif percentage >= 50:
            print("👍 Неплохо! Продолжайте практиковаться.")
        else:
            print("💪 Не расстраивайтесь, в следующий раз повезёт!")
    print("До свидания! 👋")
    print("=" * 55)


if __name__ == "__main__":
    # Точка входа в программу
    main()
