#a program that enters 10 positive numbers and returns the total.
total = 0
counter = 0
for count in range(1,10):
    num = int(input("enter a positive number"))
    while num<0:
        num = int(input(" please enter positive number"))
    total = total +num

print(total)    

        


