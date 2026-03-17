from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Groq_API_KEY"))

def ask_ai(context, question):
    prompt = f""""
    You are a FAQ assistant.

Only answer from the FAQ context.
If the answer is not in the context say:
"Sorry! Sir, Please contact  our Support."
    
    FAQ:
    {context}
    
    User Question:
    {question}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
    