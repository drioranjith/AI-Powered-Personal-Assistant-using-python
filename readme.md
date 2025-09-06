# AI-Powered Personal Assistant using python:
    
 ## Project Overview

This Python-based AI assistant interacts fully through voice commands and responses. It listens to spoken user input, understands natural language intents, and replies via speech synthesis. The assistant provides functionalities including:

Real-time weather updates for any location.

Latest news headlines.

Google search queries.

Task and reminder management.

Basic math calculations.

Current date and day information.

It is designed for hands-free operation, requiring no text input or display for interaction.

## Key Features:

Speech-to-text input and text-to-speech output using SpeechRecognition, gTTS, and Pygame.

Integration with external APIs such as OpenWeather and NewsAPI.

Conversational natural language understanding for diverse queries.

Modular and extensible architecture.


## Features
- Answer questions (Live weather, calculations, Day To Day Live News, Google Search)
- Manage to-do and reminders
- Conversational NLP parsing
- Speech-to-speech (Google)
- Integrates OpenWeather API ,Google Search API AND NEWS API 
- Easy to add new skills and APIs

## structure of the Complete file


AI_Assistant/
│
├── main.py              # Main driver script
├── assistant/
│   ├── __init__.py      # Assistant core functions
│   ├── nlp.py           # NLP utilities (e.g. intent, sentiment)
│   ├── tasks.py         # To-do and reminders management
│   ├── api.py           # External APIs (weather, Google search)
│   ├── voice.py         # Speech-to-text and text-to-speech
│   └── personal.py      # User data, basic memory
├── config.py            # API keys and config variables
├── requirements.txt     # Project Python dependencies
├── README.md            # Setup documentation
└── .env                 # Secret API keys: GOOGLE, OPENWEATHER, NEWS 


## Setup & Installation (It's a Personal Assignment )
  ## Add Environment Varables
    create .env file in project:

      GOOGLE_API_KEY="YOUR_API_KEY"
      OPENWEATHER_API_KEY="YOUR_API_KEY"
      NEWS_API_KEY="YOUR_API_KEY"

## install the Requriments for the Project
    pip install -r requirements.txt

## Run the Project
 python main.py

## specific command to Get Reply:(the below commands are example in this type u can ask anything to assistent)
1. What’s the weather of (any state and country)

2. Give me the latest news.

3. Add task submit report.

4. Remind me to call mom at 6 pm.

5.  for Calculate:
  . number plus number
  . number mins number
  . number multiple number 
  . number divided by number  

6. What day is it today?

7. what is date and day and time ?

## Usage (The network is need to run this code):

  speak -> the assistant Transcribes, process with NLP -> Respond with Voice  
                    (The answer is get by API Keys)

    Note:

        This is simple AI-Assistant for Paticular tasks 









