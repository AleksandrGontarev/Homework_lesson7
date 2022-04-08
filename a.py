my_str = "lonyyyyyyggo"
l_limit = "o"
r_limit = "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index:r_index]
print(sub_str)