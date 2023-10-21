
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, user, amount):
        self.username = user
        self.balance = amount

    def checkTransaction(self, amount):
        if self.balance >= amount:
            return amount
        else:
            raise BalanceException(f"You don't have enough balance. Current balance: ${self.balance:.2f}")
    
    def userInformation(self):
        print(f"\nUser: {self.username}\nCurrent Balance: ${self.balance:.2f}")
        print("\n----------------------------")

    def transactionType(self, type, amount):
        print(f"\n{type} 🏧")
        print(f"{type} amount: ${amount:.2f}\n")

    def deposit(self, amount):
        self.balance += amount
        self.transactionType("Deposit", amount)
        self.userInformation()

    def withdraw(self, amount):
        try:
            self.checkTransaction(amount)
            self.balance -= amount
            print("\nWithdraw 🏧\n")
            print(f"Withdraw amount: ${amount:.2f}")
            self.userInformation()
        except BalanceException as error:
            self.transactionType("Withdraw", amount)
            print(f"Transaction Failed! ⚠️\n{error}")
            self.userInformation()
    
    def transfer(self, user, amount):
        try:
            self.checkTransaction(amount)
            self.balance -= amount
            user.deposit(amount)
            self.userInformation()
        except BalanceException as error:
            self.transactionType("Transfer", amount)
            print(f"Transaction Failed! ⚠️\n{error}")
            self.userInformation()


class InterestRewardDeposit(BankAccount):
    interest = 15
    def deposit(self, amount):
        self.balance += (amount + (amount * InterestRewardDeposit.interest / 100))
        self.transactionType("Interest Deposit", amount)
        print(f"Interest: {InterestRewardDeposit.interest}%")
        self.userInformation()

class SavingsAcct(InterestRewardDeposit):
    def __init__(self, user, amount):
        super().__init__(user, amount)
        self.fees = 5
    
    def withdraw(self, amount):
        try:
            self.transactionType("Withdraw Savings", amount)
            self.checkTransaction(amount)
            self.balance -= (amount - (amount * self.fees / 100))
            self.userInformation()
        except BalanceException as error:
            self.transactionType("Withdraw Savings", amount)
            print(f"Transaction Failed! ⚠️\n{error}")

# user1 = BankAccount("Fyqq", 250)
# user2 = BankAccount("Sarah", 50)
# user1.userInformation()
# user1.deposit(20)
# user1.withdraw(252)
# user1.transfer(user2, 150)

# user1 = InterestRewardDeposit("John", 1150)
# user1.deposit(200)

user1 = SavingsAcct("Dilan", 550)
user1.withdraw(660)









