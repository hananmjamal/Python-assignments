def record_expense():
    category = input("Enter the expense category: ")
    amount = int(input("Enter the expense amount: "))
    date = input("Enter the date of expense (DD-MM-YYYY): ")

    file = open("expenses.txt", "a")
    file.write(f"{category} {amount} {date}\n")
    file.close()
    print("Expense recorded successfully!\n")


def show_expenses():
    print("\n--- All Expenses ---")
    file = open("expenses.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
    print("-------------------\n")


def calculate_total():
    total_amount = 0
    file = open("expenses.txt", "r")
    for line in file:
        data = line.split()
        total_amount += int(data[1])
    file.close()
    print(f"Total expenses so far: {total_amount}\n")


while True:
    print("Expense Tracker Menu:")
    print("1 = Add a new expense")
    print("2 = View all expenses")
    print("3 = Calculate total expenses")
    print("4 = Exit\n")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        print("Adding a new expense...\n")
        record_expense()
    elif user_choice == 2:
        print("Listing all expenses...\n")
        show_expenses()
    elif user_choice == 3:
        print("Calculating total expenses...\n")
        calculate_total()
    elif user_choice == 4:
        print("Thank you for using the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
