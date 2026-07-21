# ⚛️ PhysicsGPT

Asisten belajar fisika berbasis AI, dibangun dengan Streamlit dan Groq API
(model Llama 3.3 70B). Mendukung banyak topik fisika, beberapa mode belajar
(jelaskan konsep, selesaikan soal, buat kuis, ringkas materi), serta riwayat
chat yang tersimpan.

## ⚠️ Sebelum mulai — soal keamanan API key

Proyek ini pernah menyertakan file `.env` berisi API key Groq asli. **Jika kamu
pernah membagikan folder proyek ini (termasuk sebagai file zip) ke pihak lain,
segera rotate/revoke key tersebut di https://console.groq.com/keys dan buat
key baru.** File `.env` sudah ada di `.gitignore` sehingga aman dari git,
tapi tidak otomatis aman dari zip/share manual.

## 1. Setup Lokal

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Buat file .env dari template
cp .env.example .env
# lalu edit .env dan isi GROQ_API_KEY dengan key kamu

# 3. Jalankan aplikasi
streamlit run app.py
```

## 2. Struktur Proyek

```
PhysicsGPT/
├── app.py                     # Entry point Streamlit
├── components/
│   └── sidebar.py              # UI sidebar (topik, mode, riwayat chat)
├── config/
│   └── settings.py             # Load .env & konfigurasi model
├── data/
│   └── history.json            # Penyimpanan riwayat chat (JSON lokal)
├── prompts/
│   ├── physics_prompt.py       # System prompt utama PhysicsGPT
│   ├── topics.py                # Konteks per topik fisika
│   └── modes.py                  # Instruksi per mode belajar
├── services/
│   ├── groq_service.py         # Wrapper pemanggilan Groq API
│   └── history_service.py      # CRUD riwayat chat (JSON)
├── utils/
│   └── prompt_builder.py       # Menggabungkan system prompt + topik + mode
├── .env.example                 # Template variabel lingkungan
└── requirements.txt
```

## 3. Deploy ke Streamlit Community Cloud

1. Push folder ini ke GitHub (pastikan `.env` **tidak** ikut ter-push —
   sudah otomatis diabaikan lewat `.gitignore`).
2. Buka [share.streamlit.io](https://share.streamlit.io) → **New app**,
   pilih repo dan file utama `app.py`.
3. Di **Advanced settings → Secrets**, tambahkan:
   ```toml
   GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxx"
   ```
4. Update `config/settings.py` agar juga bisa membaca dari `st.secrets`
   sebagai fallback (opsional, berguna karena Streamlit Cloud tidak
   membaca file `.env`):
   ```python
   import streamlit as st
   GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
   ```
5. Klik **Deploy**.

## 4. Catatan

- `data/history.json` bersifat lokal per-instance. Di Streamlit Cloud,
  penyimpanan ini akan reset saat aplikasi di-redeploy/restart karena
  filesystem-nya sementara (ephemeral). Untuk penyimpanan permanen,
  pertimbangkan database eksternal (mis. Supabase/SQLite dengan volume
  persisten).
- Model AI diatur di `config/settings.py` (`MODEL_NAME`). Daftar model
  Groq terbaru bisa dicek di https://console.groq.com/docs/models.
