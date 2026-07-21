from services.history_service import (
    create_chat,
    add_chat,
    load_history
)

chat = create_chat(
    title="Apa itu Hukum Newton?",
    topic="Mechanics",
    mode="Explain Concept"
)

add_chat(chat)

print("Chat berhasil ditambahkan!\n")

history = load_history()

print(history)