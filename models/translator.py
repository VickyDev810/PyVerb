from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self):
        # English to Hindi
        self.en_hi_tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-hi')
        self.en_hi_model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-hi')

        # Hindi to English
        self.hi_en_tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-hi-en')
        self.hi_en_model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-hi-en')

    def en_to_hi(self, text: str) -> str:
        tokens = self.en_hi_tokenizer(text, return_tensors="pt", padding=True)
        translation = self.en_hi_model.generate(**tokens)
        return self.en_hi_tokenizer.decode(translation[0], skip_special_tokens=True)

    def hi_to_en(self, text: str) -> str:
        tokens = self.hi_en_tokenizer(text, return_tensors="pt", padding=True)
        translation = self.hi_en_model.generate(**tokens)
        return self.hi_en_tokenizer.decode(translation[0], skip_special_tokens=True)
