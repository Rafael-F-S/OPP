
"""
class Employee:
    pass

emp_1=Employee()
emp_2=Employee()

print(emp_1)
print(emp_2)

emp_1.first = "Rafael"
emp_1.last = "Silva"
emp_1.email = "Rafael.silva@company.com"
emp_1.pay = 50000

emp_2.first = "test"
emp_2.last = "user"
emp_2.email = "test.user@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print("-*-"*20)

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"


emp_1 = Employee("Rafael", "Silva", 50000)
emp_2 = Employee("test", "user", 60000)

print(emp_1.email)
print(emp_2.email)

print("{} {}".format(emp_1.first,emp_1.last))

"""
print("-*-"*20)

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Rafael", "Silva", 50000)
emp_2 = Employee("test", "user", 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

#they do the same thing
print("--")
print(emp_1.fullname())
print("--")
print(Employee.fullname(emp_1))

