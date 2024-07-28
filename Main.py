#Taking user inputs
Pass=(input("Enter your credits at pass: "))
Defer=(input("Enter your credits at DEFER: "))       
Fail=(input("Enter your credits at Fail: "))

flag1=True

na=nb=nc=nd=0

while flag1:

    if not(Pass.isdigit() and Defer.isdigit() and Fail.isdigit()):
        print("Integer required.")
    elif int(Pass)+int(Defer)+int(Fail)!=120:
        print("Total incorrect")
    elif not((int(Pass) in [0,20,40,60,80,100,120]) and (int(Defer) in [0,20,40,60,80,100,120] ) and (int(Fail) in [0,20,40,60,80,100,120])):
        print("Out of range")
    else:
        Pass=int(Pass)
        Defer=int(Defer)
        Fail=int(Fail)

        # Printing the grade according to the number of credits
        if Pass==120:
            print("A")
            na+=1
        elif Pass==100 and (Defer==20 or Fail==20):
            print("B")
            nb+=1
        elif (Pass==40 and Fail==80) or (Pass==20 and (Defer<=20 and Defer+Fail==100)) or (Pass==0 and (Defer<=40 and Defer+Fail==120)):
            print("D")
            nd+=1
        else:
            print("C")
            nc+=1
    print("Would you like to eneter another set of data?")
    cont=input("Enter y for yes or q for quit: ")
    flag2=True
    
    while flag2:
        if cont=="y":
            Pass=(input("Enter your credits at pass: "))
            Defer=(input("Enter your credits at DEFER: "))       
            Fail=(input("Enter your credits at Fail: "))
            flag2=False
        elif cont=="q":
            print("------------------------------------------------------------------------------------------------")
            
            L=[na,nb,nc,nd]
            L_String=[]

            while not(all(g==0 for g in L)):
                L_String.append(["*" if k>=1 else " " for k in L])
                L=[h-1 if h>=1 else h for h in L]
            L_String2=[' '.join(p) for p in L_String]
            L_String2.insert(0,"A B C D")
            
            for i in L_String2:
                print(i)
            
            
                
            
            flag2=False
            flag1=False
            
        else:
            print("You have entered a wrong input, Try with y and q only!!!")
            print("Would you like to enter another set of data?")
            cont=input("Enter y for yes or q for quit: ")
            
            
            
