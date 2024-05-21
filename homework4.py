immutable_var = ([3], 4 , "строка", True)
print(immutable_var)
immutable_var [1][0] = 15 # элементы кортежа нельзя измить если только внутри кортежа они не взяты в список
print(immutable_var)
mutable_list = [25, 100, "левый", True]
mutable_list[0] = 50
mutable_list[1] = 200
mutable_list[2] = 300
mutable_list[3] = False
print(mutable_list)