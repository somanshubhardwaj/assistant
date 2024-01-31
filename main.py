import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Sorry, there was an error while requesting results; {e}")
        return None


while True:
    text = listen()
    if text:
        print("You said:", text)
        break

langcode = {"Hindi": "hi", "English": "en", "French": "fr", "German": "de", "Spanish": "es", "Italian": "it",
            "Japanese": "ja", "Korean": "ko", "Russian": "ru", "Chinese": "zh-cn"}


def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


text_to_translate = input("Enter the text to translate: ")
print("Languages:")
for language in langcode:
    print(f"{language} ({langcode[language]})")
target_language = input("Enter the target language (e.g., 'fr' for French): ")
translated_text = translate_text(text_to_translate, target_language)
print("Translated text:", translated_text)


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Opens the generated audio file


text_to_convert = translated_text
language_code = target_language
text_to_speech(text_to_convert, language_code)
