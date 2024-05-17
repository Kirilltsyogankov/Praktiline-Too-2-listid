from random import randint, choice
from os import replace
from string import ascii_lowercase
from time import sleep

# 1
try:
    nimekirja = []
    N = int(input("Введите длину списка чисел: "))
    for i in range(N):
        arv = randint(10, 100)
        nimekirja.append(arv)
    maksimum = max(nimekirja)  
    for i in range(len(nimekirja)):
        if nimekirja[i] == maksimum:
            nimekirja[i] = "useless_number"  
    print("Исходный список: " + str(nimekirja))   
except ValueError:
    print("Пожалуйста, введите корректное число")

# 7
try:
    sort_order = input("Хотите отсортировать по убыванию (к) или возрастанию (в)?").lower()
    if sort_order not in ['к', 'в']:
        raise ValueError("Неверный ввод. Введите 'к' или 'в'.")
    numbers = sorted([randint(-100, 100) for _ in range(6)], key=abs, reverse=sort_order == "к")
    print("Отсортированный список: ")
    print(*numbers, sep="\n")
except ValueError as e:
    print("Ошибка: ", e)

# 8
lists = [
   ['крот', 'белка', 'выхухоль'],
   ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],
   ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
]
try:
    max_length = 0
    for sublist in lists:
        for string in sublist:
            if len(string) > max_length:
                max_length = len(string)
    for sublist in lists:
        for i in range(len(sublist)):
            sublist[i] = sublist[i].ljust(max_length, '_')
    for sublist in lists:
        print(sublist)
except Exception as e:
    print("Ошибка: ", e)

# 9
try:
    name = input("Введите ваше имя: ")
    if not name.isalpha():
        raise ValueError("Имя должно содержать только буквы")
    print("Привет,", name.capitalize())
    total_letters = len(name)
    vowels = sum(1 for letter in name if letter.lower() in 'aeiouаеёиоуыэюя')
    consonants = total_letters - vowels
    print("Количество букв в имени: ", total_letters)
    print("Количество гласных: ", vowels)
    print("Количество согласных: ", consonants)
    print("Буквы в имени в алфавитном порядке: ", *sorted(set(name.lower())))
except ValueError as e:
    print("Ошибка:", e)
except Exception as e:
    print("Ошибка: ", e)

# 12
try:
    numbers = [randint(1, 100) for i in range(10)]
    print("Исходный список: ", numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    min_index = numbers.index(min_number)
    max_index = numbers.index(max_number)
    numbers[min_index], numbers[max_index] = max_number, min_number
    print("Список после замены минимального и максимального элементов: ", numbers)
except Exception as e:
    print("Ошибка: ", e)

# 16
try:
    vastused = ["Да, конечно!", "Да!", "Возможно!", "Нет!"]
    print("Добро пожаловать в игру вопросов и ответов!")
    while True:
        kysimus = input("Задайте вопрос да/нет (для выхода напишите 'выход'): ")
        if kysimus.lower() == "выход":
            print("Спасибо за игру! До свидания!")
            break
        elif kysimus.endswith("?"):
            vastus = choice(vastused)
            print("Ответ: ", vastus)
        else:
            print("Это не кажется вопросом да/нет. Пожалуйста, задайте вопрос да/нет.")
except Exception as e:
    print("Ошибка: ", e)
