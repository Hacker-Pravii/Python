#using names control using try and except and isalpha and else 
roll1="priyanka"
roll2="shruti"
roll3="ramya"
roll4="kavitha"
roll5="praveen"
teacher=0
print("Teacher calling Roll Number Please say your name \n ")

print("If Present Say Your name otherwise if absent give Enter \n")
present=0
absent=0
pending=0
for i in range(1,6):
    teacher=int(input("Roll Number "))
    if teacher==1:
        a=input("Enter Your Name:")
        try:
            a=int(a)
            print("Error,Please Do not Enter Numarical input considered as absent \n")
            absent+=1
        except:
            if a==roll1:
                print(roll1," is Present \n")
                present+=1
            elif a=="":
                print("Not Answered considered as Absent\n")
                absent+=1
            elif a.isalpha():
                print("Entered Spelling is mistake considered is pending\n ")
                pending+=1
            else:
                print(roll1,"is absent symbol is not allowed\n") #excecte if any symbolic 
                absent+=1
    
    elif teacher==2:
        a=input("Enter Your Name:")
        try:
            a=int(a)
            print("Error,Please Do not Enter Numarical input considered as absent \n")
            absent+=1
        except:
            if a==roll2:
                print(roll2," is Present \n")
                present+=1
            elif a=="":
                print("Not Answered considered as Absent\n")
                absent+=1
            elif a.isalpha():
                print("Entered Spelling is mistake considered is pending\n ")
                pending+=1
            else:
                print(roll2,"is absent symbol is not allowed\n") #excecte if any symbolic 
                absent+=1
    elif teacher==3:
        a=input("Enter Your Name:")
        try:
            a=int(a)
            print("Error,Please Do not Enter Numarical input considered as absent \n")
            absent+=1
        except:
            if a==roll3:
                print(roll3," is Present \n")
                present+=1
            elif a=="":
                print("Not Answered considered as Absent\n")
                absent+=1
            elif a.isalpha():
                print("Entered Spelling is mistake considered is pending\n ")
                pending+=1
            else:
                print(roll3,"is absent symbol is not allowed\n") #excecte if any symbolic 
                absent+=1
    elif teacher==3:
            a=input("Enter Your Name:")
            try:
                a=int(a)
                print("Error,Please Do not Enter Numarical input considered as absent \n")
                absent+=1
            except:
                if a==roll3:
                    print(roll3," is Present \n")
                    present+=1
                elif a=="":
                    print("Not Answered considered as Absent\n")
                    absent+=1
                elif a.isalpha():
                    print("Entered Spelling is mistake considered is pending\n ")
                    pending+=1
                else:
                    print(roll3,"is absent symbol is not allowed\n") #excecte if any symbolic 
                    absent+=1
    elif teacher==4:
            a=input("Enter Your Name:")
            try:
                a=int(a)
                print("Error,Please Do not Enter Numarical input considered as absent \n")
                absent+=1
            except:
                if a==roll4:
                    print(roll4," is Present \n")
                    present+=1
                elif a=="":
                    print("Not Answered considered as Absent\n")
                    absent+=1
                elif a.isalpha():
                    print("Entered Spelling is mistake considered is pending\n ")
                    pending+=1
                else:
                    print(roll4,"is absent symbol is not allowed\n") #excecte if any symbolic 
                    absent+=1
    elif teacher==5:
            a=input("Enter Your Name:")
            try:
                a=int(a)
                print("Error,Please Do not Enter Numarical input considered as absent \n")
                absent+=1
            except:
                if a==roll5:
                    print(roll5," is Present \n")
                    present+=1
                elif a=="":
                    print("Not Answered considered as Absent\n")
                    absent+=1
                elif a.isalpha():
                    print("Entered Spelling is mistake considered is pending\n ")
                    pending+=1
                else:
                    print(roll5,"is absent symbol is not allowed\n") #excecte if any symbolic 
                    absent+=1
    else:
        print("This roll Number not in list")
  
print("studnets Present is class ",present)

print("studnets Absent is class ",absent)

print("Students Entered name wrong ",pending)