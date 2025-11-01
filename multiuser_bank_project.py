class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: ₹{self.balance}")


def main():
    print("🏦 Welcome to the Mini Banking System (Multi-Account)")
    accounts = {}

    while True:
        print("\n🔐 Main Menu")
        print("1. Create new account")
        print("2. Access existing account")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            name = input("Enter your name: ")
            if name in accounts:
                print("⚠️ Account with this name already exists.")
            else:
                accounts[name] = BankAccount(name)
                print("✅ Account created successfully.")

        elif choice == '2':
            name = input("Enter your name: ")
            if name in accounts:
                account = accounts[name]
                while True:
                    print(f"\n💼 Welcome {name}")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    sub_choice = input("Choose an option (1-4): ")

                    if sub_choice == '1':
                        amount = float(input("Enter amount to deposit: ₹"))
                        account.deposit(amount)

                    elif sub_choice == '2':
                        amount = float(input("Enter amount to withdraw: ₹"))
                        account.withdraw(amount)

                    elif sub_choice == '3':
                        account.check_balance()

                    elif sub_choice == '4':
                        print("Logging out...")
                        break

                    else:
                        print("❌ Invalid option.")
            else:
                print("⚠️ No account found with that name.")

        elif choice == '3':
            print("👋 Thank you for using the banking system. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")

main()
