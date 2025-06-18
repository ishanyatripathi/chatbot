# interface.py

from model_loader import load_chatbot_model

def main():
    chatbot = load_chatbot_model()

    print("🤖 Chatbot is ready! Type your question or /exit to quit.")
    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        # Smart prompt to improve factual output
        prompt = f"Answer this question correctly:\n{user_input}"
        response = chatbot(prompt, max_new_tokens=100)[0]['generated_text']
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
