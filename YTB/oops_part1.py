class Employee:

    raise_percentage = 1.04 #class variable 
    count = 0

    __slots__ = ["first","last","pay","gmail","__dict__"] #enforce the python

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.gmail = f"{self.first.lower()}.{self.last.lower()}@xyz.com"
        Employee.count += 1 #instance 
        # self.count += 1 won't use if it is in global because in dict it will check if not found it will take as global value

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self):
        self.pay = int(self.pay* self.raise_percentage) # here if u use Employee.raise_percentage u won't modify at instance level like emp1,emp2


emp1 = Employee("chandra", "p", 30000)
emp2 = Employee("chandru", "chandu", 15000)

print(emp1.gmail)          # should print: chandra.mouli@xyz.com
print(emp1.full_name())    # should print: chandra mouli
#print(emp2.__dict__)       # should print emp2’s attributes as a dict
print(emp1.pay)
#emp1.increase_pay(5)
print(emp1.pay)
print(emp2.pay)
#Employee.increase_pay(emp2,5)
print(emp2.pay)
#print(emp1.__dict__)
#emp1.pya = 2000 #Won't allow this misspelled attr because of slots
#print(emp1.__dict__)
print(Employee.raise_percentage)
print(emp1.raise_percentage)
print(emp1.pay)
emp1.increase_pay()
print(emp1.pay)

print(emp1.__dict__) #raise_percentage won't here
print(Employee.__dict__) #raise_percentage is here

#override class variable
Employee.raise_percentage = 1.07
print(Employee.raise_percentage)
print(emp1.raise_percentage)
emp2.raise_percentage = 1.17
print(emp2.raise_percentage)

print(Employee.count) #2

print(emp1.count)