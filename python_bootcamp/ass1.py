
repeat=1

while repeat==1:
    a=int(input("Enter the marks of the student : "))
    if a>=90 and a<=100:
        print("Your grade is A+")
    elif a>=80 and a<90:
        print("Your grade is A")
    elif a>=70 and a<80:
        print("Your grade is B")
    elif a>=60 and a<70:
        print("Your grade is C")
    elif a>=50 and a<60:
        print("Your grade is D")
    elif a>=00 and a<50:
        print("You have been fail")
    else:
        print("entered marks is not valid")
    
    repeat=int(input("press 1 to continue or any other key to exit"))