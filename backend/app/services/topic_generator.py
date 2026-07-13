from transformers import pipeline, set_seed

# Load GPT-2 only once when the application starts
generator = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-medium"
)

# For reproducibility
set_seed(42)


def generate_conversation_starters(
    event_themes: list[str],
    user_interests: list[str]
) -> list[str]:

    themes = ", ".join(event_themes)

    interests = (
        ", ".join(user_interests)
        if user_interests
        else "General Networking"
    )

    prompt = f"""
Generate exactly 3 short professional networking conversation starters.
Themes: {themes}
Interests: {interests}
Conversation Starters:
1.
"""

    output = generator(
        prompt,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True,
        num_return_sequences=1,
        pad_token_id=generator.tokenizer.eos_token_id,
        eos_token_id=generator.tokenizer.eos_token_id
    )

    print(output)