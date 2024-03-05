import math
list = [num for num in range(51) ]
even = [even for even in list if even % 2 == 0] 
odd = [odd for odd in list if odd % 2 != 0]
even_sum = sum(even)
print ("Sum of even num: ", even_sum)

prod = math.prod(odd)
print ("Product of odd numbers: ", prod)


#the largest num
list1 = [num for num in range(51) ]
list1.sort()
print ("Largest element is: ", list1[-1])


