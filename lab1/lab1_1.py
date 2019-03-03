print('Введите числа a, b, c')
a = int(input())
b = int(input())
c = int(input())
rez = 0
if a != c:
    rez = abs(1 - a * b ** c - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a))
    print(rez)
else:
    print('Деление на ноль недопустимо. Пожалуйста измените числа')