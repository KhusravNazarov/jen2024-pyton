from add import addition
from dev import devision
from mult import multiply
from sub import subtraction
# import dev
# import mult
# import sub 



def calculate():
    char = input("Enter the operation (+, -, *, /): ")
    if char == '+':
        answer = addition()
    if char == '/':
        answer = dev()
    if char == '*':
        answer = multiply()
    if char == '-':
        answer = subtraction()
    return answer
    


print(calculate())