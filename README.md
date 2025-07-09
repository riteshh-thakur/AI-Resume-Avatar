# 🤖 AI Resume Avatar — A Smart Career Agent

**Ritesh Thakur's AI Avatar** is a next-generation, AI-powered resume interface. This project turns a traditional resume into an **interactive digital agent** that can answer questions about your background, skills, and experience — in first person.

Built using **Ollama + OpenChat**, **Gradio** for UI, and **Pushover** for real-time alerts, it creates a smart, deployable portfolio that actively engages recruiters, clients, or collaborators.

---

## 🚀 Features

✅ **LLM-Powered Chat**: Uses OpenChat via Ollama to simulate realistic and professional Q&A about your skills and experience.

✅ **Real-Time Notifications**: Instantly notifies you on your phone when someone interacts with your resume using [Pushover](https://pushover.net/).

✅ **Tool Usage Tracking**:
- Logs user contact info (`record_user_details`)
- Logs unknown questions the AI couldn't answer (`record_unknown_question`)

✅ **Resume-Contextual Awareness**: Uses your PDF resume (`linkedin.pdf`) and summary (`summary.txt`) to respond in character.

✅ **LLM (OpenAI API/Ollama)**: Uses open-source models running locally via [Ollama](https://ollama.com) — private, fast, and cost-free.

✅ **Modular and Extensible**: Easily plug in more tools (search, summarizer, file reader) or upgrade to LangChain Agents.

---

## 🎯 Use Cases

| Use Case                     | Benefit |
|-----------------------------|---------|
| 🧑‍💼 Job Applications          | Impress recruiters with a smart, living resume |
| 🌐 Portfolio Websites        | Embed it in your developer portfolio or GitHub Pages |
| 🧪 AI Agent Showcases        | Demonstrates advanced tool-calling and self-awareness |
| 📱 Personal Branding         | Provides a 24/7 assistant to answer questions about your work |
| 💡 Networking / Hiring       | Captures interest, collects contact info, and notifies you live |

---

## ✨ Uniqueness

- **Not just a chatbot.** It acts as your **digital twin**, complete with tools and intelligent behavior.
- **Push notifications on real devices**, unlike static resumes.
- **Tracks meaningful user data** to help you improve or respond.

---

## 🛠️ Tech Stack

| Component        | Tool               |
|------------------|--------------------|
| 💬 LLM            | OpenChat via Ollama |
| 🖥️ Frontend        | Gradio              |
| 📩 Notifications  | Pushover API        |
| 🧠 Prompt Engine   | LangChain PromptTemplate |
| 📄 Resume Context | PDF + Text files    |

---

## 🧑‍💻 Project Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourname/ai-resume-avatar.git
cd ai-resume-avatar
```

### 2. Install Dependencies

> You must have [Ollama installed](https://ollama.com/download)

```bash
# Pull OpenChat
ollama pull openchat

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install Python deps
pip install -r requirements.txt
```

### 3. Add Your Resume & Summary

Place your resume files in a `me/` folder:
```
/me
  ├── linkedin.pdf      ← Your detailed resume
  └── summary.txt       ← Short summary of your skills and goals
```

### 4. Configure Environment Variables

Create a `.env` file:
```
PUSHOVER_TOKEN=your_app_token
PUSHOVER_USER=your_user_key
```

> Get your token and user key from [pushover.net](https://pushover.net)

### 5. Run the App

```bash
uv run app.py
```

---

## 📂 File Structure

```
ai-resume-avatar/
├── app.py                      # Main app logic (chat + Gradio)
├── me/
│   ├── linkedin.pdf            # Your resume
│   └── summary.txt             # Your short profile summary
├── .env                        # Pushover API keys
├── requirements.txt
```

---

## 🧠 Example Conversations

> User: What kind of projects have you worked on in AI?

> AI: I’ve worked on projects involving LangChain Agents, Playwright test automation, and an AI-powered SaaS Testing Platform...

---

## 🔐 Privacy-Friendly

- No data leaves your machine — LLM runs locally.
- Logs are stored locally (`record_user_detail.json`, `record_unknown_question.json`).

---

## 📦 Planned Improvements

- [ ] Add download button for resume
- [ ] Deploy on Hugging Face or Railway
- [ ] Add analytics dashboard
- [ ] Enable voice interface (Gradio + Whisper)

---

## 🤝 Credits

Developed by [Ritesh Thakur](https://github.com/riteshh-thakur)  
LLM Powered by [OpenChat](https://huggingface.co/openchat) via [Ollama](https://ollama.com)  
Push Notifications by [Pushover](https://pushover.net)

---

## 📧 Contact Me

If you'd like to collaborate, hire, or connect, please say hi via the AI avatar — or reach out at: `thakurritesh8219@gmail.com`

---
