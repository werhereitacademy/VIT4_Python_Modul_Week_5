  

class Customer:
    
    def __init__(self, fname, lname, ID_number, phone):

        self.name = fname
        self.lastname = lname
        self.ID_number = ID_number
        self.phone = phone

    def display_customer_info(self):
        print("Customer Information:")
        print("Name:", self.name)
        print("Surname:", self.lastname)
        print("TC ID:", self.ID_number)
        print("Phone:", self.phone)





class Account(Customer):
    
    def __init__(self, customer, iban, balance=0):
        super().__init__(customer.name, customer.lastname, customer.ID_number, customer.phone)

        self.customer = customer
        self.balance = balance
        self.iban = iban

    def display_balance(self):
        print(f"Account Balance: {self.balance} TL")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} TL to the account.")
        self.display_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} TL from the account.")
        else:
            print("Insufficient balance. Withdrawal unsuccessful.")
            
        self.display_balance()

customer1 = Customer("Mehmet", "Gunes", "39767346864", "05458374756")

account1 = Account(customer1, "TR9837645864", 2000)

customer1.display_customer_info()

account1.display_balance()

account1.deposit(455)

account1.withdraw(650)