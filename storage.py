import json
from pathlib import Path

DATA_FILE = Path("data") / "transactions.json"

def load_data():

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
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)