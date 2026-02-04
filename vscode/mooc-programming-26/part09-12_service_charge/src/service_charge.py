# WRITE YOUR SOLUTION HERE:


class BankAccount():
    def __init__(self, owner: str, acc_numb: int, balance: float):
        self.__owner = owner
        self.__acc_number = acc_numb
        self.__balance = balance
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    def withdraw(self, amount: float):
        if self.__balance - amount < 0:
            return
        self.__balance -= amount
        self.__service_charge()
        
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
        
    def __service_charge(self):
        self.__balance = self.__balance * 0.99
        
        
if __name__ == "__main__":     
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)