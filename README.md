# Voice AI Assistant

## Description
Voice AI Assistant is a Python-based project that allows users to interact with an AI using voice commands. It converts speech into text, generates answers using the Llama 3.2 model, and speaks the answers aloud.

It can also provide the current date and time.

## Technologies Used
- Python
- Faster-Whisper
- Ollama
- Llama 3.2
- SoundDevice
- SciPy
- pyttsx3

## Features
- Records voice using a microphone.
- Converts speech into text.
- Generates AI responses.
- Speaks the generated answers.
- Provides current date and time.
- Supports continuous voice interaction.
- Stops using voice commands like stop, exit, and quit.

## Installation

Install the required libraries:

```bash
pip install sounddevice scipy faster-whisper ollama pyttsx3
```

Install Ollama and download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

## How to Run

Run the following command:

```bash
python main.py
```

## Working
1. The microphone records the user's voice.
2. Faster-Whisper converts voice into text.
3. Ollama generates an AI response.
4. pyttsx3 converts the response into speech.
5. The assistant continues listening for the next question.

## Project Structure

```text
Voice-AI-Assistant/
    main.py
    audio.wav
    README.md
```

## Author
Developed using Python as a Voice AI Assistant project.
