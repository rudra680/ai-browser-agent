chat_history = []

def add_memory(message):
    chat_history.append(message)

def get_memory():
    return chat_history