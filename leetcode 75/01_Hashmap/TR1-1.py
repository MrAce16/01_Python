# select CONCAT (col1, col2) as 
# combined_colum
# from <employee_data>
# where id = 2351;


# string = "hi i am an python developer"
# vowels = "aeiou"
# count = 0

# for i in string:
#     if i.lower() in vowels:
#         count +=1
# print(" number of vowels", count)

# create trigger set_order 
# before insert on orders
# for each row
# execuete function update_order();

'''Write a Python program that simulates a simple banking system with the following functionalities:     

Create an account.     

Check balance.     

Deposit money.     

Withdraw money.     

Exit the program. 

Requirements:     

Each account should have an account number and a balance.     Implement input validation (e.g., check for sufficient balance during withdrawals).'''

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
    

    def deposit(self, amount):
        self.amount = amount
    

    def check_balance(self, balance):
        self.balance = balance

        print(f"current balance is :{self.balance}")
    

    def main():
        print("welcome to simple banking system")1

        account_number = input("enter the account number")

        account = BankAccount(account_number)

        while True:
            print("\n choose an option")
            print("1. deposite")
            print("2. withdrawl")
            print("3. check balance")
            print("4. exit")

            choice = input("Enter the menu")

            if choice ==1:
                amount = float(input("Enter the deposite amount"))
                account.deposit (amount)
            
            elif choice ==4:
                print("Thanking you for banking with us")

    if __name__ =="__main__":
        main()

    