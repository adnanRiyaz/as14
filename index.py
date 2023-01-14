class Bank:
    def __init__(self,iamount=0.00):
        self.balance=iamount
    def log_transac(self,transac_str):
        with open("transac.txt","a") as file:
            file.write(f"{transac_str} \t\t\tBalance: {self.balance}\n")
    def withdrawal(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount =0
        if amount:
            self.balance = self.balance - amount
            self.log_transac(f"Withdraw ${amount}")

    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount =0
        if amount:
            self.balance = self.balance + amount
            self.log_transac(f"Deposited ${amount}")
account = Bank(50.50)

while True:
    try:
        action = input("What kind of action do you want?")
    except KeyboardInterrupt:
        print("\n Leaving the ATM \n")
    if action in ["withdrawal","deposit"]:
        if action =="withdrawal":
            amount = input("Enter amount to withdraw :")
            account.withdrawal(amount)
        else:
            amount = input("Enter amount to deposit :")
            account.deposit(amount)
        print("Available Balance :",account.balance)
    else:
        print("That is not the valid Input!")
account.deposit(10)
print(account.balance)
account.withdrawal(14.75)
print(account.balance)