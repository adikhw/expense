from datetime import date, datetime
from storage import load_data, save_data

VALID_TYPE={"income", "expense"}

# Validation functions
def amount_validation(amount):
    try:
        number = int(str(amount))
    except ValueError:
        raise ValueError("amount must be an integer")
    if number <= 0:
        raise ValueError("amount must be greater than 0")
    return number

def type_validation(transactions_type):
    transactions_type = transactions_type.strip().lower()

    if transactions_type not in VALID_TYPE:
        raise ValueError("type must be income or expense")
    return transactions_type

def category_validation(category):
    category = category.strip().lower()

    if not category:
        raise ValueError("category cannot be empty")
    return category

def date_validation(date_text):
    date_text = date_text.strip()

    if date_text == "":
        return date.today().isoformat()

    try:
        result = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("date format must be YYYY-MM-DD")

    return result.date().isoformat()

# Main functions
def add_transaction(date_text, transactions_type, amount, category, note):
    date_text = date_validation(date_text)
    transactions_type = type_validation(transactions_type)
    amount = amount_validation(amount)
    category = category_validation(category)
    note = note.strip()

    data = load_data()

    if not data:
        new_id = 1
    else:
        new_id = max(item["id"] for item in data) + 1    

    transaction = {
        "id": new_id,
        "date": date_text,
        "type": transactions_type,
        "amount": amount,
        "category": category,
        "note": note
    }

    data.append(transaction)
    save_data(data)

# History functions
def get_sorted_transactions():
    data = load_data()
    sorted_data = sorted(
        data,
        key=lambda item: (item["date"], item["id"]),
        reverse=True
    )
    return sorted_data

# Summary functions
def calculate_summary(month = None):
    data = load_data()

    if month is not None:
        data = [
            t for t in data
            if t["date"][:7] == month
        ] # Month format "YYYY-MM"

    total_income = 0
    total_expense = 0 
    per_category = {} # Key: category, value: total expense

    for t in data:
        if t["type"] == "income":
            total_income = total_income + t["amount"]
        elif t["type"] == "expense":
            total_expense = total_expense + t["amount"]

            if t["category"] not in per_category:
                per_category[t["category"]] = 0

            per_category[t["category"]] = per_category[t["category"]] + t["amount"]

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "per_category": per_category
    }

