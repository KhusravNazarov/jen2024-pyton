import re
#import librery (re)
flag = 0
passwd = input("enter the password: ") #get the input as variable 
if not re.search('[a-z]', passwd) : #Check if (passwd) contain needed characters
    flag = 1 
    print ("Lovercase letters required")
if not re.search('[0-9]', passwd):
    flag = 1
    print ("Numbers required")
if not re.search('[A-Z]', passwd):
    flag = 1
    print ("Capital letters required")
if not re.search('[!@#$%^&*]', passwd):
    flag = 1
    print ("Symbols required")
if len(passwd)<8:
    flag = 1
    print ("8 or more characters required")
if (flag == 0):
    print ("Password  is valid")
else:
    print("password is  invalid")
