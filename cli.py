from datetime import datetime
from tracker import get_sorted_transactions, calculate_summary

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
