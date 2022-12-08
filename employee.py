"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, isHourly=False, hours=0, salaryPay=0, noOfContracts=0, contractPay=0):
        self.name = name
        self.isHourly = isHourly
        self.hours = hours
        self.salaryPay = salaryPay
        self.noOfContracts = noOfContracts
        self.contractPay = contractPay

    def get_pay(self):
        return ((self.hours * self.salaryPay) + (self.noOfContracts * self.contractPay))

    def __str__(self):
        if (self.isHourly and self.hours > 1):
            workType = "contract"
            amount = "{} hours at {}/hour".format(self.hours, self.salaryPay)
        else:
            workType = "monthly salary"
            amount = "{}".format(self.salaryPay)
            
        if (self.noOfContracts > 1 and self.contractPay > 0):
            contract = " and receives a commission for {} contract(s) at {}/contract".format(self.noOfContracts, self.contractPay)
            amount += contract
        elif (self.noOfContracts == 1):
            contract = " and receives a bonus commission of {}".format(self.contractPay)
            amount += contract
            
        end = " Their total pay is " + str(self.get_pay())
        return "{} works on a {} of {}. {}.".format(self.name, workType, amount, end) 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', isHourly=False, hours=1, salaryPay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', isHourly=True, hours=100, salaryPay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', isHourly=False, hours=1, salaryPay=3000, noOfContracts=4, contractPay=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', isHourly=True, hours=150, salaryPay=25, noOfContracts=3, contractPay=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', isHourly=False, hours=1, salaryPay=2000, noOfContracts=1, contractPay=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', isHourly=True, hours=120, salaryPay=30, noOfContracts=1, contractPay=600)
