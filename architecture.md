# System Architecture

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
Tool Orchestration
        ↓
FAISS Memory Retrieval
        ↓
Scheduling Engine
        ↓
TTS Response Generation
        ↓
Browser Audio Playback