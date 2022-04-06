# 1. Дано целое число (int). Определить сколько нулей в этом числе.

int = 2000
rezult = str(int).count("0")
print(rezult)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

int = 2000300
my_str = ""
value = -1
while str(int)[value] in str(int) and str(int)[value] == "0":
    my_str += (str(int)[value])
    value -= 1
print(len(my_str))

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, 3, 4]
my_list_2 = [10, 20, 55, 88]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
symbol = my_list[0]
new_list = my_list.copy()[1:]
new_list.append(symbol)
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4]
id_start = id(my_list)
del_value = my_list[::-1].pop()
my_list[:] = my_list[1:]
my_list.append(del_value)
id_finish = id(my_list)
if id_start == id_finish:
    print('список не изменился')
else:
    print("я где-то накосячил")

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

my_str = "43 больше чем 34 но меньше чем 56"
my_list = []
rezult = 0
for symbol in my_str.split(" "):
    if symbol.isdigit():
        my_list.append(int(symbol))
for symbol_summ in my_list:
    rezult += symbol_summ
print(rezult)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "lonyyyyyygo"
l_limit = "o"
r_limit = "g"
list = []
sub_str = ""
for index,symbol in enumerate(my_str):
    if symbol == l_limit:
        index_l = index
        list.append(index_l)
for index,symbol in enumerate(my_str[::]):
    if symbol == r_limit:
        index_r = index
        list.append(index_r)
sub_str = my_str[list[0] + 1:list[-1]]
print(sub_str)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = "abcdefg"
my_list = []
index_1 = 0
index_2 = 2
if len(my_str) %2 != 0:
    my_str += "_"
for index in enumerate(my_str):
    if index_2 <= len(my_str):
        value = my_str[index_1:index_2]
        my_list.append(value)
        index_1 +=2
        index_2 +=2
print(my_list)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
my_list = [2,4,1,5,3,9,0,7]
index_c = 1
index_l = 0
index_r = 2
rezult = 0
for x,symbol in enumerate(my_list):
    if index_r < len(my_list):
        summ = my_list[index_l] + my_list[index_r]
        if my_list[index_c] > summ:
            rezult +=1
        index_c += 1
        index_l += 1
        index_r += 1
print("количество элементов выполняющих условие = ",rezult)

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1,2,3, "11", "22", "33"]
new_list = []
for symbol in my_list:
    if type(symbol) == str:
        new_list.append(symbol)
print(new_list)

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
my_str = "asdfgfffsrg"
my_list = []
for symbol in my_str:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "asdfgh1"
my_str_2 = "uiaajssshp21"
my_list = []
str_general = my_str_1 + my_str_2
for symbol in str_general:
    if str_general.count(symbol) >= 2:
        if symbol not in my_list:
            my_list.append(symbol)
if my_list:
    print(my_list)
else:
    print("повторяющихся символов нет")



