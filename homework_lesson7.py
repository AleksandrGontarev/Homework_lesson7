# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# int = 2000
# rezult = str(int).count("0")
# print(rezult)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# int = 2000300
# my_str = ""
# value = -1
# while str(int)[value] in str(int) and str(int)[value] == "0":
#     my_str += (str(int)[value])
#     value -= 1
# print(len(my_str))

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list_1 = [1, 2, 3, 4]
# my_list_2 = [10, 20, 55, 88]
# my_result = my_list_1[::2] + my_list_2[1::2]
# print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1, 2, 3, 4]
# symbol = my_list[0]
# new_list = my_list.copy()[1:]
# new_list.append(symbol)
# print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4]
# id_start = id(my_list)
# del_value = my_list[::-1].pop()
# my_list[:] = my_list[1:]
# my_list.append(del_value)
# id_finish = id(my_list)
# if id_start == id_finish:
#     print('список не изменился')
# else:
#     print("я где-то накосячил")

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

# my_str = "43 больше чем 34 но меньше чем 56"
# my_list = []
# rezult = 0
# for symbol in my_str.split(" "):
#     if symbol.isdigit():
#         my_list.append(int(symbol))
# for symbol_summ in my_list:
#     rezult += symbol_summ
# print(rezult)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".







