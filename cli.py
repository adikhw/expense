from tracker import get_sorted_transactions, calculate_summary, find_transaction, delete_transaction, add_transaction, is_valid_month

# Style helper
def print_title(text):
    """Display a centered title with separator lines."""
    print()
    print(f" {text} ".center(40, "="))
    print()


# Input functions
def get_non_empty_input(prompt):
    """Prompt repeatedly until the user enters non-empty text.

    Args:
        prompt: The message displayed to the user.

    Returns:
        str: The non-empty input with surrounding whitespace removed.
    """
    while True:
        text = input(prompt).strip()

        if text:
            return text

        else:
            print("Input cannot be empty")

def get_positive_int(prompt):
    """Prompt repeatedly until the user enters a positive integer.

    Args:
        prompt: The message displayed to the user.

    Returns:
        int: The validated positive integer.
    """
    while True:
        raw = input(prompt).strip()

        try:
            number = int(raw)
        except ValueError:
            print("Please enter a whole number")
            continue

        if number > 0:
            return number
        else:
            print("Number must be greater than 0")

def confirm_input(prompt):
    """Prompt until the user confirms with y or n.

    Args:
        prompt: The confirmation message displayed to the user.

    Returns:
        bool: True for y and False for n.
    """
    while True:
        answer = input(prompt).strip().lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please type y or n")


# Show transaction history
def show_history():
    """Display all transactions sorted from newest to oldest."""
    transaction = get_sorted_transactions()

    if not transaction:
        print("No transaction found")
        return

    print(f"{'ID':>4}  {'Date':<10}  {'Type':<8}  {'Amount':>12}  {'Category':<12}  Note")
    print("-" * 65)

    for t in transaction:
        print(
            f"{t['id']:>4}  "
            f"{t['date']:<10}  "
            f"{t['type']:<8}  "
            f"{t['amount']:>12,}  "
            f"{t['category']:<12}  "
            f"{t['note']}"
        )

# Show transaction summary

def show_summary():
    """Display income, expenses, balance, and expense totals by category.

    The user can optionally filter the summary by month.
    """
    month_input = input("Month (YYYY-MM), leave blank for all: ").strip()
    if not month_input:
        month = None
    elif not is_valid_month(month_input):
        print("Wrong input format, use YYYY-MM")
        return
    else:
        month = month_input

    summary = calculate_summary(month)

    print()
    print("SUMMARY")
    print("-" * 28)
    print(f"Total income  : {summary['total_income']:>12,}")
    print(f"Total expense : {summary['total_expense']:>12,}")
    print(f"Balance       : {summary['balance']:>12,}")
    print("-" * 28)

    print()
    print("Expense per category:")
    if not summary['per_category']:
        print("No expenses yet")
    else:
        for category, total in summary['per_category'].items():
            print(f"{category:<12}  {total:>12,}")

# Delete menu
def delete_menu():
    """Find a transaction, display its details, and ask for deletion confirmation."""
    id_input = input("ID to be deleted: ")

    try:
        transaction_id = int(id_input)
    except ValueError:
        print("ID must be a number")
        return

    t = find_transaction(transaction_id)
    if t is None:
        print("ID not found")
        return

    print()
    print(f"ID          : {t['id']}")
    print(f"Date        : {t['date']}")
    print(f"Type        : {t['type']}")
    print(f"Amount      : {t['amount']:,}")
    print(f"Category    : {t['category']}")
    print(f"Note        : {t['note']}")
    print()
    

    if confirm_input("Delete this transaction? y/n: "):
        try:
            delete_transaction(transaction_id)
            print("Transaction deleted")
        except ValueError as error:
            print(error)

    else:
        print("Canceled")

# Add menu functions
def add_menu():
    """Prompt for transaction details and submit a new transaction."""
    print_title("ADD TRANSACTION")

    date_text = input("Date (YYYY-MM-DD, empty = today): ")
    transaction_type = input("Type (income/expense): ")
    amount = get_positive_int("Amount: ")
    category = get_non_empty_input("Category: ")
    note = input("Note (optional): ")

    print()
    try:
        add_transaction(date_text, transaction_type, amount, category, note)
        print("Transaction added")
    except ValueError as error:
        print(error)

# Main menu
def main_menu():
    """Display the main menu and handle choices until the user exits."""
    while True:
        print_title("EXPENSE TRACKER")
        print(
            "1. Add transaction",
            "\n2. Show history",
            "\n3. Show summary",
            "\n4. Delete transaction",
            "\n5. Exit"
        )
        print()

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                add_menu()
            elif choice == "2":
                show_history()
            elif choice == "3":
                show_summary()
            elif choice == "4":
                delete_menu()
            elif choice == "5":
                print("Goodbye!")
                return
            
            else:
                print("Invalid choice, please enter 1-5")
        except ValueError as err:
            print("Error:", err)
