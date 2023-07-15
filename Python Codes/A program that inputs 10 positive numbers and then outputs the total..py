#a program code that inputs 10 positive numbers and then outputs the total
total = 0
counter = 0
num = 0
num = int(input("enter a positive number"))
if num > 0:
    while counter != 10:
        num = int(input("enter  positive number"))
        total = total + num
        counter = counter + 1
else:
    print ("not a positive num")
            
        

        

    

print (total)


          
