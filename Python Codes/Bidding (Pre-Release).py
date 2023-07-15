ItemIDs = []
ItemDescription = []
Bids = []
ReservePrice = []
LastBid = []
ItemSold = []
BuyerIDs = []
NumberOFItems = 0
Fee = 0.1

 
def Task1():#function1

    global NumberOFItems 
    NumberOFItems = int(input("enter the number of item(should be 4 or more than 4)"))
    while NumberOFItems<4:
         NumberOFItems = int(input("enter the number of item(should be 4 or more than 4)"))
         
    for counter in range(NumberOFItems):#recording all the details about the items
        ItemIDs.append(counter)
        description = input("give the description of the item")
        ItemDescription.append(description)
        cost = int(input("give the reserve price of the item"))
        ReservePrice.append(cost)
        LastBid.append(0)
        Bids.append(0)
        ItemSold.append(False)
        
    print("the item ids of your items concide with the index positions",ItemIDs)
    
def Task2():#fucntion2
    ID = input("to get registered and place a bid, enter your id")
    BuyerIDs.append(ID)
    
        
    for counter1 in range(NumberOFItems):
        if ItemSold[counter1] != True:
            print("the itemid is",ItemIDs[counter1])
            print("the description of your items is",ItemDescription[counter1])
            print("the current highest bid on your items ",LastBid[counter1])
        
    

    Morebids = "yes"
    while Morebids == "yes":
        entity = int(input("on which item id do you want to  place a bid on"))
        while entity not in ItemIDs:
            entity = int(input("enter a valid item id"))
        print("enter a bid more than",LastBid[entity])
        bid = int(input())
        while bid <= LastBid[entity]:
           print("your bid must be more than",LastBid[entity])
           bid = int(input())
        LastBid[entity] = bid
        Bids[entity] = Bids[entity]+1
        Morebids = input("If you want to make more bids enter yes or enter no to finish the bidding process")
                                 
def Task3():#fucntion3
    Totalfee = 0.0
    Itemssold = 0
    Itemsnotsold = 0
    Nobids = 0

    print("the items sold or that have reached their reserved price(if any) are given below:")
    for counter2 in range(NumberOFItems):
        if LastBid[counter2] >= ReservePrice[counter2]:
            ItemSold[counter2] = True
            Totalfee = Totalfee + LastBid[counter2] * Fee
            print("the item id is",ItemIDs[counter2])
            Itemssold = Itemssold + 1
    print("the fee total is:",Totalfee)

    print("the items which did not reach their reserve price(if any) are given below:")

    for counter3 in range(NumberOFItems):
        if ItemSold[counter3] !=True and Bids[counter3]>=1:
            print("the item number or id is",ItemIDs[counter3])
            print("the final bid is",LastBid[counter3])
            Itemsnotsold = Itemsnotsold + 1
            
    print("the items which did not recived any bids(if any) are given below:")
    for counter4 in range(NumberOFItems):
        if Bids[counter4] == 0:
            print("the item number is is",ItemIDs[counter4])
            Nobids = Nobids + 1
            
    print("the number of items which were sold are",Itemssold)
    print("the number of items which were not sold are",Itemsnotsold)
    print("the number of items with 0 bids are",Nobids)
    
          
def auction():#calling all three functions in a single function
    Task1()
    Task2()
    Task3()
    
    
      
        
        
        
            
            
            
            
    
        
        
                   
        
        

    
    

