from app.services.event_analyser import extract_event_themes


def test_returns_list():
    themes = extract_event_themes(
        "AI conference discussing large language models."
    )

    assert isinstance(themes, list)
    assert(len(themes))>0