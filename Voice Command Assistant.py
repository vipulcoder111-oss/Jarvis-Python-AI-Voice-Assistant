import speech_recognition as sr
import pyttsx3
import datetime

# ---------------- SPEECH RECOGNITION ----------------
r = sr.Recognizer()


# ---------------- SPEAK FUNCTION ----------------
def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ---------------- FIRST VOICE ----------------
speak("Hello Vipul, I am your assistant.")


# ---------------- MAIN PROGRAM ----------------
while True:

    with sr.Microphone(device_index=1) as source:

        print("Speak...")

        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:

        command = r.recognize_google(audio).lower()

        print("You:", command)

        # ---------------- TIME ----------------
        if "time" in command:

            t = datetime.datetime.now().strftime("%I:%M %p")

            print("The time is", t)

            speak("The time is " + t)

        # ---------------- WEATHER ----------------
        elif "weather" in command:

            print("Today's weather is sunny.")

            speak("Today's weather is sunny.")

        # ---------------- NEWS ----------------
        elif "news" in command:

            print("Today's top news is AI is growing fast.")

            speak("Today's top news is AI is growing fast.")

        # ---------------- HELLO ----------------
        elif "hello" in command or "hi" in command:

            print("Hello! How can I help you?")

            speak("Hello! How can I help you?")

        # ---------------- NAME ----------------
        elif "your name" in command or "who are you" in command:

            print("I am your personal voice assistant.")

            speak("I am your personal voice assistant.")

        # ---------------- EXIT ----------------
        elif "exit" in command or "bye" in command:

            print("Goodbye!")

            speak("Goodbye! Have a nice day.")

            break

        # ---------------- UNKNOWN ----------------
        else:

            print("Command not found.")

            speak("Sorry, I don't understand that command.")

    except sr.UnknownValueError:

        print("Please speak again.")

        speak("Please speak again.")

    except sr.RequestError:

        print("Speech recognition service is not available.")

        speak("Speech recognition service is not available.")