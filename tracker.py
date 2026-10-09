from datetime import date, datetime
from storage import load_data, save_data

VALID_TYPE= {"income", "expense"}

# validation
def amount_validation(amount):
    try:
        number = int(amount)
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


