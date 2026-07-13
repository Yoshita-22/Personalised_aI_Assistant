from fastapi import FastAPI
from .routers import conversation
app = FastAPI()

@app.get("/")
def health():
    return {
        "status": "Server is running"
    }
app.include_router(conversation.router)