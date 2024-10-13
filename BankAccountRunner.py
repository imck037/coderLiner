class Bank():
    def __init__(self, account, balance) -> None:
        self.account = account
        self.balance = balance
        print(f"Account: {self.account}\nBalance: {self.balance}")

    def deposit(self, ammount):
        self.balance = self.balance + ammount
        print(f"Deposit of {ammount} to {self.account} successful.\nTotal balance: {self.balance:,}")
        
    def withdraw(self, ammount):
        if ammount < self.balance:
            self.balance = self.balance - ammount
            print(f"Withdrawal of {ammount} from {self.account} successful.\nTotal balance: {self.balance:,}")
        else:
            print(f"The ammount of withdrawal is greater the balance.")

    def transfer(self, ammount, account):
        if ammount < self.balance:
            account.deposit(ammount)
            self.balance = self.balance - ammount
            print(f"Transfer to {account.account} from {self.account} successful.\nTotal ammount: {self.balance}")
        else:
            print("The ammount is less than the balance.")

    def __str__(self):
        return f"Account name: {self.account}, balance: {self.balance}"


people1 = Bank("labKumar", 34000)
people2 = Bank("kushKumar", 8200)

people2.deposit(5000)
people2.withdraw(4000)
people2.transfer(10000, people1)

print(people1)
print(people2)