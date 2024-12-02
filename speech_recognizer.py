import speech_recognition as sr
import pyttsx3
import aifc

def speak_text(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Captures speech and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            # Listen and recognize speech
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "I could not understand what you said."
        except sr.RequestError:
            return "Unable to connect to the speech recognition service."

def process_command(command):
    """Processes the recognized command and performs actions."""
    if "hello" in command:
        response = "Hello! How can I assist you today?"
    elif "time" in command:
        from datetime import datetime
        response = f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "exit" in command or "quit" in command:
        response = "Goodbye!"
        speak_text(response)
        exit()
    else:
        response = "I'm sorry, I didn't understand that command."
    return response

def main():
    """Main function to handle speech recognition and command processing."""
    print("Speech Recognition System is ready.")
    speak_text("Speech recognition system is ready.")
    while True:
        command = recognize_speech()
        if command:
            print(f"You said: {command}")
            response = process_command(command)
            print(response)
            speak_text(response)

if __name__ == "__main__":
    main()
