class BalanceSheet:

    def __init__(self):
        self.assets = {}
        self.liabilities = {}
        self.equity = {}

    def add_entry(self, category, name, amount):
        if category == "assets":
            self.assets[name] = self.assets.get(name, 0) + amount
        elif category == "liabilities":
            self.liabilities[name] = self.liabilities.get(name, 0) + amount
        elif category == "equity":
            self.equity[name] = self.equity.get(name, 0) + amount
        else:
            print("Invalid category. Please use 'assets', 'liabilities', 'equity'")
            return  # Exit the method if an invalid category is entered

        print(f"{amount} added to {category} '{name}'")

    def view_balance_sheet(self):
        print("\nBalance Sheet:")
        print("Assets:")
        for name, amount in self.assets.items():
            print(f"{name}: {amount}")

        print("Liabilities:")
        for name, amount in self.liabilities.items():
            print(f"{name}: {amount}")

        print("Equity:")
        for name, amount in self.equity.items():
            print(f"{name}: {amount}")

        self.check_balance()

    def check_balance(self):
        total_assets = sum(self.assets.values())
        total_liabilities = sum(self.liabilities.values())
        total_equity = sum(self.equity.values())

        print(f"Total Assets: {total_assets}")
        print(f"Total Liabilities: {total_liabilities}")
        print(f"Total Equity: {total_equity}")

        if total_assets == total_liabilities + total_equity:
            print("The Balance Sheet Balances.")
        else:
            print("The balance sheet is not balanced.")

def main():
    bs = BalanceSheet()

    while True:
        print("\nBalance Sheet Management System")
        print("1. Add Asset")
        print("2. Add Liability")
        print("3. Add Equity")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter asset name: ")
            amount = float(input("Enter amount: "))
            bs.add_entry("assets", name, amount)

        elif choice == "2":
            name = input("Enter liability name: ")
            amount = float(input("Enter amount: "))
            bs.add_entry("liabilities", name, amount)

        elif choice == "3":
            name = input("Enter equity name: ")
            amount = float(input("Enter amount: "))
            bs.add_entry("equity", name, amount)

        elif choice == "4":
            bs.view_balance_sheet()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
