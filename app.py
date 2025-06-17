from fastapi import FastAPI, Query
from models.translator import Translator

app = FastAPI(title="PyVerb Translator API")
translator = Translator()

@app.get("/")
def root():
    return {"message": "Welcome to PyVerb – Hindi <-> English Translator"}

@app.get("/translate/en-hi")
def translate_en_hi(text: str = Query(..., description="Text in English")):
    translated = translator.en_to_hi(text)
    return {"input": text, "translated": translated, "direction": "English to Hindi"}

@app.get("/translate/hi-en")
def translate_hi_en(text: str = Query(..., description="Text in Hindi")):
    translated = translator.hi_to_en(text)
    return {"input": text, "translated": translated, "direction": "Hindi to English"}

