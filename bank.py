class BankAccount:
    
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully!")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Invalid Amount!")
        else:
            self.balance -= amount
            print("Amount Withdrawn Successfully!")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Current Balance: ₹", self.balance)


# Dictionary to store multiple accounts
accounts = {}

while True:
    print("\n----- BANKING SYSTEM -----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        acc_no = input("Enter Account Number: ")
        accounts[acc_no] = BankAccount(name, acc_no)
        print("Account Created Successfully!")

    elif choice == "2":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter Amount to Deposit: "))
            accounts[acc_no].deposit(amount)
        else:
            print("Account Not Found!")

    elif choice == "3":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter Amount to Withdraw: "))
            accounts[acc_no].withdraw(amount)
        else:
            print("Account Not Found!")

    elif choice == "4":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            accounts[acc_no].check_balance()
        else:
            print("Account Not Found!")

    elif choice == "5":
        print("Thank You for Using Banking System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
