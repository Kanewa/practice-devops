import random

MIN_NUMBER = 1       
MAX_NUMBER = 100     
MAX_ATTEMPTS = 10    
HINT_THRESHOLD = 5   

def generate_number() -> int:
    return random.randint(MIN_NUMBER, MAX_NUMBER)

def get_range_hint(secret: int, attempt: int) -> str:
    if attempt <= HINT_THRESHOLD:
        return ""

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
    while True:
        hint_text = f"Попытка {attempt}/{MAX_ATTEMPTS} (осталось {remaining})"
        print(f"\n{hint_text}")
        user_input = input(f"Введите число от {MIN_NUMBER} до {MAX_NUMBER} (или 'выход' для выхода): ").strip().lower()
        
        if user_input in ("выход", "exit", "q", "quit"):
            return None
        
        if not user_input:
            print("⚠️  Ввод не может быть пустым. Попробуйте ещё раз.")
            continue
        
        try:
            number = int(user_input)
        except ValueError:
            print(f"⚠️  '{user_input}' — не целое число. Введите целое число от {MIN_NUMBER} до {MAX_NUMBER}.")
            continue
        
        if is_out_of_range(number):
            print(f"⚠️  Число должно быть в диапазоне от {MIN_NUMBER} до {MAX_NUMBER}.")
            continue
        
        return number

def is_out_of_range(number: int) -> bool:
    return number < MIN_NUMBER or number > MAX_NUMBER

def play_game() -> bool:
    secret = generate_number()
    attempt_counter = 0
    
    print("\n" + "🎮 " * 10)
    print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}.")
    print(f"У вас {MAX_ATTEMPTS} попыток. После {HINT_THRESHOLD}-й попытки — подсказка!")
    print("🎮 " * 10)
    
    while attempt_counter < MAX_ATTEMPTS:
        attempt_counter += 1
        remaining = MAX_ATTEMPTS - attempt_counter + 1
        
        guess = get_user_input(attempt_counter, remaining)
        
        if guess is None:
            print(f"\n👋 Выход из игры. Загаданное число было: {secret}.")
            return False
        
        if guess == secret:
            print(f"\n🎉 Поздравляю! Вы угадали число {secret}!")
            print(f"Это заняло {attempt_counter} {'попытку' if attempt_counter == 1 else 'попытки' if 2 <= attempt_counter <= 4 else 'попыток'}.")
            return True
        elif guess < secret:
            print("📉 Слишком маленькое! Загаданное число больше.")
        else:
            print("📈 Слишком большое! Загаданное число меньше.")
        
        hint = get_range_hint(secret, attempt_counter)
        if hint:
            print(hint)
        
        remaining_after = MAX_ATTEMPTS - attempt_counter
        if remaining_after == 2:
            print("⚠️  Осторожно! Осталось всего 2 попытки!")
        elif remaining_after == 1:
            print("🚨 Последняя попытка!")
    
    print(f"\n😞 Попытки закончились! Загаданное число было: {secret}.")
    return False

def ask_play_again() -> bool:
    while True:
        answer = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        elif answer in ("нет", "н", "no", "n"):
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

def main():
    print("=" * 55)
    print("       🎯 ИГРА 'УГАДАЙ ЧИСЛО' 🎯")
    print("=" * 55)
    print("Правила игры:")
    print(f"  • Компьютер загадывает число от {MIN_NUMBER} до {MAX_NUMBER}")
    print(f"  • У вас {MAX_ATTEMPTS} попыток, чтобы его угадать")
    print(f"  • После {HINT_THRESHOLD}-й попытки вы получите подсказку о диапазоне")
    print("  • После каждой попытки — подсказка 'больше' или 'меньше'")
    print("=" * 55)
    
    total_games = 0
    wins = 0
    
    while True:
        total_games += 1
        result = play_game()
        if result:
            wins += 1
        
        print(f"\n📊 Статистика: побед {wins} из {total_games} игр "
              f"({wins * 100 // total_games}%)")
        
        if not ask_play_again():
            break
    
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
    main()
