import random

def gallows():
    words = ["Крематорий", "Аэропорт", "Кристал", "Генератор", "Декораторы", "Полиморфизм", "Формальдегид"]

    secret_word = random.choice(words).lower()

    guessed_letters = set()
    attempts = 7

    while attempts > 0:
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        if display == secret_word:
            print("Поздравляю! Вы угадали слово", secret_word)
            break

        print("Осталось попыток:", attempts)

        guess = yield

        if guess in guessed_letters:
            print("Вы уже угадали эту букву. Попробуйте еще раз.")
        elif guess in secret_word:
            guessed_letters.add(guess)
        else:
            attempts -= 1
            print(f"Неправильно. Буквы {guess} нет в слове.")
            if attempts == 0:
                print("Игра окончена. Вы не угадали слово", secret_word)

game = gallows()

print("Добро пожаловать в игру 'ВИСИЛИЦА'")
print("Компьютер загадал слово. Попробуйте угадать его, вводя по одной букве.")

next(game)

while True:
    user_input = input("Введите букву: ").lower()
    if len(user_input) != 1 or not user_input.isalpha():
        print("Ошибка! Введите одну букву.")
        continue

    game.send(user_input)
