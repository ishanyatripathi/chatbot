class ChatMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []

    def add_exchange(self, user_input, bot_response):
        self.history.append((user_input, bot_response))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context_text(self):
        context = ""
        for user, bot in self.history:
            context += f"User: {user}\nBot: {bot}\n"
        return context
