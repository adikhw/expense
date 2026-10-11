from datetime import date, datetime
from storage import load_data, save_data

VALID_TYPE={"income", "expense"}

# Validation functions

def amount_validation(amount):
    """Validate the amount and return it as a positive integer.

    Raises:
        ValueError: If the amount is not an integer or is not greater than 0.
    """
    try:
        number = int(str(amount))
    except ValueError:
        raise ValueError("amount must be an integer")
    if number <= 0:
        raise ValueError("amount must be greater than 0")
    return number

def type_validation(transaction_type):
    """Normalize the transaction type and validate it.

    Returns:
        str: The normalized transaction type.

    Raises:
        ValueError: If the type is not income or expense.
    """
    transaction_type = transaction_type.strip().lower()

    if transaction_type not in VALID_TYPE:
        raise ValueError("type must be income or expense")
    return transaction_type

def category_validation(category):
    """Normalize the category and ensure it is not empty.

    Returns:
        str: The normalized category.

    Raises:
        ValueError: If the category is empty.
    """
    category = category.strip().lower()

    if not category:
        raise ValueError("category cannot be empty")
    return category

def date_validation(date_text):
    """Validate the date and return it in YYYY-MM-DD format.

    Returns:
        str: The validated date, or today's date if the input is empty.

    Raises:
        ValueError: If the date does not match the required format
        or represents an invalid date.
    """
    date_text = date_text.strip()

    if date_text == "":
        return date.today().isoformat()

    try:
        result = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("date format must be YYYY-MM-DD")

    return result.date().isoformat()

def is_valid_month(text):
    """Check whether the month matches the YYYY-MM format.

    Returns:
        bool: True if the month is valid, otherwise False.
    """
    try:
        parsed = datetime.strptime(text, "%Y-%m")
    except ValueError:
        return False
    return parsed.strftime("%Y-%m") == text

# Main functions
def add_transaction(date_text, transaction_type, amount, category, note):
    """Validate input, generate a new ID, and save a transaction.

    Args:
        date_text: The transaction date in YYYY-MM-DD format, or an empty string.
        transaction_type: The transaction type, either income or expense.
        amount: The transaction amount as a positive integer.
        category: The transaction category.
        note: An optional note describing the transaction.

    Raises:
        ValueError: If any validated input is invalid.
    """
    date_text = date_validation(date_text)
    transaction_type = type_validation(transaction_type)
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
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "note": note
    }

    data.append(transaction)
    save_data(data)

# History functions
def get_sorted_transactions():
    """Retrieve all transactions sorted by date and ID in descending order.

    Returns:
        list: A new list of transactions, with the newest first.
    """
    data = load_data()
    sorted_data = sorted(
        data,
        key=lambda item: (item["date"], item["id"]),
        reverse=True
    )
    return sorted_data

# Summary functions
def calculate_summary(month = None):
    """Calculate income, expenses, balance, and expenses per category.

    Args:
        month: An optional month in YYYY-MM format. None includes all data.

    Returns:
        dict: A dictionary containing total_income, total_expense,
        balance, and per_category. The per_category dictionary contains
        expense totals grouped by category.
    """
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

# Find function
def find_transaction(transaction_id): 
    """Find a transaction by its ID.

    Args:
        transaction_id: The ID of the transaction to find.

    Returns:
        dict: The matching transaction, or None if not found.
    """
    data = load_data()

    for t in data:
        if t['id'] == transaction_id:
            return t
    return None

# Delete function
def delete_transaction(transaction_id):
    """Delete a transaction by its ID and save the updated data.

    Args:
        transaction_id: The ID of the transaction to delete.

    Raises:
        ValueError: If the specified ID does not exist.
    """
    data = load_data()
    new_data = []
    found = False

    for t in data:
        if t['id'] == transaction_id:
            found = True
        else:
            new_data.append(t)

    if not found:
        raise ValueError("ID not found")

    save_data(new_data)
