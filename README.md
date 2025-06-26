# HEY SIRI - A Voice-Controlled Smart Virtual Assistant (MALA)

**HEY_SIRI** is an intelligent voice assistant named **MALA** developed in Python using speech recognition, text-to-speech, AI-based essay writing, weather, math solving, and much more. It listens for a wake word and performs a wide range of tasks like playing music, writing essays, fetching news/weather, solving math problems, and executing system operations via voice commands.

---

## 🎯 Features

- 🎤 Voice activation using a wake word (`"mala"`)
- 🔊 Text-to-speech with male/female voice switching
- 🧠 AI-powered essay generation using Google Gemini
- 🌦️ Real-time weather info (via OpenWeather API)
- 🧮 Math solver with GUI using generative AI
- 📰 News reading by category (via NewsAPI)
- 📺 YouTube & Google search
- 🖼️ Screenshot capture
- 🔐 System operations (shutdown, restart, lock, empty recycle bin)
- 🎵 Play YouTube songs via voice
- 🗣️ Small talk with predefined chatbot patterns

---

## 🧪 Technologies Used

- Python 3.x
- Google Generative AI (Gemini)
- `speech_recognition` for speech input
- `pyttsx3` for text-to-speech
- `tkinter` for GUI components
- `pywhatkit`, `pyautogui` for automation
- `requests` for API calls
- `nltk` for simple chatbot response
- `wikipedia`, `wolframalpha`, `openai` (optional extensions)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MAHADHARSHINI29/HEY_SIRI.git
cd HEY_SIRI

pip install -r requirements.txt

##Replace #API_KEY in the script with your actual API keys:
  Google Generative AI
  OpenWeatherMap API
  NewsAPI

```bash
python hey_siri.py

Then speak the wake word:
mala
