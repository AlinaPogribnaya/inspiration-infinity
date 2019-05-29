my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
my_string = my_string.split(';')
print(my_string[0], my_string[1], my_string[2], '                        ', "О студенте")

for i in range(5,11,5):
    print(my_string[i], my_string[i+1], my_string[i+2], ' '*(25-len(my_string[i])-len(my_string[i+1])-len(my_string[i+2])-2), my_string[i+4], ',', my_string[i+3])