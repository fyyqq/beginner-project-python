
class BalanceException(Exception):
    pass

class Database:
    data = {}

class Auth:
    data = Database.data

    def exit():
        print("\nThank you for using our services. 👋\n")
    
    def register():
        print("\n=========================\n")
        print("Register 📝\n")
        user = input(f"Username: ")
        pin = input(f"Pincode: ")
        if pin in Auth.data:
            print(f"Pincode '{pin}' already have in database")
            confirmation = input("\nPress 'Enter' to Login ('q' to quit) : ")
            if confirmation == 'q':
                Auth.exit()
            else:
                Auth.login()
        else:
            Database.data[pin] = { "username": user, "pincode": pin, "balance": 0 }
            Auth.userInformation(pin)
            print("\n=========================\n")
        return pin

    def login():
        print("\nLogin 📝\n")
        pin = input(f"Pincode: ")
        
        if pin in Auth.data:
            Auth.userInformation(pin)
        else:
            print(f"Pincode '{pin}' doesn't have in database")
            confirmation = input("\nPress 'Enter' to Register ('q' to quit) : ")
            if confirmation == 'q':
                Auth.exit()
            else:
                Auth.register()
        return pin

    def userInformation(pincode):
        data = Auth.data[pincode]
        print("\n=========================\n")
        print("User Information 📄\n")
        print(f"Username: {data['username']}\nPincode: {data['pincode']}\nBalance: ${data['balance']}")


class Atm:
    def __init__(self, username, pincode, balance):
        self.username = username
        self.pincode = pincode
        self.balance = balance
    
    def validationTransaction(self, amount):
        if self.balance >= amount:
            return amount
        else:
            raise BalanceException(f"\nYou do not have enough balance. Current balance: ${self.balance}\n")

    def deposit(self, amount):
        print("\n=========================\n")
        print(f"Deposit 💵")
        print(f"Deposit amount: ${amount}\n")
        print(f"Old balance: ${self.balance}")
        self.balance += amount
        print(f"Current balance: ${self.balance}")
        print("\n=========================\n")
    
    def checkBalance(self):
        print("\n=========================\n")
        print(f"Balance 🏧\n")
        print(f"Current balance: ${self.balance}")
        print("\n=========================\n")
    
    def withdraw(self, amount):
        try:
            print("\n=========================\n")
            self.validationTransaction(amount)
            self.balance -= amount
            print("Withdraw 💸")
            print(f"Withdraw amount: ${amount}")
            print("\n=========================\n")
        except BalanceException as error:
            print(f"Transaction interrupted: \n{error}")
            print("=========================\n")


def start():
    print("\nWelcome To Repace Bank 😄\n")
    print("=========================\n")

    auth = input("Press 'Enter' to register ('L' for login) : ").lower()
    pincode = 0

    if auth == 'l':
        pincode = Auth.login()
    else:
        pincode = Auth.register()

    data = Auth.data[pincode]
    atm = Atm(data['username'], data['pincode'], data['balance'])

    depositOption = "Press 'd' to Deposit"
    balanceOption = "Press 'b' to Check Balance"
    withdrawOption = "Press 'w' to Withdraw"
    quitOption = "Press 'q' to Quit"
    option = "Option: "

    while True:
        confirmation = input(f"{depositOption}\n{balanceOption}\n{withdrawOption}\n{quitOption}\n{option}").lower()
        if confirmation == 'd':
            deposit = int(input("How much do you want to deposit: $"))
            atm.deposit(deposit)
        elif confirmation == 'b':
            atm.checkBalance()
        elif confirmation == 'w':
            withdraw = int(input("How much do you want to withdraw: $"))
            atm.withdraw(withdraw)
            pass
        elif confirmation == 'q':
            Auth.exit()
            break

start()