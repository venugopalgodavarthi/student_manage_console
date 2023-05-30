from student_register import Student,Student_login

def Register_View():
    print("Student Registrations Process")
    print("-*-"*30)
    l=[]
    n=int(input("enter the no of objects:"))
    for i in range(0,n):
        l+=[Student(input("enter the name"),input("enter the age"),input("enter the email"),input("enter the phone"),input("enter the address"),)]
    return l

def Home_View():
    choose=int(input("Menu:\n1)Register \n2)Exit \nChoose the Option:-"))
    match choose:
        case 1:
            res = Register_View()
            print(Student_login(res))
        case 2:
            exit()
Home_View()