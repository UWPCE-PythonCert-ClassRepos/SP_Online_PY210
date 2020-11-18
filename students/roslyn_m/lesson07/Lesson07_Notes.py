class Employee:

    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay): # "self" refers to automatically taking in the instance
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# 2 ways to call fullname:
emp_1.fullname()
Employee.fullname(emp_1)

# Class Variables: variables that are shared among all instances of a class
# while instance variables can be unique for each instance like our names and email and pay
# class variables should be the same for each instance

print(Employee.__dict__)
print(emp_1.__dict__)

Employee.raise_amt = 1.04 # can set raise amount by class
emp_1.raise_amt = 1.09 # can set it for one instance specifically
# Now call properties, and you will see emp_1 has raise amt
print(Employee.__dict__)
print(emp_1.__dict__)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# class method vs Static methods
# When working with classes..... reg methods pass instance as the first argument, class methods automatically pass class as first.
# static method dont pass anything (no class or instance). Behave just like reg functions, but we include thm in our classes because they pertian to class
# If you dont access instance or the class, it should prob be an @staticmethod

print(vars(emp_1)) #gives attributes of an instance