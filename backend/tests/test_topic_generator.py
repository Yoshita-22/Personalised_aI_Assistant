from app.services.topic_generator import generate_conversation_starters
def test_topic_generator():
    themes = ["AI","Cities"]
    user_intersts = ["Technology"]
    topics = generate_conversation_starters(themes,user_intersts)
    assert isinstance(topics, list)
    assert len(topics) == 3
    assert all(isinstance(topic, str) for topic in topics)
    assert all(topic.strip() != "" for topic in topics)