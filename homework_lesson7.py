########################################### 1
int = 2000
rezult = str(int).count("0")
print(rezult)
########################################### 2
int = 2000300
my_str = ""
value = -1
while str(int)[value] in str(int) and str(int)[value] == "0":
    my_str += (str(int)[value])
    value -= 1
print(len(my_str))
############################################ 3

my_list_1 = [1, 2, 3, 4]
my_list_2 = [10, 20, 55, 88]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)
############################################## 4
my_list = [1, 2, 3, 4]
symbol = my_list[0]
new_list = my_list.copy()[1:]
new_list.append(symbol)
print(new_list)
############################################ 5
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
############################################### 6
my_str = "43 больше чем 34 но меньше чем 56"
my_list = []
for symbol in my_str.split(" "):
    if symbol.isdigit():
        my_list.append(int(symbol))
print(sum(my_list))
############################################  7
my_str = "lonyyyyyygo"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]
print(sub_str)
########################################### 8
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
########################################### 9
my_list = [2,4,1,5,3,9,0,7]
index = 1
rezult = 0
for x,symbol in enumerate(my_list):
    if index + 1 < len(my_list):
        summ = my_list[index - 1] + my_list[index + 1]
        if my_list[index] > summ:
            rezult +=1
        index += 1
print("количество элементов выполняющих условие = ",rezult)
########################################## 10
my_list = [1,2,3, "11", "22", "33"]
new_list = []
for symbol in my_list:
    if type(symbol) == str:
        new_list.append(symbol)
print(new_list)
######################################### 11
my_str = "assfff"
my_list = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)
######################################### 12
my_str_1 = "asdfgh1"
my_str_2 = "uiaajssshp21"
my_list = []
my_list = set(my_str_1).intersection(set(my_str_2))
if my_list:
    print(my_list)
else:
    print("повторяющихся символов нет")
##########################################  13
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


