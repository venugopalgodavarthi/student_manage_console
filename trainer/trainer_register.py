from student.student_register import Student

class Trainer(Student):
    def display(self):
        print("Trainer Name:-",self.s_name)
        print("Trainer Age:-", self.s_age)
        print("Trainer Email:-", self.s_email)
        print("Trainer Phone:-", self.s_phone)
        print("Trainer Address:-", self.s_address)


rama=Student("rama",'26','rama@gmail.com','9988774422','hyd')
print(rama.__dict__)
rama.display()


obj=Trainer("Girish","30","girish@gmail.com","9988775522","Bangalore")
print(obj.__dict__)
obj.display()