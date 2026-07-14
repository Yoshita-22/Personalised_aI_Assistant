import json
from pathlib import Path
from datetime import datetime

# Path to history.json
HISTORY_FILE = Path("app/data/history.json")


def log_conversation(data: dict) -> None:
    """
    Saves a conversation into history.json.
    """

    # Add timestamp
    data["timestamp"] = datetime.now().isoformat()

    # Read existing history
    if HISTORY_FILE.exists():

        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            history = json.load(file)

    else:
        history = []

    # Append new conversation
    history.append(data)

    # Write updated history
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def load_history() -> list:
    """
    Returns all previous conversations.
    """

    if not HISTORY_FILE.exists():
        return []

    with HISTORY_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)
        