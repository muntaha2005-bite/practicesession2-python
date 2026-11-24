expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append(amount)
        print(name, "added successfully!")

    elif choice == "2":
        print("Your expenses:", expenses)

    elif choice == "3":
        print("Total spending:", sum(expenses))

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")