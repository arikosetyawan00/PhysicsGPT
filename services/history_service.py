import json
import uuid
from datetime import datetime
from pathlib import Path

# ==========================================
# History File
# ==========================================

HISTORY_FILE = Path("data/history.json")


# ==========================================
# Load History
# ==========================================

def load_history():
    """
    Memuat seluruh riwayat chat dari file JSON.
    """

    if not HISTORY_FILE.exists():
        return []

    try:
        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:
        return []


# ==========================================
# Save History
# ==========================================

def save_history(history):
    """
    Menyimpan seluruh riwayat chat ke file JSON.
    """

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )

# ==========================================
# Create Chat
# ==========================================

def create_chat(
    title,
    topic,
    mode
):
    """
    Membuat objek chat baru.
    """

    chat_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    chat = {
    "id": chat_id,
    "title": title,
    "created_at": timestamp,
    "updated_at": timestamp,
    "topic": topic,
    "mode": mode,
    "messages": []
}
    return chat
# ==========================================
# Add Chat
# ==========================================

def add_chat(chat):
    """
    Menambahkan chat baru ke history.
    """
    history = load_history()
    history.append(chat)
    save_history(history)


# ==========================================
# Get Chat By ID
# ==========================================

def get_chat(chat_id):
    """
    Mengambil satu chat berdasarkan ID.
    """

    history = load_history()

    for chat in history:
        if chat["id"] == chat_id:
            return chat

    return None

# ==========================================
# Update Chat
# ==========================================

def update_chat(updated_chat):
    """
    Memperbarui isi chat yang sudah ada.
    """

    history = load_history()

    for index, chat in enumerate(history):

        if chat["id"] == updated_chat["id"]:

            updated_chat["updated_at"] = datetime.now().isoformat()

            history[index] = updated_chat

            break

    save_history(history)