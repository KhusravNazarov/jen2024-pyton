# List of values 
# -mutable 
# -Any data




# lst = [1, 3, 53, 54, 8.4]
# lst.append(90)
# lst[2] = "john"
# print(lst)
#support indexing



# >>Tuples<<
# defined with value, or (value,)
# # -immutable
# # -read only
# -not support assignment
# tpl = (1, 3, 53, 54, 8.4)
#support indexing


#Dictionary
#Key value pair also defined with {}
#it does not have index
#can hold multiple data types 
#mutable

# person = {
#     "name" : "john",
#     "lastname" : "Bob",
#     "ssn" : "23435424",
#     "phone": ["123-434-534","123-433-545"]

# }
# print (person["name"])


#The dictionary of my favorite movie
# movies = [
#     {"title": "forrest gump", 
#     "year": "1994", 
#     "director": "robbert",
#     "actors": ["Tom", "crus"],
#     },
    
#     ]

# print(movies[0]["year"])



#Sets
#{} --->value1 , value2
#sorts values
#no acces to elements
#doesn't support index

st_a = {1,1,3,3,5, "Hello"}
st_b = {5,6,6,7}
union_st = st_a | st_b
union_st = st_a & st_b

print(union_st)
#for num in st:
   