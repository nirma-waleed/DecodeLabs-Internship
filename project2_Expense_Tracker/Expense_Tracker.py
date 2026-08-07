
print("===================================")
print("      EXPENSE TRACKER")
print("===================================")

total = 0
expenses = []

print("\nEnter your expenses one by one.")
print("Type 'quit' (any capitalization) when you are finished.")

while True:

    user_input = input("Enter expense (or type 'quit' to finish): ").strip()

    if user_input.lower() == "quit":
        break

    try:
        expense = int(user_input)

        if expense < 0:
            print("Expense cannot be negative.\n")
            continue

        expenses.append(expense)
        total += expense

        print("Expense added successfully!")
        print(f"Current Total: Rs. {total}")

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
print("\n===================================")
print("      EXPENSE SUMMARY")
print("===================================")

if len(expenses) == 0:
    print("No expenses were entered.")
else:
    print("\nExpenses Entered:\n")

    for index, amount in enumerate(expenses, start=1):
        print(f"{index}. Rs. {amount}")

    highest = max(expenses)
    lowest = min(expenses)
    average = total / len(expenses)

    print(f"\nTotal Transactions : {len(expenses)}")
    print(f"Highest Expense    : Rs. {highest}")
    print(f"Lowest Expense     : Rs. {lowest}")
    print(f"Average Expense    : Rs. {average:.2f}")
    print(f"Total Spent        : Rs. {total}")

print("\nExpense tracking completed successfully!")
print("Thank you for using Expense Tracker!")
print("===================================")