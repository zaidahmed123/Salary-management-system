#This is the project you are requested to make it good.
class Employee:
    increment = 1.5
    decrement = 0.75
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        self.salary = int(self.salary*Employee.increment)
    def decrease(self):
        self.salary = int(self.salary*Employee.decrement)   
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount        
    @classmethod
    def change_decrement(cls,amount):
        cls.decrement=amount        

print("Employee list\nZaid\nZaid's salary = 50000\nRohan\nRohan's salary = 45000\nSumit\nSumit's salary = 55000")
Zaid = Employee("Zaid","Ahmed Ansari",50000)
Rohan = Employee("Rohan","Das",45000)
Sumit = Employee("Sumit","Sharma",55000)
user_input_employee = input("Select your employee: ")


if user_input_employee=='Zaid':
    user_input_work = input ("What do you want to do?:\nI for salary increment\nD for salary decrement:\nIC for increase the salary by your choice:\nDC for decrease the salary by your choice:\n")
    if user_input_work=="I":
        Zaid.increase()
        print(f"Now Zaid's salary is {Zaid.salary}")
    elif user_input_work=='D':
        Zaid.decrease()
        print(f"Now Zaid's salary is {Zaid.salary}")
    elif user_input_work=='IC':
        c = float(input("How many times you want to increase the salary by the previous one:\n"))
        Employee.change_increment(c)
        Zaid.increase()
        print(f"Now Zaid's salary is {Zaid.salary}")    
    elif user_input_work=='DC':
        c = float(input("How many times you want to decrease the salary by the previous one:\n"))
        Employee.change_decrement(c)
        Zaid.decrease()
        print(f"Now Zaid's salary is {Zaid.salary}")    
    else:
        print("Invalid choice")        

elif user_input_employee=='Rohan':
    user_input_work = input ("What do you want to do?:\nI for salary increment\nD for salary decrement\nIC for increase the salary by your choice:\nDC for decrease the salary by your choice:\n")
    if user_input_work=="I":
        Rohan.increase()
        print(f"Now Rohan's salary is {Rohan.salary}")
    elif user_input_work=='D':
        Rohan.decrease()
        print(f"Now Rohan's salary is {Rohan.salary}")
    elif user_input_work=='IC':
irst type employee name")        c = float(input("How many times you want to increase the salary by the previous one:\n"))
        Employee.change_increment(c)
        Rohan.increase()
        print(f"Now Rohan's salary is {Rohan.salary}")
    elif user_input_work=='DC':
        c = float(input("How many times you want to decrease the salary by the previous one:\n"))
        Employee.change_decrement(c)
        Rohan.decrease()
        print(f"Now Rohan's salary is {Rohan.salary}")
    else:
        print("Invalid choice")        
        

elif user_input_employee=='Sumit':
        user_input_work = input ("What do you want to do?:\nI for salary increment\nD for salary decrement\nIC for increase the salary by your choice:\nDC for decrease the salary by your choice:\n")
        if user_input_work=="I":
            Sumit.increase()
            print(f"Now Sumit's salary is {Sumit.salary}")
        elif user_input_work=='D':
            Sumit.decrease()
            print(f"Now Sumit's salary is {Sumit.salary}")
        elif user_input_work=='IC':
            c = float(input("How many times you want to increase the salary by the previous one:\n"))
            Employee.change_increment(c)
            Rohan.increase()
            print(f"Now Sumit's salary is {Sumit.salary}")  
        elif user_input_work=='DC':
            c = float(input("How many times you want to decrease the salary by the previous one:\n"))
            Employee.change_decrement(c)
            Rohan.decrease()
            print(f"Now Sumit's salary is {Sumit.salary}")      
        else:
            print("Invalid choice")        
else:
        print("Enter correct name")        
