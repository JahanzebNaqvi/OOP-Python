from Manager import Manager
from Developer import Developer
from Employee import Employee



dev_1 = Developer('Dev','User1',50000,'Java')
dev_2 = Developer('Dev','User2',60000,'Python')
print(dev_1.fullname())

# print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.fullname())
print(dev_1.prog_lang)

print(dev_2.fullname())
print(dev_2.prog_lang)

print('Number of All Employees : {}'.format(Developer.num_of_emp))


mgr_1 = Manager('Manager','User 1',78000,[dev_1])

mgr_1.add_emp(dev_2)
print(mgr_1.fullname())
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print('Is object a istance of Developer Class',isinstance(dev_1,Developer))
print('is Developer subclass of Employee: ',issubclass(Developer,Employee))
print('Is object a istance of Manager Class',isinstance(mgr_1,Manager))
