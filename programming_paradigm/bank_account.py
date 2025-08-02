class BankAccount:
    def _init_(self, account_balance = 0):
        self.account_balance = account_balance
    def deposit (self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    def withdraw (self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

import sys
from bank_account import BankAccount
def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> [amount] [initial_balance]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
        print(f"Withdrew: ${amount}")
    else:
        print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if _name_ == "_main_":
    main()
    




    
