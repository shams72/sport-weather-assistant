from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_message
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class ChatRequest(BaseModel):
    user_id: str
    user_message: str


@app.post("/chat")
async def chat(request: ChatRequest):

    result = await process_message(
        user_id=request.user_id,
        user_message=request.user_message
    )

    return {
        "response": result
    }
