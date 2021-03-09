def odd_nums_gen (n):
    for num in range(1, n+1, 2):
        yield num

number = 45
print(type(odd_nums_gen(number)))
for el in  odd_nums_gen(number):
    print(el)
