class Pocket:

    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return ("Account balance : %d" % self.balance)

    def deposit(self, amount):
        if (type(amount) == int and amount > 0):
            self.balance += amount
        else:
            pass
    
    def withdraw(self, amount):
        if (type(amount) == int and amount > 0):
            if self.balance - amount >= 0:
                self.balance -= amount
            else:
                pass
        else:
            pass

    

    

