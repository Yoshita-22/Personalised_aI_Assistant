# 🤝 Personalized Networking Assistant

An AI-powered web application that helps users generate personalized networking conversation starters based on an event description and their interests. The application also provides Wikipedia-based fact checking, conversation history, and user feedback logging to enhance the networking experience.

---

# 📌 Problem Statement

Professionals and students often find it difficult to initiate meaningful conversations during conferences, workshops, career fairs, and networking events. Existing networking tools provide generic suggestions that are not tailored to the event context or user interests. There is also no simple way to verify factual claims discussed during networking sessions.

---

# 💡 Proposed Solution

The Personalized Networking Assistant uses Artificial Intelligence to generate context-aware networking conversation starters. DistilBERT performs zero-shot classification to identify event themes, while Gemini generates engaging conversation starters. A Wikipedia-powered fact-checking module allows users to verify statements, and the application stores conversation history and user feedback for future reference.

---

# ✨ Features

- Generate personalized networking conversation starters
- Event theme extraction using DistilBERT Zero-Shot Classification
- AI-powered conversation generation using Gemini
- Wikipedia-based fact checking
- Conversation history logging
- User feedback logging (Like/Dislike)
- Interactive Streamlit frontend
- REST APIs using FastAPI
- Automated API testing using Pytest

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Programming Language | Python 3.11+ |
| Theme Extraction | DistilBERT (`typeform/distilbert-base-uncased-mnli`) |
| Conversation Generation | Gemini 2.5 Flash |
| Fact Checking | Wikipedia API |
| Data Storage | JSON (`history.json`, `feedback.json`) |
| API Testing | Pytest, FastAPI TestClient |
| HTTP Requests | Requests |
| Environment Variables | Python Dotenv |

---

# 📁 Project Structure

```
personalisedAIAssistant/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── data/
│   │   │   ├── history.json
│   │   │   └── feedback.json
│   │   │
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── conversation.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── request_response.py
│   │   │
│   │   ├── services/
│   │   │   ├── event_analyser.py
│   │   │   ├── topic_generator.py
│   │   │   ├── fact_checker.py
│   │   │   ├── history_logger.py
│   │   │   └── feedback_logger.py
│   │   │
│   │   ├── config.py
│   │   ├── main.py
│   │   └── .env
│   │
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_analyze_event.py
│   │   ├── test_fact_check.py
│   │   ├── test_routes.py
│   │   └── test_topic_generator.py
│   │
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   └── app.py
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/personalisedAIAssistant.git
```

---

## 2. Navigate to the Project

```bash
cd personalisedAIAssistant
```

---

## 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

---

## 4. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 6. Configure Environment Variables

Create a `.env` file inside

```
backend/app/
```


# 🚀 Running the Backend

Navigate to backend

```bash
cd backend
```

Start FastAPI

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🎨 Running the Frontend

Open another terminal

```bash
cd frontend
```

Run Streamlit

```bash
streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 🧪 Running Tests

Run all tests

```bash
pytest
```

Run a specific test

```bash
pytest tests/test_routes.py
```

---

# 📖 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/generate-conversation` | Generate networking conversation starters |
| POST | `/analyze-event` | Extract event themes |
| POST | `/fact-check` | Verify statements using Wikipedia |
| GET | `/history` | Retrieve previous conversations |
| POST | `/feedback` | Store user feedback |
| GET | `/feedback` | Retrieve feedback history |

---

# 🏗️ Project Workflow

```
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ├── Event Theme Extraction (DistilBERT)
   │
   ├── Conversation Generation (Gemini)
   │
   ├── Wikipedia Fact Checking
   │
   ├── History Logger
   │
   └── Feedback Logger
   │
   ▼
JSON Storage
```



# 📄 License

This project is developed for educational and learning purposes.
