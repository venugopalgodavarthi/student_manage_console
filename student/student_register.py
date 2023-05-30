def Student_login(coll):
    print("Student Login Process")
    print("-*-"*30)
    email = input("Enter the Email=")
    phone = input("Enter the Phone=")
    print(coll)
    for i in coll:
        print(i.s_email, email, i.s_phone, phone)
        if i.s_email == email and i.s_phone == phone:
            return f"Login Success\n--Mr/Miss {i.s_name}--"
    return "EMAIL and PHONE Incorrect"


class Student:
    college_name="PYSPIDERS"
    college_address='HYD'
    def __init__(self,name,age,email,phone,address):
        self.s_name=name
        self.s_age=age
        self.s_email=email
        self.s_phone=phone
        self.s_address=address

    def display(self):
        print("Student Name:-",self.s_name)
        print("Student Age:-", self.s_age)
        print("Student Email:-", self.s_email)
        print("Student Phone:-", self.s_phone)
        print("Student Address:-", self.s_address)

