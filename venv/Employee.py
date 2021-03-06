class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Class variable
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # instance variable find variable in instance then in the Class
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return "'{}','{}'".format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Employee','User',20000)
emp_2 = Employee('Test','User',30000)

print(emp_1.first)
print(emp_2.first)

print(emp_2) # Checks if str dunker present call str dunker otherwise callback to repr dunker
print(emp_2.__repr__())
print(emp_2.__str__())

print(emp_1+emp_2)

print(emp_2.__len__())