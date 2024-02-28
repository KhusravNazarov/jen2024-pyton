test_string = str(input("Please enter a string for the variable chars: "))
print("The original string is: " + test_string)
first_part, second_part = test_string[:len(test_string)//2], test_string[len(test_string)//2:]
Word = str(input("Please enter a word to insert into the middle of chars: ")) 
Result = f'{first_part}{Word}{second_part}'
print(Result)