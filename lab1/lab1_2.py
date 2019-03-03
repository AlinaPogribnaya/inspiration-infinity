from random import random
a = round(random() * 100)
print("Компьютер загадал число. Отгадайте его")
b = int
while b!=a:
    b = int(input())
    if b > a:
        print('Много')
    elif b < a:
        print('Мало')
    if b==a:
        print('Вы угадали')
