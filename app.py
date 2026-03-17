from fastapi import FastAPI
from pydantic import BaseModel
from faq_search import search_faq
from ai_service import ask_ai
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    message: str
    
@app.get("/chat")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
def chat(req: ChatRequest):
        faq = search_faq(req.message)
    
        if faq:
            answer = ask_ai(faq, req.message)
            return{"answer": answer}
        return {"answer":"Please contact our Support."}
        