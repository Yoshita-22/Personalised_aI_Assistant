import json
from pathlib import Path
from datetime import datetime

# Path to feedback.json
FEEDBACK_FILE = Path("app/data/feedback.json")


def log_feedback(suggestion: str, action: str) -> None:
    """
    Saves user feedback for a conversation starter.
    """

    feedback_entry = {
        "suggestion": suggestion,
        "action": action,
        "timestamp": datetime.now().isoformat()
    }

    # Read existing feedback
    if FEEDBACK_FILE.exists():

        with FEEDBACK_FILE.open("r", encoding="utf-8") as file:
            feedback = json.load(file)

    else:
        feedback = []

    # Append new feedback
    feedback.append(feedback_entry)

    # Write updated feedback
    with FEEDBACK_FILE.open("w", encoding="utf-8") as file:
        json.dump(feedback, file, indent=4)


def load_feedback() -> list:
    """
    Returns all stored feedback.
    """

    if not FEEDBACK_FILE.exists():
        return []

    with FEEDBACK_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)