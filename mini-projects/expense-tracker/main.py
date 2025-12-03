from helpers import (
    add_expense,
    get_total,
    get_by_category,
    delete_expense,
    highest_expense,
    lowest_expense
)

def main():
    expenses = []    # list of dicts: {"amount": 100, "category": "Food"}

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Total expenditure")
        print("4. View expenses by category")
        print("5. Delete an expense")
        print("6. Highest expense")
        print("7. Lowest expense")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)
            print("Expense added!")

        elif choice == "2":
            print("\n--- All Expenses ---")
            for i, exp in enumerate(expenses):
                print(f"{i}. ₹{exp['amount']} - {exp['category']}")

        elif choice == "3":
            total = get_total(expenses)
            print(f"Total spent: ₹{total}")

        elif choice == "4":
            category = input("Enter category: ")
            result = get_by_category(expenses, category)
            print(f"\nExpenses in category '{category}':")
            for exp in result:
                print(f"₹{exp['amount']}")

        elif choice == "5":
            index = int(input("Enter index to delete: "))
            if delete_expense(expenses, index):
                print("Expense deleted!")
            else:
                print("Invalid index.")

        elif choice == "6":
            high = highest_expense(expenses)
            if high:
                print(f"Highest expense: ₹{high['amount']} ({high['category']})")
            else:
                print("No expenses yet.")

        elif choice == "7":
            low = lowest_expense(expenses)
            if low:
                print(f"Lowest expense: ₹{low['amount']} ({low['category']})")
            else:
                print("No expenses yet.")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
