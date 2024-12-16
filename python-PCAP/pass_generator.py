import random
small = []
cap = []
for i in range(97, 123):  # ASCII values for 'a' to 'z' are 97 to 122
    small.append(chr(i))
    cap.append(chr(i).upper())
numb = []
for n in range(10):
    numb.append(str(n))
special_characters = ['~', '@', '#','$', '%','^', '&','*', '(',')', '_', '+']



user_input = input(''' -- Password generator -- 
Choose option:
1: generate password
2: exit the program
Your choice: ''')
res_yes = [ 'YES', 'Yes', 'yes', 'y', 'Y']
res_no = [ 'NO', 'No', 'no', 'n', 'N']

while user_input != '1' and user_input != '2':
    print(' invalid input! ')
    user_input = input(''' -- Password generator -- 
Choose option:
1: generate password
2: exit the program
Your choice: ''')

if user_input == '1':
    pass_length = int(input( ' Provide password length: '))
    uppercase = input(' Use uppercase letters? (y/n) ')
    while uppercase not in res_yes and uppercase not in res_no:
        print(' invalid input! ')
        uppercase = input(' Use uppercase letters? (y/n) ')

    if uppercase in res_yes:
        small = small + cap
    digits = input(' Use digits? (y/n) ')
    while digits not in res_yes and digits not in res_no:
        
        print(' invalid input! ')
        digits = input(' Use digits? (y/n) ')

    if digits in res_yes:
        small = small + numb
    special = input(' Use special characters? (y/n) ')
    while special not in res_yes and special not in res_no:
        print(' invalid input! ')
        special = input(' Use special characters? (y/n) ')
        
    if special in res_yes:
        small = small + special_characters
    random_elements = ''.join(random.choices(small, k=pass_length))
    print(random_elements)
    
    
if user_input == '2':
    print('Bye!')

