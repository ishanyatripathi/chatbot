# 🤖 CLI Chatbot – flan-t5-base

This is a command-line chatbot built using the `google/flan-t5-base` model from Hugging Face. It runs entirely offline (no API), answers factual questions, and is built in modular Python code — ideal for internship projects or lightweight AI demos.

---

## 📂 Project Structure

chatbot/
├── model_loader.py      # Loads the flan-t5-base model using Hugging Face Transformers
├── interface.py         # Command-line chatbot loop
├── requirements.txt     # Required Python libraries
├── .gitignore           # Prevents pycache files from being pushed
└── README.md            # Project documentation (you are here!)

---

## 🚀 How to Run

1. Clone the repository

   git clone https://github.com/ishanyatripathi/chatbot.git
   cd chatbot

2. Install dependencies

   pip install -r requirements.txt

3. Run the chatbot

   python interface.py

---

## 💬 Example Interaction

🤖 Chatbot is ready! Type your question or /exit to quit.
User: Who wrote Hamlet?
Bot: William Shakespeare.

User: What is the capital of Italy?
Bot: Rome.

---

## 🤖 Model Details

- Model: google/flan-t5-base
- Type: Seq2Seq (Text2Text Generation)
- Size: ~500MB
- Capabilities: Instruction-following, Q&A, basic reasoning
- Runs Locally: Yes (no internet required after download)

---

## ✅ Features

- 💡 Uses instruction-tuned model for better factual accuracy
- 🧱 Modular code (model_loader.py, interface.py)
- 🧠 Local inference — no API keys or server needed
- 🧼 Clean .gitignore included

---

## 🎥 Demo Instructions (for Internship)

In your 2–3 minute video, include:

1. A quick tour of your folder and files
2. A short walkthrough of model_loader.py and interface.py
3. Live demo with 2–3 sample questions
4. Mention the GitHub link to your repo

---

## 👩‍💻 Author

- Ishanya Tripathi  
  GitHub: https://github.com/ishanyatripathi

---

## 📘 License

This project is licensed under the MIT License.

---

✅ Ready for internship submission!
