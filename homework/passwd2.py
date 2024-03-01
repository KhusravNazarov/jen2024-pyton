import re 
flag = 0
passwd = input("Enter a strong password: ")
if not re.search('[a-z]', passwd) and re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[!@#$%^&*]', passwd) and len(passwd)<8:
    flag = 1
if (flag == 1):
    print("password is  invalid")
else :
    print("password is valid")
