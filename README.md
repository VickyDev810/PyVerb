# 🔊 PyVerb — Your Own Local Google Translator 🧠⚡

Forget laggy APIs and limited usage quotas. **PyVerb** is your **blazing-fast, offline-capable language translator**, powered by Hugging Face Transformers and FastAPI.  
It translates between **Hindi 🇮🇳 and English 🇬🇧** faster than you can say _"Namaste, world!"_

## 🚀 Features

- 🔁 **Bi-directional translation** (English ↔ Hindi)
- 🧠 Powered by **Hugging Face MarianMT** models
- ⚡ FastAPI backend for low-latency translation
- 🛡️ 100% local — privacy-respecting and quota-free
- 🧰 Ready to extend for other languages

## 🌐 Supported Languages

PyVerb uses the MarianMT model family by Helsinki-NLP. You can explore **all supported language pairs** here:  
👉 [HuggingFace - MarianMT Language Pairs](https://huggingface.co/Helsinki-NLP)

Currently implemented:

- English → Hindi (`en-hi`)
- Hindi → English (`hi-en`)

Want more languages? Just plug them in — PyVerb is built for modular growth.

---

## 📦 Installation

```bash
git clone https://github.com/VickyDev810/PyVerb.git
cd PyVerb
pip install -r requirements.txt
````

---

## 🧪 Usage

### 🔧 Run the API

```bash
uvicorn app:app --reload
```

### 🔍 Translate Text

#### English ➡ Hindi

```http
GET /translate/en-hi?text=How are you?
```

#### Hindi ➡ English

```http
GET /translate/hi-en?text=आप कैसे हैं?
```

📨 **Sample Response:**

```json
{
  "input": "आप कैसे हैं?",
  "translated": "How are you?",
  "direction": "Hindi to English"
}
```

---

## 🗂️ Project Structure

```
PyVerb/
├── app.py                  # FastAPI app
├── models/
│   └── translator.py       # Translation logic
├── README.md               # This hot doc
└── requirements.txt        # Dependencies
```

---

## 🛠️ Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [Transformers](https://huggingface.co/transformers/)
* [Helsinki-NLP MarianMT Models](https://huggingface.co/Helsinki-NLP)

---

## 💡 Tip

Want to make PyVerb your own offline Google Translate box?
🔌 Add more models, build a frontend, or containerize it with Docker. Sky’s the limit.

---

## 🧠 License

MIT — because good tools should be free and badass.

---
