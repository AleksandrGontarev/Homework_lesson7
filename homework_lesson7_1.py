# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
my_list = []
str_general = my_str_1 + my_str_2
for symbol in str_general:
    if str_general.count(symbol) == 2:
        if symbol not in my_list:
            my_list.append(symbol)
if my_list:
    print(my_list)
else:
    print("повторяющихся символов нет")