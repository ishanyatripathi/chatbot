from model_loader import load_chatbot_model
from chat_memory import ChatMemory

def main():
    chatbot = load_chatbot_model()
    memory = ChatMemory(max_turns=5)

    print("🤖 Chatbot is ready! Type your question or /exit to quit.")
    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        # Include previous history in the prompt
        prompt = memory.get_context_text() + f"User: {user_input}\nBot:"
        response = chatbot(prompt, max_new_tokens=100)[0]["generated_text"]

        # Extract the new response (after the prompt)
        bot_reply = response[len(prompt):].strip().split("\n")[0]

        print(f"Bot: {bot_reply}")
        memory.add_exchange(user_input, bot_reply)

if __name__ == "__main__":
    main()
