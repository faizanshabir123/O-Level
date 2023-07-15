#Global (can be accessed by all subroutine
name = []
discount = []
#balance = []
RATE1 = 10
RATE2 = 50
hours = 0
cost = 0
day = 0
arrival_hour = 0



def task1():
    print("""
            1 Monday
            2 Tuesday
            3 Wednesday
            4 Thursday
            5 Friday
            6 Saturday
            7 Sunday""")
    day = int(input("select a valid day"))
    arrival_hour = int(input("enter the arrival hour only"))
    while day<1 or day>7:
        day = int(input("select a valid day"))
    while (arrival_hour + hours) > 24:
        if day in (1,2,3,4,5):
            hours = int(input("enter the number of hours"))
            while hours<1 or hours>2:
                hours = int(input("enter the number of hours"))
        elif day == 6:
            hours = int(input("enter the number of hours"))
            while hours<1 or hours>4:
                hours = int(input("enter the number of hours"))
        else:
            hours = int(input("enter the number of hours"))
            while hours<1 or hours>8:
                hours = int(input("enter the number of hours"))

    arrival_hour = int(input("enter the arrival hour only"))

    while arrival_hour<0 or arrival_hour>23:
        arrival_hour = int(input("enter valid arrival hour only"))
    
    
    if (arrival_hour + hours) > 24:
        print("you cannot park beyond midnight")


task1()
