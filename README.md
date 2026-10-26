# VoiceBot AI Assistant 🎙️

## About the Project

Voice AI Assistant is a Python-based application that allows users to interact with an AI using voice commands. It records the user's voice, converts speech into text, generates AI responses using the Llama 3.2 model, and speaks the answers aloud.

The assistant can also provide the current date and time through voice interaction.

## Features

- **Voice Input:** Records user voice using a microphone.
- **Speech Recognition:** Converts spoken words into text using Faster-Whisper.
- **AI Responses:** Uses Ollama with the Llama 3.2 model to answer questions.
- **Voice Output:** Converts AI-generated text into speech using pyttsx3.
- **Current Time:** Provides the current time when asked.
- **Current Date:** Provides today's date when asked.
- **Continuous Interaction:** Allows users to ask multiple questions without restarting the program.
- **Stop Commands:** Stops the assistant when the user says stop, exit, quit, goodbye, close, or shutdown.

## Technologies Used

- Python
- SoundDevice
- SciPy
- Faster-Whisper
- Ollama
- Llama 3.2
- pyttsx3
- DateTime

## Requirements

- Python installed on your computer.
- Working microphone.
- Ollama installed.
- Internet connection to download the required AI model and dependencies.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Voice-AI-Assistant
```

### 3. Install Required Libraries

```bash
pip install sounddevice scipy faster-whisper ollama pyttsx3
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/

### 5. Download the Llama 3.2 Model

Open your terminal and run:

```bash
ollama pull llama3.2
```

### 6. Run the Program

```bash
python main.py
```

## How It Works

1. The program starts and loads the Faster-Whisper speech recognition model.
2. The microphone records the user's voice for 5 seconds.
3. Faster-Whisper converts the recorded audio into text.
4. The program checks whether the user is asking for the current date or time.
5. For normal questions, Ollama generates an AI response using Llama 3.2.
6. The answer is displayed on the screen.
7. pyttsx3 converts the answer into speech.
8. The assistant continues listening for the next question.

## Example Interaction

**User:** What is the capital of India?

**AI:** The capital of India is New Delhi.

**User:** What is the current time?

**AI:** The current time is 07:30 PM.

**User:** Stop.

**AI:** Goodbye.

## Project Structure

```text
Voice-AI-Assistant/
│
├── main.py
├── audio.wav
└── README.md
```

`audio.wav` is generated automatically when the program records voice.

## Future Improvements

- Support for multiple languages.
- Add a graphical user interface.
- Improve voice detection and recording duration.
- Add more voice commands.
- Integrate additional AI models.

## Author

Developed as a Python-based Voice AI Assistant project.

## License

This project is open-source and available for learning and educational purposes.
