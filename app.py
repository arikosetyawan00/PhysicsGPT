import streamlit as st

from components.sidebar import render_sidebar
from prompts.physics_prompt import SYSTEM_PROMPT
from services.groq_service import ask_groq
from utils.prompt_builder import build_messages
from services.history_service import (
    get_chat,
    create_chat,
    add_chat,
    update_chat
)
# ==========================================
# Konfigurasi Halaman
# ==========================================

st.set_page_config(
    page_title="PhysicsGPT",
    page_icon="⚛️",
    layout="wide"
)


# ==========================================
# Header
# ==========================================

st.title("⚛️ PhysicsGPT")
st.caption("AI Physics Learning Assistant")

# ==========================================
# Inisialisasi Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = "Mechanics"

if "chat_mode" not in st.session_state:
    st.session_state.chat_mode = "Normal Chat"

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

if "loaded_chat_id" not in st.session_state:
    st.session_state.loaded_chat_id = None
# ==========================================
# Sidebar
# ==========================================

render_sidebar()


# ==========================================
# Load Active Chat
# ==========================================

if (
    st.session_state.current_chat_id is not None
    and
    st.session_state.current_chat_id != st.session_state.loaded_chat_id
):

    chat = get_chat(st.session_state.current_chat_id)

    if chat:
        st.session_state.messages = chat["messages"]
        st.session_state.loaded_chat_id = chat["id"]
# ==========================================
# Menampilkan Riwayat Chat
# ==========================================

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# Input User
# ==========================================

prompt = st.chat_input("Tanyakan sesuatu tentang fisika...")

if prompt:
    topic = st.session_state.get(
        "selected_topic",
        "Mechanics"
    )

    mode = st.session_state.get(
        "chat_mode",
        "Normal Chat"
    )


# ==========================================
# Membuat Chat Baru
# ==========================================

    if st.session_state.current_chat_id is None:
        new_chat = create_chat(
            title=prompt[:40],
            topic=topic,
            mode=mode
        )

        add_chat(new_chat)

        st.session_state.current_chat_id = new_chat["id"]
        st.session_state.loaded_chat_id = new_chat["id"]



    # tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Ambil topik & mode dari sidebar
    topic = st.session_state.get(
        "selected_topic",
        "Mechanics"
    )

    mode = st.session_state.get(
        "chat_mode",
        "Normal Chat"
    )

    # Bangun prompt
    messages = build_messages(
        chat_history=st.session_state.messages,
        topic=topic,
        mode=mode
    )

    # Memanggil Groq
    with st.chat_message("assistant"):
        with st.spinner("PhysicsGPT sedang berpikir..."):
            try:
                answer = ask_groq(messages)
            except Exception as e:
                answer = f"❌ Terjadi kesalahan:\n\n{e}"
        st.markdown(answer)

    # Simpan jawaban AI
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    # ===========================
    # Update Chat
    # ===========================

    chat = get_chat(st.session_state.current_chat_id)

    if chat:
        chat["messages"] = st.session_state.messages
        update_chat(chat)
