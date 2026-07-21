from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME ,TEMPERATURE,MAX_COMPLETION_TOKENS

# Membuat koneksi ke Groq API
client = Groq(api_key=GROQ_API_KEY)


def ask_groq(messages):
    """
    Mengirim daftar pesan ke Groq API
    dan mengembalikan jawaban AI.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
        max_completion_tokens=MAX_COMPLETION_TOKENS
    )

    return response.choices[0].message.content