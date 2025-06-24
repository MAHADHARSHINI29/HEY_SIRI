# Required Imports
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import openai
import pyttsx3
from nltk.chat.util import Chat, reflections
import datetime
import platform
import sys
import wikipedia
import wolframalpha
import requests
import random
import webbrowser
from bs4 import BeautifulSoup
import os
import winshell
import pywhatkit
import pyautogui
import time
import ctypes

# Setup Google API Key
google_api_key = "AIzaSyBUvjiVam5-5B_gat9gKQbSvNU8p6xwsY0"
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

class VirtualAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.synthesizer = pyttsx3.init()
        self.voice_gender = "female"
        self.chatbot = Chat(self.get_chat_patterns(), reflections)
        self.wake_word = "mala"
        self.voices = self.synthesizer.getProperty('voices')
        self.female_voice = None
        self.male_voice = None

        for voice in self.voices:
            if 'zira' in voice.name.lower():
                self.female_voice = voice.id
            elif 'david' in voice.name.lower():
                self.male_voice = voice.id
            if self.female_voice and self.male_voice:
                break

        if self.female_voice:
            self.synthesizer.setProperty('voice', self.female_voice)

    def change_voice(self):
        if self.female_voice and self.male_voice:
            current = self.synthesizer.getProperty('voice')
            new_voice = self.male_voice if current == self.female_voice else self.female_voice
            self.synthesizer.setProperty('voice', new_voice)
            self.speak("Voice changed!")

    def speak(self, text):
        self.synthesizer.say(text)
        self.synthesizer.runAndWait()

    def listen_for_wake_word(self):
        with sr.Microphone() as source:
            while True:
                audio = self.recognizer.listen(source)
                try:
                    if self.wake_word in self.recognizer.recognize_google(audio).lower():
                        self.speak("System activated successfully")
                        self.speak(self.greet())
                        self.listen_for_command()
                        break
                    else:
                        self.speak("Access Denied...")
                except:
                    pass

    def play_listening_tune(self):
        if platform.system() == 'Windows':
            import winsound
            winsound.Beep(2500, 300)

    def get_chat_patterns(self):
        return [
            (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
            (r'how are you', ['I am good, thank you!']),
            (r'what is your name', ['You can call me MALA!']),
            (r'bye|see you', ['Goodbye!', 'Bye!', 'See you later!']),
            (r'who are you', ['Everyone calls me smart voice assistant.']),
            (r'help', ['Sure! I\'ll do my best to assist you.']),
        ]

    def greet(self):
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12: return "Good morning!"
        elif 12 <= hour < 18: return "Good afternoon!"
        elif 18 <= hour < 21: return "Good evening!"
        else: return "Good night!"

    # Additional command methods like search, play music, essay generation etc.
    # See next message for extended methods (GUI, weather, math, essay, maps...)
    def listen_for_command(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            query = self.recognizer.recognize_google(audio).lower()

            if "change voice" in query:
                self.change_voice()
            elif "play song" in query:
                self.play_song()
            elif "close tab" in query:
                self.close_current_tab()
            elif "map" in query:
                self.open_google_maps()
            elif "empty recycle bin" in query:
                self.empty_recycle_bin()
            elif "lock window" in query:
                self.lock_window()
            elif "restart" in query or "reboot" in query:
                self.restart_system()
            elif "shutdown" in query:
                self.shutdown_system()
            elif "write" in query or "essay" in query:
                self.write_essay()
            elif "news" in query:
                self.listen_and_respond()
            elif "weather" in query:
                self.get_weather()
            elif "time" in query:
                self.tell_time()
            elif "joke" in query:
                self.tell_joke()
            elif "today" in query:
                self.tell_today_date()
            elif "tomorrow" in query:
                self.tell_tomorrow_date()
            elif "yesterday" in query:
                self.tell_yesterday_date()
            elif "maths" in query or "calculate" in query:
                self.open_math_gui()
            elif "take screenshot" in query:
                self.take_screenshot()
            elif "youtube" in query:
                self.search_youtube()
            elif "google" in query:
                self.search_google()
            elif "search" in query:
                topic = query.replace("search", "").strip()
                self.get_brief_info(topic)
            elif "goodbye" in query:
                self.speak("Goodbye! Take care.")
                sys.exit()
            else:
                response = self.chatbot.respond(query)
                self.speak(response)

        except Exception as e:
            self.speak(f"Error: {e}")

    def play_song(self):
        self.speak('Which song would you like to play?')
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            song = self.recognizer.recognize_google(audio).lower()
            self.speak('Playing ' + song)
            pywhatkit.playonyt(song)
        except:
            self.speak("Sorry, I couldn't play that.")

    def search_youtube(self):
        self.speak("What would you like to search for on YouTube?")
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            query = self.recognizer.recognize_google(audio).lower()
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
        except:
            self.speak("Couldn't understand your search.")

    def search_google(self):
        self.speak("What would you like to search on Google?")
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            query = self.recognizer.recognize_google(audio).lower()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
        except:
            self.speak("Couldn't understand your search.")
    def write_essay(self):
        self.speak("On which topic do you need the essay?")
        topic = self.recognize_speech_from_microphone()
        if topic:
            self.speak(f"Writing essay on {topic}. Please wait...")
            essay = self.generate_essay(topic)
            self.speak("Here is the essay.")
            self.display_essay(essay)

    def generate_essay(self, topic):
        try:
            prompt = f"Write an essay on the topic: {topic}. The essay should discuss the key points and provide analysis."
            response = model.generate_content(prompt)
            return response.text
        except:
            return "An error occurred while generating the essay."

    def display_essay(self, essay):
        root = tk.Tk()
        root.title("Generated Essay")
        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
        text_area.pack(padx=10, pady=10)
        text_area.insert(tk.INSERT, essay)
        text_area.configure(state='disabled')
        root.mainloop()

    def listen_and_respond(self):
        self.speak("Which category do you want to hear news from? (politics, health, sports, weather, economics)")
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            category = self.recognizer.recognize_google(audio).lower()
            mapping = {
                "politics": "general",
                "health": "health",
                "sports": "sports",
                "weather": "general",
                "economics": "business"
            }
            if category in mapping:
                headlines = self.get_news(mapping[category])
                self.speak_news(headlines)
            else:
                self.speak("Sorry, I couldn't understand the category.")
        except:
            self.speak("Could not understand.")

    def get_news(self, category):
        api_key = "1aedf86443d4474b8e53c8f0f051d5b7"
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}"
        response = requests.get(url)
        news_data = response.json()
        if news_data["status"] == "ok":
            articles = news_data["articles"]
            return [article["title"] for article in articles][:3]
        return ["Sorry, couldn't fetch news at the moment."]

    def speak_news(self, headlines):
        for headline in headlines:
            self.speak(headline)

    def get_weather(self, city=None):
        if not city:
            self.speak("Please specify the city name.")
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                city = self.recognizer.recognize_google(audio)
        api_key = '6f64eb4c45a74139b3154fb1508327a1'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            desc = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            self.speak(f"The weather in {city} is {desc}. Temperature is {temp}°C with {humidity}% humidity.")
        else:
            self.speak("Sorry, I couldn't fetch the weather.")

    def open_math_gui(self):
        def search_answer():
            question = entry.get("1.0", tk.END).strip()
            try:
                prompt = f"Solve the following math problem: {question}"
                response = model.generate_content(prompt)
                result = response.text if hasattr(response, 'text') else "No result"
                result_var.set(result.strip())
            except Exception as e:
                result_var.set(f"Error: {e}")

        math_window = tk.Tk()
        math_window.title("Math Solver")
        tk.Label(math_window, text="Enter your math question:").pack(pady=10)
        entry = scrolledtext.ScrolledText(math_window, width=50, height=10)
        entry.pack(pady=10)
        result_var = tk.StringVar()
        tk.Button(math_window, text="Solve", command=search_answer).pack(pady=10)
        tk.Label(math_window, textvariable=result_var, wraplength=400).pack(pady=10)
        math_window.mainloop()

    def take_screenshot(self):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            self.speak("Screenshot saved as screenshot.png.")
        except:
            self.speak("Failed to take screenshot.")
def main():
    assistant = VirtualAssistant()
    assistant.speak("Voice activation requires...")
    assistant.listen_for_wake_word()
    try:
        while True:
            assistant.play_listening_tune()
            assistant.listen_for_command()
    except SystemExit:
        pass

if __name__ == "__main__":
    main()
