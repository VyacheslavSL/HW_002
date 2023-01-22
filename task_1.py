# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

#  Вариант человек против человека:

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"Ошибка! {name}, введите количество конфет от 1 до 28: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# sweets = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while sweets> 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         sweets -= k
#         flag = False
#         p_print(player1, k, counter1, sweets)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         sweets -= k
#         flag = True
#         p_print(player2, k, counter2, sweets)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
    
    # ======================================================================================================
    
# Вариант человек против бота:
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"Ошибка! {name}, введите количество конфет от 1 до 28: "))
#     return x

# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# sweets = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while sweets > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         sweets -= k
#         flag = False
#         p_print(player1, k, counter1, sweets)
#     else:
#         k = randint(1, 29)
#         counter2 += k
#         sweets -= k
#         flag = True
#         p_print(player2, k, counter2, sweets)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
    # ==========================================================================================================

# Вариант человек против бота c "интеллектом":
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"Ошибка! {name}, введите количество конфет от 1 до 28: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def bot_calc(value):
    k = randint(1, 29)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k


player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
sweets = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while sweets > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        sweets -= k
        flag = False
        p_print(player1, k, counter1, sweets)
    else:
        k = bot_calc(sweets)
        counter2 += k
        sweets -= k
        flag = True
        p_print(player2, k, counter2, sweets)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")