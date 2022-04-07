my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
my_list = []
for symbol in set(my_str_1).intersection(my_str_2):
    if (my_str_1 + my_str_2).count(symbol) == 2:
        my_list.append(symbol)
if my_list:
    print(my_list)
else:
    print("повторяющихся символов нет")



