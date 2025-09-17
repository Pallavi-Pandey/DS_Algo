# Encapsulation
# Hiding the internal implementation details of a class from the user.

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def transfer(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

my_bank = Bank(1000)
print(my_bank.get_balance())
my_bank.set_balance(2000)
print(my_bank.get_balance())