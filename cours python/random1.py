import random

correctnum = random.randint(1,100)
print (correctnum)
gess =int(input("enter gess")) 
if gess == correctnum:
    print("your gess is correct")
elif gess > correctnum:
    print("your gess is too high")
elif gess < correctnum:
    print("your gess is too low")    
    
while gess != correctnum:
    gess =int(input("enter gess")) 
    if gess == correctnum:
        print("your gess is correct")
    elif gess > correctnum:
         print("your gess is too high")
    elif gess < correctnum:
         print("your gess is too low")    


        