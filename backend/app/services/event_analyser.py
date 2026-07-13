from transformers import pipeline

# Load once when the application starts
classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

DEFAULT_LABELS = [
    "Artificial Intelligence",
    "Machine Learning",
    "Healthcare",
    "Blockchain",
    "Cybersecurity",
    "Education",
    "Finance",
    "Cloud Computing",
    "Sustainability",
    "Robotics",
    "Data Science",
    "Internet of Things"
]


def extract_event_themes(
    event_description: str,
    user_interests: list[str] | None = None
) -> list[str]:

    labels = user_interests or DEFAULT_LABELS

    result = classifier(
        event_description,
        candidate_labels=labels,
        multi_label=True
    )

    return result["labels"][:3]