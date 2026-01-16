import os
import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# --- IMPORTS ---
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load Keys
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()

# 2. CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Setup AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ CRITICAL ERROR: GOOGLE_API_KEY not found in .env")
    sys.exit(1)

# Initialize Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=api_key,
    temperature=0.7
)

# 4. Chat Logic
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant named Ai-Chat-Master-Pro."),
    ("human", "{input}"),
])

chain = prompt | llm | StrOutputParser()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Ai-Chat-Master-Pro (New Backend) is Online"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = chain.invoke({"input": request.message})
        return {"response": response}
    except Exception as e:
        return {"response": f"⚠️ Error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)