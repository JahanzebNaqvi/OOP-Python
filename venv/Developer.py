from Employee import Employee
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay,prog_lang):
        super().__init__( first, last, pay) #More Readable and Maintable as in inheritance
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

