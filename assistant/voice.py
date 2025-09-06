import speech_recognition as sr
from gtts import gTTS
import pygame
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()    # Stop playback explicitly
    pygame.mixer.quit()          # Quit the mixer to release the file lock

    os.remove(filename)          # Now safe to delete the file

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=3, phrase_time_limit=4)
    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except Exception as e:
        speak("Sorry, could not recognize your voice.")
        return ""
