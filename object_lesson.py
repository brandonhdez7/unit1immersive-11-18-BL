class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Employee.empCount += 1
    
    # def displayCount(self):
        # print "Total Employee: 1" #Employee.empCount
    
    def displayEmployee(self):
        print "Name: ", self.name, ", Salary: ", self.salary

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

print emp1.displayEmployee()
print emp2.displayEmployee()