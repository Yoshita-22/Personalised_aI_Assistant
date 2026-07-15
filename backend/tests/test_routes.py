from unittest.mock import patch, MagicMock
import requests
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)



@patch("app.routers.conversation.log_conversation")
@patch("app.routers.conversation.generate_conversation_starters")
@patch("app.routers.conversation.extract_event_themes")
def test_generate_conversation_success(
    mock_extract,
    mock_generate,
    mock_log
):

    mock_extract.return_value = [
        "Technology",
        "Networking"
    ]

    mock_generate.return_value = [
        "What projects are you working on?",
        "which technology excites you most?",
        "How can we build valuable connections?"
    ]

    response = client.post(
        "/generate-conversation",
        json={
            "event_description":"AI Conference",
            "user_interests":["Machine Learning",]
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["themes"] == [
        "Technology",
        "Networking"
    ]

    assert body["conversation_starters"] == [
        "What projects are you working on?",
        "which technology excites you most?",
        "How can we build valuable connections?"
    ]
@patch("app.routers.conversation.fact_check")
def test_fact_check_success(mock_fact):

    mock_fact.return_value = {
        "verification_status":"Information Retrieved",
        "summary":"Python is a programming language."
    }

    response = client.post(
        "/fact-check",
        json={
            "input_text":"Python"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "verification_status":"Information Retrieved",
        "summary":"Python is a programming language."
    }
