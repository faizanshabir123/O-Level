import random

#Arrays
valid_check = ["0","1","2","3","4","5","6","7","8","9","x","X"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#CONSTANTS
#for holding rates for dicount
DISCOUNT1 = .10   
DISCOUNT2 = .50


#Subroutine for Generating a 5digit Discount code
def generate_code():
    new_code = ""
    for count in range(4):
        digit = random.randint(0,9)
        new_code = new_code+str(digit)
    temp = 5*int(new_code[0])+4*int(new_code[1])+3*int(new_code[2])+2*int(new_code[3])           
    temp = 11-(temp%11)
    if  temp == 11:
        new_check = "0"     
    elif temp == 10:
        new_check = "x"
    else:
        new_check = str(temp)

    new_code=new_code+new_check
    print("Here is your new code, please keep it safe to avail discounts next time  ",new_code)

#Subroutine for Verifying a 5 digit Discount code.
def verify_code(user_code):
    if user_code[4] == "0":
        check_digit = 11
    elif user_code[4] == "x" or user_code[4]=="X":
        check_digit = 10

    else:
        check_digit = int(user_code[4])    
    temp = (5*int(user_code[0])+4*int(user_code[1])+3*int(user_code[2])+2*int(user_code[3]))+check_digit
    if temp%11==0:
        print("Code is Valid")
        code_valid = 1
    else:
        print("Code is Not Valid")
        code_valid = 0
    if code_valid == 0:
        print("You did not enter a valid code")
    return code_valid
################################################################################################################################################################################

def main():

##################################################################      TASK 1     ########################################################################
    
    cont = "y"
    code_valid,day,prev_day,daily_total,prev_time = 0,0,0,0,0  
#all types above are integer
#code_valid will hold 1 if the user has entered a valid code and 0 if the user has entered a invalid code
#prev_day will hold the day number of the previous day and will be reset each time a new day is selected
#daily_total will hold the earning for each day
#prev_time will hold the latest time of the previous customer
   
    discount_choice = " "
    while cont == "y" or cont == "Y":
        Allowed_Time,Within_Day,First_Half = False,False,False
        print("Welcome User")
        discount_choice = input("Press 1 if you have a discount code or anything else if you don't")
        if discount_choice == "1":
            user_code = input("enter a valid code  ")    

            
            #VALIDATION CHECK 1
            while (len(user_code)!=5) or (not(user_code[0:4].isdigit()) or (user_code[4] not in valid_check)):
                user_code = input("You have not entered a valid 5 digit code, only for example 1234X  ") 
            #VALIDATION CHECK 1 ENDS HERE
            
            code_valid = verify_code(user_code)
        
        if code_valid == 0 or discount_choice != "1":

            generate_code()                
                
                         
        print("""
        What Day is it?
            1. Monday
            2. Tuesday
            3. Wednesday
            4. Thursday
            5. Friday
            6. Saturday
            7. Sunday""")

        day = int(input("enter day number "))

        
        #VALIDATION CHECK 2     
        #This Validation Check Makes Sure that the user selects only a valid day

        while day not in (1,2,3,4,5,6,7):
            day = int(input("Please enter a valid day number "))

        #VALIDATION CHECK 2 ENDS HERE

########################################################################    TASK 2   #########################################################################

        if day != prev_day and prev_day!=0:
            print("It is a new day")
            print("The Earning for Day ",days[prev_day-1]," is ",daily_total)
            daily_total = 0
            prev_time = 0
        
#   VALIDATION CHECK 3
#        This Validation Check ensures that the
#       (1) (valid_time) If the users has entered a valid arrival time i.e. b/w 800 and 2300 AND
#            if the arrival time for that customer is after than the last customer's arrival time
#       (2)  If the user is allowed to park desired hours based on the day selected (allowed_time)
#       (3)  If the user's required time allows him/her to leave before midnight (within_day).
        
        
        while Allowed_Time == False or Within_Day == False:
            arrival_time = int(input("Please Enter Arrival Time"))

            while arrival_time<8 or arrival_time>23:
                arrival_time= int(input("the time of arrival is not valid between midnight to 8am  "))
            while arrival_time<prev_time and prev_time != 0:
                print("You cannot possibly come before ",prev_time)
                arrival_time = int(input("Please Re-Enter Arrival Time"))
            if arrival_time>=8 and arrival_time <= 15:
                First_Half = True
            else:
                First_half = False
            
            req_time = int(input("enter required time  "))

            if (day in (1,2,3,4,5)) and First_Half == True:
                max_hours = 2
                per_hour = 10
                dis_rate = DISCOUNT1
            elif day==6 and First_Half == True:
                max_hours = 4
                per_hour = 3
                dis_rate = DISCOUNT1
            else:
                if arrival_time>=8 and arrival_time<=15:
                    per_hour = 2
                    dis_rate = Discount1
                    First_Half = True
                else:
                    dis_rate = DISCOUNT2

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
#   VALIDATION CHECK 3 ENDS HERE

        dis_rate = dis_rate * code_valid

        if First_Half == True:
            total_amount = ((req_time) * per_hour)
        else:
            total_amount = 2        

        amount_payable = total_amount-(total_amount*dis_rate)
        print("Total Payable  ",amount_payable)

#########################################################################           TASK 3       ###################################################

        if (arrival_time<16) and((arrival_time + req_time)>16):
            new_amount = 0
            first_half = 0
            print("Applying task 3(making payments fairer)")
            first_half = 16-arrival_time
        
            if code_valid == 1:
                new_amount = ((first_half*per_hour) * (1-DISCOUNT1)) + 1
            else:
                new_amount = (first_half*per_hour) + 2
        #task 2
                #amount_payable (integer) the amount owed by customer
            amount_payable = new_amount
        print("Your Total Bill is ", amount_payable)
        amount_paid = int(input("please make payment"))

# VALIDATION CHECK 4
    # This Validation check ensures that the user pays (amount_paid) an amount that is either more or equal to the amount owed (amount_payable)  
        while amount_paid < amount_payable:
            print("you must atleast pay ", amount_payable)
            amount_paid = int(input("please make payment"))
#VALIDATION CHECK 4 ENDS


        daily_total = daily_total + amount_paid         #daily_total (integer) adds the total amount earned in one day. 

        prev_day = day
        prev_time = arrival_time

        print("The daily Total so far ", daily_total)
        
        cont = input("are there more customers? Y or y for Yes anything else for no")

        
main()




