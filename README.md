# 🎙️ Real-Time Multilingual Voice AI Agent

A production-style multilingual conversational AI system supporting realtime voice interaction, multilingual speech recognition, contextual memory, AI reasoning, and voice responses using FastAPI, WebSockets, LangGraph, Groq, FAISS, and faster-whisper.

---

# ✨ Features

## 🎤 Real-Time Voice Streaming

* Browser microphone streaming
* Low-latency WebSocket communication
* Real-time speech pipeline

## 🌍 Multilingual AI Support

* English
* Hindi
* Tamil
* Automatic language detection
* Language-aware AI responses

## 🧠 Conversational AI Agent

* LangGraph orchestration
* Groq LLM integration
* Context-aware reasoning
* Tool-driven workflows

## 🗂️ Persistent Memory System

* FAISS vector database
* Semantic memory retrieval
* Conversation continuity
* Context persistence

## 🔊 Speech Pipeline

* faster-whisper Speech-to-Text
* edge-tts Text-to-Speech
* Real-time audio response playback

## ⚡ Realtime UX Features

* Streaming microphone input
* Interruption handling
* WebSocket-based communication
* Low-latency response pipeline

## 📅 Scheduling System

* Appointment booking
* Appointment cancellation
* Doctor specialization matching
* Slot management

## 📈 Production Features

* Render cloud deployment
* Lazy-loaded AI models
* Deployment-safe architecture
* WebSocket production handling

---

# 🏗️ System Architecture

```text
Browser Microphone
        ↓
WebSocket Streaming
        ↓
FastAPI Backend
        ↓
Streaming Audio Buffer
        ↓
faster-whisper STT
        ↓
Language Detection
        ↓
LangGraph Agent
        ↓
Groq LLM
        ↓
FAISS Memory Retrieval
        ↓
Text-to-Speech
        ↓
Browser Audio Playback
```

---

# 🛠️ Tech Stack

| Layer                  | Technology            |
| ---------------------- | --------------------- |
| Backend                | FastAPI               |
| Realtime Communication | WebSockets            |
| AI Orchestration       | LangGraph             |
| LLM                    | Groq                  |
| STT                    | faster-whisper        |
| TTS                    | edge-tts              |
| Vector Memory          | FAISS                 |
| Embeddings             | Sentence Transformers |
| Deployment             | Render                |
| Language               | Python 3.12           |

---

# 📂 Project Structure

```text
project-root/
│
├── agent/
├── api/
├── memory/
├── voice/
├── scheduler/
├── outbound/
├── frontend/
├── utils/
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/cruzz77/Real-Time-Multilingual-Voice-AI-Agent.git

cd Real-Time-Multilingual-Voice-AI-Agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

MODEL_NAME=llama-3.1-8b-instant

WHISPER_MODEL=tiny

TTS_VOICE_EN=en-US-AriaNeural

TTS_VOICE_HI=hi-IN-SwaraNeural

TTS_VOICE_TA=ta-IN-PallaviNeural
```

---

# ▶️ Run Locally

```bash
uvicorn api.server:app --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000
```

---

# ☁️ Deployment

Deployed on Render using:

* Python Web Service
* FastAPI
* WebSockets
* HTTPS secure streaming

### Render Start Command

```bash
uvicorn api.server:app --host 0.0.0.0 --port $PORT
```

---

# 🧪 Example Queries

## English

```text
Book me a dermatologist appointment tomorrow evening
```

## Hindi

```text
मुझे कल डॉक्टर की अपॉइंटमेंट चाहिए
```

## Tamil

```text
எனக்கு நாளை மருத்துவர் நேரம் வேண்டும்
```

---


# 🎥 Demo Video

Add your demo video link here:

```text
https://your-demo-video-link
```

---

# 📈 Future Improvements

* Redis distributed memory
* Twilio phone integration
* GPU inference optimization
* Streaming token generation
* Voice Activity Detection (VAD)
* Kubernetes deployment

---

# 🧩 Challenges Solved

* Render deployment optimization
* AI model lazy loading
* WebSocket production handling
* Multilingual speech pipeline
* Realtime streaming architecture
* Deployment memory optimization

---

# 👨‍💻 Author

Aditya Chopra

GitHub:
https://github.com/cruzz77

---

# ⭐ Project Highlights

✅ Realtime AI voice interaction
✅ Multilingual speech support
✅ Production deployment
✅ WebSocket streaming
✅ FAISS semantic memory
✅ LangGraph orchestration
✅ Faster-whisper integration
✅ Render cloud deployment

---

# 📜 License

This project is developed for educational, research, and portfolio purposes.
