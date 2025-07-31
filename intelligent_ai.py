class IntelligentAI:
    def __init__(self):
        self.personality = "You are an ethical hacking and programming assistant. Respond clearly, concisely, and professionally."

    def generate_response(self, message, user_id=None):
        message = message.lower()

        # Simple logic for demonstration (expand this as you like)
        if "hello" in message or "hi" in message:
            return "Hello! How can I help you today?"
        elif "help" in message or "hack" in message:
            return "As an ethical assistant, I can guide you on cybersecurity best practices and legal hacking techniques."
        elif "python" in message:
            return "Python is a versatile language. What would you like to build?"
        elif "bye" in message:
            return "Goodbye! Stay secure."
        else:
            return "I'm your AI assistant. I can help with ethical hacking, coding, or general tech questions."
