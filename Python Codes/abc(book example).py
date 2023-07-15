def main1():
   FirstNumber = int (0)
   SecondNumber = int (0)
   Sum = int(0)
   FirstNumber = int(input("enter first whole number"))
   SecondNumber = int(input("enter secong whole number"))
   if FirstNumber > SecondNumber:
      print ("First number is largest",Firstnumber)
   else:
         print ("second number is largest",SecondNumber)
      

def main2():
   Number = int(0)
   Count = (0)
   Sum = int(0)
   while Count < 5:
      Number = int(input("enter a whole number"))
      Sum = Sum + Number
      Count =  Count + 1
   print ("sumof five numbers is",Sum)


def main3():
   NumberOfTickets = int(0)
   Discount = float(0)
   Cost = float(0)
   while NumberOfTickets >1 and NumberOfTickets <26:
      NumberOfTickets = float(input("how many tickets would you like to buy"))
   Discount = 0.2
   if NumberOfTickets < 10:
      Discount = 0
   elif NumberOfTickets < 20:
      Discount = 0.1
   Cost = NumberOfTickets * 20 * (1 - Discount)
 
   
