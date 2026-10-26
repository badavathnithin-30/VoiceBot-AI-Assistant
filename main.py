import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import ollama
import pyttsx3
from datetime import datetime


# ==========================================
# 1. LOAD SPEECH RECOGNITION
# ==========================================

print("Loading speech recognition...")

whisper_model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


# ==========================================
# 2. RECORD VOICE
# ==========================================

def record_voice():

    sample_rate = 16000
    seconds = 5

    print("\n🎤 Speak now...")

    audio = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(
        "audio.wav",
        sample_rate,
        audio
    )

    print("✅ Recording completed.")


# ==========================================
# 3. VOICE → TEXT
# ==========================================

def speech_to_text():

    print("📝 Converting voice to text...")

    segments, info = whisper_model.transcribe(
        "audio.wav",
        vad_filter=True,
        language="en"
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()


# ==========================================
# 4. CURRENT TIME
# ==========================================

def get_current_time():

    return datetime.now().strftime("%I:%M %p")


# ==========================================
# 5. CURRENT DATE
# ==========================================

def get_current_date():

    return datetime.now().strftime("%A, %d %B %Y")


# ==========================================
# 6. ASK AI
# ==========================================

def ask_ai(question):

    question_lower = question.lower().strip()


    # --------------------------------------
    # TIME
    # --------------------------------------

    if (
        "what time" in question_lower
        or "current time" in question_lower
        or "time now" in question_lower
        or "what is the time" in question_lower
        or "tell me the time" in question_lower
        or "what's the time" in question_lower
    ):

        return "The current time is " + get_current_time()


    # --------------------------------------
    # DATE
    # --------------------------------------

    if (
        "what date" in question_lower
        or "today's date" in question_lower
        or "current date" in question_lower
        or "what is today" in question_lower
        or "what day is it" in question_lower
    ):

        return "Today is " + get_current_date()


    # --------------------------------------
    # NORMAL QUESTION → OLLAMA
    # --------------------------------------

    print("\n🧠 AI is thinking...")

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return "Sorry, I could not connect to the AI."


# ==========================================
# 7. TEXT → VOICE
# ==========================================

def speak(text):

    print("\n🔊 AI is speaking...")

    try:

        # Create a NEW engine every time
        engine = pyttsx3.init()

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(text)

        engine.runAndWait()

        # Cleanly stop this engine
        engine.stop()

        del engine

    except Exception as e:

        print("⚠️ Voice error:", e)


# ==========================================
# 8. START
# ==========================================

print("\n===================================")
print("       VOICE AI ASSISTANT")
print("===================================")
print("Ask any question.")
print("Say 'stop' to stop the program.")
print("===================================")


# ==========================================
# 9. MAIN LOOP
# ==========================================

while True:

    # --------------------------------------
    # RECORD
    # --------------------------------------

    record_voice()


    # --------------------------------------
    # CONVERT VOICE TO TEXT
    # --------------------------------------

    text = speech_to_text()

    print("\nYou said:")
    print(text)


    # --------------------------------------
    # NOTHING HEARD
    # --------------------------------------

    if not text or not any(c.isalnum() for c in text):

        print("❌ I didn't hear clear speech.")

        continue


    # --------------------------------------
    # STOP COMMAND
    # --------------------------------------

    if text.lower().strip() in [
        "stop",
        "exit",
        "quit",
        "goodbye",
        "close",
        "shutdown"
    ]:

        print("\n🛑 Agent stopped.")

        speak("Goodbye")

        break


    # --------------------------------------
    # ASK AI
    # --------------------------------------

    answer = ask_ai(text)


    # --------------------------------------
    # SHOW ANSWER
    # --------------------------------------

    print("\n🤖 AI:")
    print(answer)


    # --------------------------------------
    # SPEAK ANSWER
    # --------------------------------------

    speak(answer)


    # --------------------------------------
    # READY
    # --------------------------------------

    print("\n✅ Ready for next question!")






    