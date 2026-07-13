from fastapi import APIRouter
from app.schemas.request_response import ConversationRequest,ConversationResponse,FactCheckRequest,FactCheckResponse
from app.services.event_analyser import extract_event_themes
from app.services.topic_generator import generate_conversation_starters
from app.services.fact_checker import fact_check
router = APIRouter()

@router.post("/generate-conversation")
def generate(request: ConversationRequest):

    themes = extract_event_themes(
        request.event_description,request.user_interests
    )

    print(themes)

    # Pass themes to GPT-2
    conversation_starters =  generate_conversation_starters(themes,request.user_interests)
    print(conversation_starters)
@router.post("/fact-check",response_model=FactCheckResponse)
def fackChecker(request:FactCheckRequest):
    summary = fact_check(request.input_text)
    return summary

    