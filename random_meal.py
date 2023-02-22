import json
import random
from pathlib import Path

PATH = Path(__file__).parent
RECEIPT_FILE = "receipts.json"
FIRST_INDENTATION = "    "
SECOND_INDENTATION = 2 * FIRST_INDENTATION


def _read_json(file_path: Path):
    with open(file_path) as f:
        data = json.load(f)
        return data


def _randomizer(meals: list):
    return random.choice(meals)


def main():
    data = _read_json(PATH / RECEIPT_FILE)
    meal = _randomizer(list(data.keys()))
    print(meal)
    for key, value in data[meal].items():
        if not isinstance(value, dict):
            print(f"{FIRST_INDENTATION}{key}: {value}")
        else:
            print(f"{FIRST_INDENTATION}{key}:")
            for ingredient, quantity in value.items():
                print(f"{SECOND_INDENTATION}{ingredient}: {quantity}")


main()
