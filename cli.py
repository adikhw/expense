from datetime import datetime
from tracker import get_sorted_transactions, calculate_summary, find_transaction, delete_transaction

# Show transactions history
def show_history():
    transactions = get_sorted_transactions()

    if not transactions:
        print("No transactions found")
        return

    print(f"{'ID':>4}  {'Date':<10}  {'Type':<8}  {'Amount':>12}  {'Category':<12}  Note")
    print("-" * 65)

    for t in transactions:
        print(
            f"{t['id']:>4}  "
            f"{t['date']:<10}  "
            f"{t['type']:<8}  "
            f"{t['amount']:>12,}  "
            f"{t['category']:<12}  "
            f"{t['note']}"
        )

# Show transactions summary
def is_valid_month(text):
    try:
        parsed = datetime.strptime(text, "%Y-%m")
    except ValueError:
        return False
    return parsed.strftime("%Y-%m") == text

def show_summary():
    month_input = input("Month (YYYY-MM), leave blank for all: ").strip()
    if not month_input:
        month = None
    elif not is_valid_month(month_input):
        print("Wrong input format, use YYYY-MM")
        return
    else:
        month = month_input

    summary = calculate_summary(month)

    print("SUMMARY")
    print(f"Total income  : {summary['total_income']:>12,}")
    print(f"Total expense : {summary['total_expense']:>12,}")
    print(f"Balance       : {summary['balance']:>12,}")

    print("Expense per category:")
    if not summary['per_category']:
        print("No expenses yet")
    else:
        for category, total in summary['per_category'].items():
            print(f"{category:<12}  {total:>12,}")

# Delete menu
def delete_menu():
    id_input = input("ID to be deleted: ")

    try:
        transactions_id = int(id_input)
    except ValueError:
        print("ID must be a number")
        return

    t = find_transaction(transactions_id)
    if t is None:
        print("ID not found")
        return

    print(f"ID          : {t['id']}")
    print(f"Date        : {t['date']}")
    print(f"Type        : {t['type']}")
    print(f"Amount      : {t['amount']:,}")
    print(f"Category    : {t['category']}")
    print(f"Note        : {t['note']}")

    answer = input("Delete this transaction? y/n: ").strip().lower()

    if answer == "y":
        try:
            delete_transaction(transactions_id)
            print("Transaction deleted")
        except ValueError as e:
            print(e)

    else:
        print("Canceled")


# Input functions
def empty_input(prompt):
    while True:
        text = input(prompt).strip()

        if text:
            return text

        else:
            print("Input cannot be empty")

def get_positive_int(prompt):
    while True:
        raw = input(prompt).strip()

        try:
            number = int(raw)
        except ValueError:
            print("please enter a whole number")
            continue

        if number > 0:
            return number
        else:
            print("Number must be greater than 0")

def confirm_input(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please type y or n")
