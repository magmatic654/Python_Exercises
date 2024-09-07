import pkg

class BankAccount:
    def __init__(self, account_number, holder_name, balance = 0):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance
    
    @property
    def account_number(self):
        return self._account_number
    
    @account_number.setter
    def account_number(self, new_account_number):
        self._account_number = new_account_number
    
    @property
    def holder_name(self):
        return self._holder_name
    
    @holder_name.setter
    def holder_name(self, new_holder_name):
        self._holder_name = new_holder_name
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        pkg.utils.check_negative(new_balance)
        self._balance = new_balance
    
    def deposit(self, amount):
        try:
            pkg.utils.check_negative_and_zero(amount)
            self._balance += amount
            return True # El deposito fue exitoso
        except ValueError as error:
            return error
        
    def withdraw(self, amount):
        try:
            pkg.utils.check_negative_and_zero(amount)
            if self._balance < amount:
                raise ValueError('No tienes fondos suficientes para realizar la operación')
            self._balance -= amount
            return True # El retiro fue exitoso
        except ValueError as error:
            return error
        
    def check_balance(self):
        return self._balance
    
if __name__ == '__main__':
    account = BankAccount(123456789, 'José Peréz Pereira', 250) 
    print(account.check_balance())
    print(account.deposit(-200))
    print(account.withdraw(-100))
    print(account.withdraw(0))
    print(account.deposit(0))
    print(account.check_balance())

    print(account.deposit(100))
    print(account.withdraw(250))
    print(account.withdraw(250))
    print(account.check_balance())