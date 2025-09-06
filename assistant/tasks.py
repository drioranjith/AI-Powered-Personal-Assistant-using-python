tasks = []
reminders = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added."

def list_tasks():
    if not tasks:
        return "No tasks in your to-do list."
    return "Tasks: " + ", ".join(tasks)

def set_reminder(text, time):
    reminders.append({"text": text, "time": time})
    return f"Reminder set for '{text}' at {time}."

def list_reminders():
    if not reminders:
        return "No reminders set."
    out = []
    for r in reminders:
        out.append(f"{r['text']} at {r['time']}")
    return "Reminders: " + "; ".join(out)
from dotenv import load_dotenv
import os