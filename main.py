from assistant.voice import listen, speak
from assistant.api import get_weather, google_search, get_news
from assistant.nlp import parse_intent
from assistant.tasks import add_task, list_tasks, set_reminder, list_reminders
import re
from datetime import datetime

def eval_expression(expr):
    expr = expr.lower()
    expr = expr.replace('plus', '+').replace('minus', '-').replace('multiple', '*').replace('divided by', '/')
    expr = re.sub(r'[^0-9\.\+\-\*\/\(\) ]', '', expr)
    try:
        # Safe eval for basic arithmetic
        return str(eval(expr))
    except Exception:
        return "Sorry, I cannot calculate that."

def main():
    speak("Hello! I'm your personal AI assistant. How can I help?")
    while True:
        command = listen()
        intent, params = parse_intent(command)

        if intent == "weather":
            city = params.get("city", "").strip()
            if not city:
                speak("Please tell me the city and country for the weather.")
                city = listen().strip()
            if city:
                response = get_weather(city)
            else:
                response = "Sorry, I didn't get the location for weather."

        elif intent == "news":
            response = get_news()

        elif intent == "search":
            query = params.get("query", "")
            if query:
                response = google_search(query)
            else:
                response = "Please provide a search query."

        elif intent == "add_task":
            task = params.get("task", "")
            if task:
                response = add_task(task)
            else:
                response = "Please specify a task to add."

        elif intent == "list_tasks":
            response = list_tasks()

        elif intent == "set_reminder":
            reminder_text = params.get("text")
            reminder_time = params.get("time", "unspecified time")
            if reminder_text:
                response = set_reminder(reminder_text, reminder_time)
            else:
                response = "I couldn't understand the reminder details. Please try again."

        elif intent == "remind":
            response = "Please tell me what to remind you and when, for example, 'remind me to call mom at 6 pm'."

        elif intent == "list_reminders":
            response = list_reminders()

        elif intent == "calculate":
            expression = params.get("expression", "")
            if expression:
                response = eval_expression(expression)
            else:
                response = "Please provide an expression to calculate."

        elif intent == "datetime":
            now = datetime.now()
            day_name = now.strftime("%A")
            date_str = now.strftime("%B %d, %Y")
            response = f"Today is {day_name}, {date_str}."

        elif intent == "exit":
            speak("Goodbye!")
            break

        else:
            response = "Sorry, I didn't get that."

        speak(response)


if __name__ == "__main__":
    main()
