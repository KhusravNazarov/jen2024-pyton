name = input('What is your name: ')
greating = f'Hello {name}'
print(greating)
chouse = str(input('Chouse the expression type: "C to F" or "F to C" ' ))
if chouse ==  "F to C":
    inp1 = int(input("Temperature in fahrengate: "))
    exp = float((inp1 -32)*5/9)
    Cellsius = (exp )
    print ("The tempereature is", Cellsius, "Celsius")
elif chouse == "C to F": 
    inp2 = int(input("Temperature in Cellsius: "))
    exp2 = float((inp2 * 9/5)+32)
    Fahr = (exp2)
    print ("The tempereature is", Fahr, "Fahrengate")
else:
    print("Not walid opthion!")
     
     

    



