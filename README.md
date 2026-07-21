<div align="center">

# ⚛️ PhysicsGPT

**AI-powered physics learning assistant built with Streamlit and Groq**

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?logo=streamlit&logoColor=white)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-00A67E)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Demo](#-demo) · [Features](#-features) · [Getting Started](#-getting-started) · [Deployment](#-deployment) · [Roadmap](#-roadmap)

</div>

---

## 📖 About

**PhysicsGPT** is a conversational AI assistant focused exclusively on physics
education. It combines topic-aware context, multiple learning modes, and a
symbolic formula solver to help students understand concepts and solve
problems step by step — powered by Llama 3.3 70B via the Groq API for
fast inference.

## 🎬 Demo

> 🔗 **Live app:** _add your Streamlit Cloud URL here after deploying_

<!--
Add a screenshot or GIF once deployed, e.g.:
![PhysicsGPT screenshot](assets/screenshot.png)
-->

## ✨ Features

- 💬 **Contextual physics chat** — ask questions and get answers in Bahasa Indonesia, grounded in accurate physics concepts
- 📚 **6 physics topics** — Mechanics, Electricity, Magnetism, Thermodynamics, Optics, and Modern Physics, each with tailored context
- 🧠 **5 learning modes** — adapt how the AI responds:
  | Mode | Behavior |
  |---|---|
  | Normal Chat | Free-form conversation |
  | Explain Concept | Structured concept breakdown with formulas & examples |
  | Solve Problem | Step-by-step problem solving (Known → Asked → Formula → Solution → Answer) |
  | Generate Quiz | Auto-generates multiple-choice practice questions |
  | Summarize Material | Condensed study summaries |
- 🧪 **Physics Formula Solver** — symbolic solver (via SymPy) that can rearrange any of ~15 common physics formulas to solve for whichever variable is unknown
- 📜 **Chat history** — conversations are saved locally and can be revisited from the sidebar
- ⚙️ **Configurable model & temperature** — swap models or tune response creativity via `config/settings.py`

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI / Frontend | [Streamlit](https://streamlit.io/) |
| LLM Inference | [Groq API](https://groq.com/) (Llama 3.3 70B) |
| Symbolic Math | [SymPy](https://www.sympy.org/) |
| Storage | Local JSON (`data/history.json`) |
| Config | `python-dotenv` |

## 📂 Project Structure

```
PhysicsGPT/
├── app.py                       # Main entry point (chat interface)
├── pages/
│   └── 1_Formula_Solver.py      # Physics Formula Solver page
├── components/
│   └── sidebar.py                # Sidebar UI (topics, modes, chat history)
├── config/
│   └── settings.py               # Environment & model configuration
├── data/
│   └── history.json              # Local chat history storage
├── prompts/
│   ├── physics_prompt.py         # Core system prompt
│   ├── topics.py                  # Per-topic context
│   └── modes.py                    # Per-mode instructions
├── services/
│   ├── groq_service.py           # Groq API wrapper
│   └── history_service.py        # Chat history CRUD
├── utils/
│   ├── prompt_builder.py         # Combines prompt + topic + mode
│   └── physics_formulas.py       # Formula database & solver engine
├── .env.example                   # Environment variable template
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com/keys)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/arikosetyawan00/PhysicsGPT.git
cd PhysicsGPT

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your API key
cp .env.example .env
# then edit .env and set GROQ_API_KEY=your_key_here

# 5. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## ☁️ Deployment

This app is designed to deploy for free on **[Streamlit Community Cloud](https://share.streamlit.io)**:

1. Push this repository to GitHub (already done ✅)
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select this repository, branch `main`, main file `app.py`
4. Under **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
5. Click **Deploy**

> ⚠️ **Security note:** never commit real API keys to this repository.
> `.env` is git-ignored — only `.env.example` (with a placeholder) should
> ever be committed. Streamlit Cloud reads secrets from its own **Secrets**
> panel, not from `.env`.

## 🗺️ Roadmap

- [x] Core chat with topic & mode selection
- [x] Physics Formula Solver
- [ ] 📈 Learning Progress tracking
- [ ] 📝 Exam Mode with scoring & timer
- [ ] 📄 PDF Learning (upload material as context)
- [ ] 🧠 RAG Knowledge Base

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check
the [issues page](https://github.com/arikosetyawan00/PhysicsGPT/issues) or
open a pull request.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE)
file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for fast LLM inference
- [Streamlit](https://streamlit.io/) for the app framework
- [SymPy](https://www.sympy.org/) for symbolic math

---

<div align="center">
Made with ⚛️ by <a href="https://github.com/arikosetyawan00">arikosetyawan00</a>
</div>
