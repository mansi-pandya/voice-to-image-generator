import speech_recognition as sr
from deep_translator import GoogleTranslator

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Describe what you want:")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        return recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        print("Couldn't understand audio.")
        return None

    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return None

    except sr.RequestError:
        print("Speech Recognition service unavailable.")
        return None


def translate(text):
    return GoogleTranslator(
        source="auto",
        target="en"
    ).translate(text)