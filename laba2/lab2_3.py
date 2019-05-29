import re;
my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса"
my_string = my_string.split(';')
print(my_string)
for i in range (len(my_string)):
    if my_string[i].startswith('_А'):
          print(my_string[i], my_string[i+1], my_string[i+2])

for i in range (len(my_string)):
    if my_string[i].startswith('_Б'):
          print(my_string[i], my_string[i+1], my_string[i+2])
