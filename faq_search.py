import json 
with open("faq_data.json") as f:
    faq_data = json.load(f)
        
def search_faq(user_question):
    for item in faq_data:
        if item["question"].lower() in user_question.lower():
            return item["answer"]
    return None            