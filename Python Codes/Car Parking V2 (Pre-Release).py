import random
valid_check = ["0","1","2","3","4","5","6","7","8","9","x","X"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
SECOND_HALF = .50
FIRST_HALF = .10
def main():
    #Task 1
    cont = "y"
    code_valid = 0
    day = 0
    prev_day = 0
    daily_total = 0
    while cont == "y" or cont == "Y":
        print("Welcome User")
        choice = "0"
        choice = input("Press 1 if you have a discount code or anything else if you don't")
        if choice == "1":
            user_code = input("enter a valid code  ")
            while (len(user_code)!=5) or (not(user_code[0:4].isdigit()) or (user_code[4] not in valid_check)):
                user_code = input("you have not entered a valid 5 digit code only for example 1234X  ")
            if user_code[4] == "0":
                check = 11
            elif user_code[4] == "x" or user_code[4]=="X":
                check = 10
            else:
                check = int(user_code[4])
            temp = (5*int(user_code[0])+4*int(user_code[1])+3*int(user_code[2])+2*int(user_code[3]))+check
            if temp%11==0:
                print("Code is Valid")
                code_valid = 1
            else:
                print("Code is Not Valid")
                code_valid = 0
            if code_valid == 0:
                print("you did not enter a valid code")
        if choice != "1" or code_valid == 0:
            new_code = ""
            for count in range(4):
                digit = random.randint(0,9)
                new_code = new_code+str(digit)
            temp = 5*int(new_code[0])+4*int(new_code[1])+3*int(new_code[2])+2*int(new_code[3])           
            temp = 11-(temp%11)
            if  temp == 11:
                check = "0"     
            elif temp == 10:
                check = "x"
            else:
                check = str(temp)

            new_code=new_code+check
            print("here is your new code please keep it safe to avail discounts next time  ",new_code)
            
        print("""
        What Day is it?
            1. Monday
            2. Tuesday
            3. Wednesday
            4. Thursday
            5. Friday
            6. Saturday
            7. Sunday""")
        day = int(input("enter day  "))
        while day not in (1,2,3,4,5,6,7):
            day = int(input("enter a valid day  "))
        #also linked with task 2        
        if day != prev_day and prev_day!=0:
            print("it is a new day")
            print("the Earning for Day ",days[prev_day-1]," is ",daily_total)
            daily_total = 0
        
        Allowed_Time= False

        Within_Day=False
        First_Half = False
        arrival_time = int(input("time of arrival  "))

        while arrival_time<8 or arrival_time>23:
            arrival_time= int(input("the time of arrival is not valid not between midnight to 8am  "))
        
        while Allowed_Time == False or Within_Day == False:
                        
            req_time = int(input("enter required time  "))
            if day in (1,2,3,4,5):
                max_hours = 2
                if arrival_time>=8 and arrival_time<=15:
                    per_hour = 10
                    dis_rate = FIRST_HALF
                    First_Half = True
                else:
                    dis_rate = SECOND_HALF
            elif day==6:
                max_hours = 4
                if arrival_time>=8 and arrival_time<=15:
                    per_hour = 3
                    dis_rate = FIRST_HALF
                    First_Half = True
                else:
                    dis_rate = SECOND_HALF
            else:
                max_hours = 8
                if arrival_time>=8 and arrival_time<=15:
                    per_hour = 2
                    dis_rate = FIRST_HALF
                    First_Half = True
                else:
                    dis_rate = SECOND_HALF

            if req_time > max_hours:
                print("you cannot park for that long  ")
                Allowed_Time = False
            else:
                Allowed_Time = True
            if (req_time + arrival_time) >24:
                print("you will have to leave before the parking lot closes  ")
                Within_Day = False
            else:
                Within_Day = True

        dis_rate = dis_rate * code_valid
        if First_Half == True:
            total_amount = ((req_time) * per_hour)
        else:
            total_amount = 2        
        amount_payable = total_amount-(total_amount*dis_rate)
        print("Total Payable  ",amount_payable)
        # task 3
        if (arrival_time<16) and((arrival_time + req_time)>15):
            new_amount = 0
            first_half = 0
            print("Applying task 3")
            first_half = 16-arrival_time
        
            if code_valid == 1:
                new_amount = ((first_half*per_hour) * (1-FIRST_HALF)) + 1
            else:
                new_amount = (first_half*per_hour) + 2
        #task 2  
            amount_payable = new_amount       
        daily_total = daily_total + amount_payable
        prev_day = day
        cont = input("are there more customers? Y or y for Yes anything else for no")

        
main()




