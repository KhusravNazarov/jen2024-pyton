def sum_list(list_num):
    sum = 0 
    for n in list_num:
        sum = sum + n
        
    return(sum)
    

list_num = [   
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]
print(sum_list(list_num))