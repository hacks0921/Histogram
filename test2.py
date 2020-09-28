a = list(range(5,11))
print(a)
b = [value for index, value in enumerate(a) if value == 9]
c = [index for index, value in enumerate(a) if value == 9]
print(b)
print(c)


# index = [i for i, value in enumerate(mask) if value == True]
