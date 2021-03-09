my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = []
for el in my_list:
    if my_list.count(el) == 1:
        new_list.append(el)
print(new_list)

print([el for el in my_list if my_list.count(el) == 1])
