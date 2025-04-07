
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    if amount > self.balance:
      return 'Not enough funds!'
    else:
      self.balance = self.balance - amount
      return amount

  def display_balance(self):
    print('Your balance is: $' + str(self.balance))
   
my_bank = BankAccount('Olesya', 'Kuz', 12345, 'saving', 1234, 0.0)

my_bank.deposit(96)
my_bank.withdraw(25)
my_bank.display_balance()