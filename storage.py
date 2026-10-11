import json
from pathlib import Path

DATA_FILE = Path("data") / "transactions.json"

def load_data():
    """
    Read all transactions from a JSON file.
    returns: 
        list: A list of transactions.

    notes: 
        Return [] if the file does not exist, is empty, is corrupted,
        or contains valid JSON that is not a list.
    """
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE ,"r") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except json.JSONDecodeError:
        return []

def save_data(data):
    """
    Write a list of transactions to a JSON file.
    
    args: 
        data: data (list of transactions).
        
    notes: 
        Create the data/ directory if it does not exist, and
        OVERWRITE the existing file contents.
    """
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)