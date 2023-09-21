class BankAccount:
    def __init__(self, acc_number, acc_holder_name, initial_balance):
        self.__account_number = acc_number
        self.__account_holder_name = acc_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid amount for deposit. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawn {amount} successfully.")
        elif amount <= 0:
            print("Invalid amount for withdrawal. Please enter a positive value.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: {self.__account_balance}")

# Create an instance of BankAccount
my_account = BankAccount("1234567890", "John Doe", 1000)

# Test deposit and withdrawal functionality
my_account.display_balance()  # Display initial balance

my_account.deposit(500)  # Deposit 500
my_account.display_balance()  # Display updated balance

my_account.withdraw(200)  # Withdraw 200
my_account.display_balance()  # Display updated balance

my_account.withdraw(1500)  # Try to withdraw more than balance
