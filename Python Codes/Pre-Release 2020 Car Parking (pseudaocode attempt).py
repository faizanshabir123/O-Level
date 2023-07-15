def prm():
    day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturaday"]
    duration = [8,2,2,2,2,2,4]
    price = [2,10,10,10,10,10,3]
    userDay = 0
    userArrivalHour = 0
    userDepartureHour = 0
    parkingDuration = 0
    count = 0
    freqParkingNum = 0
    digit = 0
    num =0
    sUm = 0
    parkingPrice = 0
    pricePaid = 0
    dailyTotal = 0
    discount = 0
    userChoice= ""
    

while userChoice !="k":
    while userDay <=1 and userDay >=7:
        print ("enter day number")
        print ("1-sunday,2-monday,3-tuesday,4-wednesday,5-thursday,6-friday,7-saturday")

    while userArrivalHour <=8 and userArrivalHour >=23:
        print ("enter time of arrival, no parking from midnight to 8 AM")
    while parkingDuration >= duration[userDay] and userDepartHour >24:
        print("enter duration of parking")
        print ("sunday max 8hrs,saturday max 4hrs,otherdays max 2hrs")
        parkingDuration = input(int("enter parking duration"))

        userDepartHour = userArrivalHour + parkingDuration
            
            
               


               


