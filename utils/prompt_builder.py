from prompts.physics_prompt import SYSTEM_PROMPT
from prompts.topics import TOPICS
from prompts.modes import MODES


def build_messages(chat_history, topic, mode):
    """
    Membangun daftar pesan yang akan dikirim ke LLM.
    """

    topic_context = TOPICS.get(
        topic,
        "Jawablah sebagai tutor fisika umum."
    )

    mode_instruction = MODES.get(
        mode,
        MODES["Normal Chat"]
    )

    system_prompt = f"""
{SYSTEM_PROMPT}

==================================================

KONTEKS PEMBELAJARAN

Topik:
{topic}

Materi yang menjadi fokus:

{topic_context}

==================================================

MODE PEMBELAJARAN

{mode}

Instruksi:

{mode_instruction}

==================================================

ATURAN

1. Selalu jawab dalam Bahasa Indonesia.
2. Fokus pada topik yang dipilih.
3. Ikuti format jawaban sesuai mode.
4. Berikan penjelasan yang mudah dipahami.
5. Gunakan contoh sederhana jika memungkinkan.
6. Gunakan notasi fisika yang benar.
7. Gunakan satuan SI.

==================================================
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Tambahkan seluruh riwayat chat (kecuali system lama)
    for message in chat_history:
        if message["role"] != "system":
            messages.append(message)

    return messages