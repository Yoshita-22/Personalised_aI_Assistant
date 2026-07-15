from unittest.mock import patch, MagicMock

from app.services.fact_checker import fact_check


@patch("app.services.fact_checker.requests.get")
def test_fact_check_success(mock_get):

    # Fake response for first API call (search)
    search_response = MagicMock()
    search_response.json.return_value = {
        "query": {
            "search": [
                {
                    "title": "Python (programming language)"
                }
            ]
        }
    }

    # Fake response for second API call (summary)
    summary_response = MagicMock()
    summary_response.json.return_value = {
        "extract": "Python is a high-level programming language."
    }

    # First requests.get() returns search_response
    # Second requests.get() returns summary_response
    mock_get.side_effect = [
        search_response,
        summary_response
    ]

    result = fact_check("Python")

    assert result == {
        "verification_status": "Information Retrieved",
        "summary": "Python is a high-level programming language."
    }