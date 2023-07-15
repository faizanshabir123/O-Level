StudentNames = []
Test1Marks = []
Test2Marks = []
Test3Marks = []
TotalScore = []
avg = float(0)
highscore = int(-1)
bestname = ""


def task1():
    print("Enter the names of thirty students")
    for a in range(3):
        name = input("enter name")
        StudentNames.append(name)
        mark1 = int(input("enter marks for test 1 for this student"))
        while mark1 < 0:
             mark1 = int(input("enter marks for test 1 for this student"))
        Test1Marks.append(mark1)
        mark2 = int(input("enter marks for test 2 for this student"))
        while mark2 < 0:
             mark2 = int(input("enter marks for test 2 for this student"))
        Test2Marks.append(mark2)
        mark3 = int(input("enter marks for test 3 for this student"))
        while mark3 < 0:
             mark3 = int(input("enter marks for test 3 for this student"))
        Test3Marks.append(mark3)

    print(StudentNames)
    print(Test1Marks)
    print(Test2Marks)
    print(Test3Marks)
 
def task2():
    classtotal = int(0)
    for b in range(3):
        total = Test1Marks[b] + Test2Marks[b] + Test3Marks[b]
        TotalScore.append(total)
        classtotal = classtotal + TotalScore[b]      
    avg = classtotal / 3
    print("the total marks score by each student are shown below")
    for c in range(3):
        print(StudentNames[c],TotalScore[c])
    print("the average total score for the class is",avg)

def task3():
    highscore = int(-1)
    bestname = ""
    for d in range(3):
        if TotalScore[d] > highscore:
            highscore = TotalScore[d]
            bestname = StudentNames[d]
    print("the student with the highest total score is",bestname,"and he scored",highscore)         
            
    
    
            
         
      
   
def auction():
    task1()
    task2()
    task3()
        
    
   


        
        
        
                    
    

    
