import streamlit as st

from prompts.physics_prompt import SYSTEM_PROMPT
from prompts.topics import TOPICS
from prompts.modes import MODES
from services.history_service import load_history


# ==========================================
# Topic Icons
# ==========================================

TOPIC_ICONS = {
    "Mechanics": "⚙️",
    "Electricity": "⚡",
    "Magnetism": "🧲",
    "Thermodynamics": "🔥",
    "Optics": "🔍",
    "Modern Physics": "🚀"
}


# ==========================================
# Clear Chat
# ==========================================

def clear_chat():
    """Menghapus seluruh riwayat percakapan."""

    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    st.session_state.current_chat_id = None
    st.session_state.loaded_chat_id = None

    st.rerun()


# ==========================================
# Sidebar
# ==========================================

def render_sidebar():

    with st.sidebar:
        history = load_history()

        # ======================================
        # Header
        # ======================================

        st.title("⚛️ PhysicsGPT")
        st.caption("AI Physics Learning Assistant")

        st.divider()

        # ======================================
        # Chat
        # ======================================

        st.subheader("💬 Chat")

        if st.button(
            "➕ New Chat",
            use_container_width=True
        ):
            clear_chat()

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):
            clear_chat()

        st.divider()

        # ======================================
        # Recent chats
        # ======================================

        st.subheader("📜 Recent Chats")

        if not history:
            st.caption("Belum ada chat.")
        else:
            for chat in reversed(history):
                if st.button(
                    f"💬 {chat['title']}",
                    key=chat["id"],
                    use_container_width=True
                ):
                    st.session_state.current_chat_id = chat["id"]
                    # reset agar app.py melakukan load ulang
                    st.session_state.loaded_chat_id = None
                    st.rerun()

        st.divider()

        # ======================================
        # Physics Topics
        # ======================================

        st.subheader("📚 Physics Topics")

        topic_labels = {
            f"{TOPIC_ICONS.get(topic,'📘')} {topic}": topic
            for topic in TOPICS.keys()
        }

        selected_label = st.radio(
            "Choose Topic",
            options=list(topic_labels.keys()),
            label_visibility="collapsed"
        )

        st.session_state.selected_topic = topic_labels[selected_label]

        st.caption(
            f"Current Topic: **{st.session_state.selected_topic}**"
        )

        st.divider()

        # ======================================
        # Learning Mode
        # ======================================

        st.subheader("🧠 Learning Mode")

        selected_mode = st.selectbox(
            "Mode",
            options=list(MODES.keys()),
            label_visibility="collapsed"
        )

        st.session_state.chat_mode = selected_mode

        st.caption(
            f"Current Mode: **{selected_mode}**"
        )

        st.divider()

        # ======================================
        # Fitur Aktif
        # ======================================

        st.subheader("✅ Fitur Tersedia")
        st.page_link("pages/1_Formula_Solver.py", label="Physics Formula Solver", icon="🧪")

        st.divider()

        # ======================================
        # Future Features
        # ======================================

        st.subheader("🚀 Coming Soon")

        st.caption("📄 PDF Learning")
        st.caption("🧠 RAG Knowledge Base")
        st.caption("📈 Learning Progress")
        st.caption("📝 Exam Mode")

        st.divider()

        # ======================================
        # About
        # ======================================

        st.subheader("ℹ️ About")

        st.write("**PhysicsGPT v1.0**")

        st.markdown("""
**Framework**
- Streamlit

**AI Model**
- Llama 3.3 70B

**Inference**
- Groq API
""")