itemIDs = []            #array for holidng all item ids                     (type integer)
itemsDesc = []          #array for holding all item descriptions           (type string) 
bids = []               #array for holding the number of bids for each item (type integer)
resPrice = []           #array for holding the reserve price for each item (type integer)
LastBid = []            #array for holding the last highest bid for each item (type of integer)
itemSold = []           #array that states if item is sold (True) or not (False)
items = 0               #this is the total number of items that the auction company has (type integer)
buyers = []             #this array will hold Buyer Ids (type String) 
RATE = 0.10             #this is a CONSTANT used to hold the rate at which the Auction company calculates its fees

        
def task1():
    global items     #this line establishes link with the global variable "buyers" python syntax
    items = int(input("enter the number of items in the auction(Cannot be less than 3)"))

    while items<3:
        items = int(input("enter the number of items in the auction(Cannot be less than 3)"))

    #initialising the arrays

    for count in range(items):
       itemIDs.append(count)
       desc = input("Please Describe the Item that you are adding")
       itemsDesc.append(desc)
       price = int(input("Enter the Reserve Price as decided by Seller"))
       resPrice.append(price)
       LastBid.append(0)
       bids.append(0)
       itemSold.append(False)

    print(itemIDs)
    print(itemsDesc)
    print(resPrice)
    print(LastBid)
    print(bids)
    

def task2():
    tempID = input("Welcome Buyer if you wish to place a bid enter your ID")
    if tempID not in buyers:
        print("you are not registered before...you will be registered now")
        buyers.append(tempID)
    else:
        print("Welcome Buyer...",tempID)
    
    for i in range(items):
        if itemSold[i] == False:
            print ("The Item ID..", itemIDs[i])
            print ("The Item Desc..", itemsDesc[i])
            print ("The Last Bid..",LastBid[i])
    cont = "y"
    while cont == "y":
        tempitem = int(input("What Item do you want to place a bid on?"))
        while tempitem not in itemIDs:
            tempitem = int(input("Please enter a valid id"))
        print("Please enter a Bid that is greater than  ", LastBid[tempitem] )
        tempbid = int(input())
        while tempbid <= LastBid[tempitem]:
            print("Please enter a Bid that is greater than  ", LastBid[tempitem] )
            tempbid = int(input())
        LastBid[tempitem] = tempbid
        bids[tempitem] = bids[tempitem]+1
        cont = input("more bids y/n")
        
    
def task3():
    print("The Following Items have Been SOLD")
    FeeTotal=0.0
    sold = 0
    notSold = 0
    noBids = 0
    global items
    for j in range(items):
        if LastBid[j] >= resPrice[j]:
            itemSold[j] = True
            FeeTotal = FeeTotal + LastBid[j] * RATE
            print("The Item ID = ", itemIDs[j])
            print("The Item Desc= ", itemsDesc[j])
            print("The Item Last Bid= ", LastBid[j])
            sold = sold + 1
    print("based on the sales the auction company has made a total of...")
    print(FeeTotal)

    print("The Following Items Did not Reach their Reserve Price after bidding...")
    for count in range(items):
        if itemSold[count]==False and bids[count]>=1:
            print("Item Id= ",itemIDs[count])
            print("Item Desc= ",itemsDesc[count])
            print("Item Last Bid",LastBid[count])
            notSold = notSold + 1
            
    print("the following items did not recieve any bids")
    for count in range(items):
        if bids[count]==0:
            print("Item ID= ", itemIDs[count])
            print("Item Desc= ", itemsDesc[count])
            noBids = noBids + 1

    print("A Total of ",sold, "items were sold in this auction")
    print("A Total of ",notSold,"items did not reach their reserve price")
    print("A total of ",noBids,"items did not receive any bids")


    

def auction():
    print ("Welcome to Auction 2019")
    task1()
    more = "y"
    while more == "y" or more =="Y":
        task2()
        more = input("Are there more bidders?")

    task3()


    print("********************************")
    print("Good Bye")
        
            
#calling the whole program
auction()
