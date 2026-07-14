from fastapi import APIRouter
from app.schemas.request_response import ConversationRequest,ConversationResponse,FactCheckRequest,FeedbackRequest,FactCheckResponse
from app.services.event_analyser import extract_event_themes
from app.services.topic_generator import generate_conversation_starters
from app.services.fact_checker import fact_check
from app.services.history_logger import log_conversation,load_history
from app.services.feedback_logger import log_feedback,load_feedback
router = APIRouter()

@router.post("/analyze-event")
def analyse_event(request: ConversationRequest):
     themes = extract_event_themes(
        request.event_description,request.user_interests
    )
     return {"topics":themes}

@router.post("/generate-conversation",response_model=ConversationResponse)
def generate(request: ConversationRequest):
   
    themes = extract_event_themes(
        request.event_description,request.user_interests
    )
    # Pass themes to GPT-2
    conversation_starters =  generate_conversation_starters(themes,request.user_interests)
    #log to json file
    log_conversation({
        "user_interests":request.user_interests,
        "event-desc":request.event_description,
        "themes":themes,
        "conversation_Starters":conversation_starters
    })
    return {
        "themes":themes,
        "conversation_starters":conversation_starters
    }

    
@router.post("/fact-check",response_model=FactCheckResponse)
def fackChecker(request:FactCheckRequest):
    summary = fact_check(request.input_text)
    return summary

@router.post("/feedback")
def save_feedback(request: FeedbackRequest):

    log_feedback(
        request.suggestion,
        request.action
    )

    return {
        "message": "Feedback saved."
    }
@router.get("/feedback")
def get_feedback():
    feedback = load_feedback()
    return feedback
@router.get("/history")
def get_history():
    history = load_history()
    return history

    