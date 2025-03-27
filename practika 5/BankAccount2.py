class Person:
    def __init__(self, name, personal_code):
        self.__name = name
        self.__personal_code = personal_code
        self.__accounts = [] 

    def add_account(self, account):
        self.__accounts.append(account)  

    def get_info(self):
        return f"Имя: {self.__name}, Персональный код: {self.__personal_code}"

    def get_accounts(self):
        return self.__accounts 

class BankAccount:
    def __init__(self, account_number, balance=0, owner=None):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner
        if owner:
            owner.add_account(self) 

    def add(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Недостаточно средств на счете.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_owner_info(self):
        if self.__owner:
            return self.__owner.get_info()
        return "Владелец не указан."
    
person = Person("Мария", "12345678901")

account1 = BankAccount("№001", 100, person)
account2 = BankAccount("№002", 200, person)


print(person.get_info())
for account in person.get_accounts(): 
    print(f"Счет: {account.get_account_number()}, Баланс: {account.get_balance()}, Владелец: {account.get_owner_info()}")
