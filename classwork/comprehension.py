lst = []

for num in range(20):
    lst.append(num)
print(lst)



lst = [num for num in range(10)] ### [value | for loop]
print(lst)


lst = [num for num in range(10) if num == (1,4)]
print (lst) 


# 1 : 1
# 2 : 4
# 3 : 9
# d = {i : i ** 2 for i in range(1,5)}