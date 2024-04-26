# Question 5
class Customer:
    def __init__(self, name, surname, id_number, phone):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.phone = phone

    def show_info(self):
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("ID Number:", self.id_number)
        print("Phone Number:", self.phone)

class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer.name, customer.surname, customer.id_number, customer.phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("{} deposited.".format(amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("{} withdrawn.".format(amount))
        else:
            print("Insufficient balance. Transaction failed.")

    def show_balance(self):
        print("Account Balance:", self.balance)

# Create instances of Customer and Account
customer = Customer("Ali", "Veli", "12345678900", "5551234567")
account = Account(customer, "123456789", 1000)

# Display customer information
customer.show_info()

# Deposit into account
account.deposit(500)
account.show_balance()

# Withdraw from account
account.withdraw(200)
account.show_balance()

# Attempt to withdraw with insufficient balance
account.withdraw(2000)