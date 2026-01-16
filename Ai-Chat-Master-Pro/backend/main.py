import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Updated Imports: Using Google Gemini instead of OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory

# 1. Force load .env
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()

# 2. Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Initialize Gemini Brain
api_key = os.getenv("OPENAI_API_KEY") # Keep the variable name in .env or change to GEMINI_API_KEY

if api_key:
    print(f"✅ SUCCESS: Gemini API Key detected (Starts with: {api_key[:10]}...)")
else:
    print("❌ ERROR: No API Key found in .env file!")

# Initialize LLM with Gemini
# We use gemini-1.5-flash for the best balance of speed and intelligence
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-preview-09-2025", 
    google_api_key=api_key,
    temperature=0.7
)

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Ai-Chat-Master-Pro Gemini Edition is Online"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Predict uses memory to maintain the conversation context
        response = conversation.predict(input=request.message)
        return {"response": response}
    except Exception as e:
        error_msg = str(e)
        print(f"Server Error: {error_msg}")
        
        # Handle the specific API Key error for Gemini
        if "API_KEY_INVALID" in error_msg or "401" in error_msg:
            return {"response": "⚠️ Gemini Authentication Error: The API key provided is invalid."}
        
        return {"response": f"System Error: {error_msg}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)