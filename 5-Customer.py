import json
from datetime import datetime

class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print("Customer Information:")
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("TR ID Number:", self.tc_identification)
        print("Phone Number:", self.phone)

class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer.name, customer.surname, customer.tc_identification, customer.phone)
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit_money(self, amount):
        self.balance += amount
        self.add_transaction("Deposit", amount)
        print(f"Deposited {amount} TL successfully.")
        self.display_balance()

    def money_check(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.add_transaction("Withdrawal", amount)
            print(f"Withdrawn {amount} TL successfully.")
            self.display_balance()
        else:
            print("Insufficient balance. Transaction failed.")

    def display_balance(self):
        print(f"Current balance: {self.balance} TL")

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transaction_history.append(transaction)

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(f"Type: {transaction['type']}, Amount: {transaction['amount']} TL, Date: {transaction['date']}")

def save_to_json(accounts, filename):
    data = []
    for account in accounts:
        account_data = {
            "customer": {
                "name": account.customer.name,
                "surname": account.customer.surname,
                "tc_identification": account.customer.tc_identification,
                "phone": account.customer.phone
            },
            "account_number": account.account_number,
            "balance": account.balance,
            "transaction_history": account.transaction_history  # İşlem geçmişini de kaydet
        }
        data.append(account_data)
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Accounts saved to accounts.json.")

def load_from_json(filename):
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            accounts = []
            for item in data:
                customer = Customer(item["customer"]["name"], item["customer"]["surname"],
                                    item["customer"]["tc_identification"], item["customer"]["phone"])
                account = Account(customer, item["account_number"], item["balance"])
                account.transaction_history = item.get("transaction_history", [])  # Eksik anahtar için boş bir liste atama
                accounts.append(account)
        print("Accounts loaded from accounts.json.")
        return accounts
    except FileNotFoundError:
        print("No accounts.json file found. Starting with an empty list of accounts.")
        return []
    
def exit_program(accounts):
    print("Exiting the program.")
    save_to_json(accounts, "accounts.json")
    exit()

def find_account_by_customer(accounts, search_term):
    for account in accounts:
        if account.customer.name == search_term or account.customer.tc_identification == search_term:
            return account
    return None

# Load accounts from JSON file
accounts = load_from_json("accounts.json")

# Menu
def menu(accounts):
    while True:
        print("\n*** Bank Account Management System ***")
        print("1. Add Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Information")
        print("5. List Customers")
        print("6. Save Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer's name: ")
            surname = input("Enter customer's surname: ")
            tc_identification = input("Enter customer's TR ID number: ")
            phone = input("Enter customer's phone number: ")
            account_number = input("Enter account number: ")
            customer = Customer(name, surname, tc_identification, phone)
            account = Account(customer, account_number)
            accounts.append(account)
            print("Account added successfully.")

        elif choice == "2":
            search_term = input("Enter customer's name or TR ID number: ")
            account = find_account_by_customer(accounts, search_term)
            if account:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit_money(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            search_term = input("Enter customer's name or TR ID number: ")
            account = find_account_by_customer(accounts, search_term)
            if account:
                amount = float(input("Enter the amount to withdraw: "))
                account.money_check(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            search_term = input("Enter customer's name or TR ID number: ")
            account = find_account_by_customer(accounts, search_term)
            if account:
                account.display_information()
                account.display_balance()
                account.display_transaction_history()
            else:
                print("Account not found.")

        elif choice == "5":
            print("\n*** Customer List ***")
            for account in accounts:
                print(f"Name: {account.customer.name}, TR ID Number: {account.customer.tc_identification}, Account Number: {account.account_number}, Balance: {account.balance} TL")

        elif choice == "6":
            save_to_json(accounts, "accounts.json")
        elif choice == "7":
            exit_program(accounts)
        else:
            print("Invalid choice. Please enter a valid option.")

# Load accounts from JSON file
accounts = load_from_json("accounts.json")

# Menüyü çağır
menu(accounts)