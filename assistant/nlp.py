import re
from datetime import datetime

def parse_intent(text):
    text = text.lower().strip()

    # Weather intent
    if "weather" in text:
        location_match = re.findall(r"weather in ([\w\s]+(?:, [\w\s]+)?)", text)
        if location_match:
            location = location_match[0].strip()
            location = ", ".join([part.strip().title() for part in location.split(",")])
        else:
            location = "London"
        return "weather", {"city": location}

    # News intent
    elif "news" in text or "headlines" in text:
        return "news", {}

    # Search intent
    elif "search" in text:
        query = text.split("search", 1)[-1].strip()
        return "search", {"query": query}

    # Add task intent
    elif "add task" in text:
        task = text.split("add task", 1)[-1].strip()
        return "add_task", {"task": task}

    # List tasks intent
    elif "list task" in text:
        return "list_task", {}

    # Reminder intent
    elif "remind me" in text:
        match = re.search(r"remind me (?:to )?(.+?)(?: at ([\d:apm ]+))?$", text)
        if match:
            reminder_text = match.group(1).strip()
            reminder_time = match.group(2).strip() if match.group(2) else "unspecified time"
            return "set_reminder", {"text": reminder_text, "time": reminder_time}
        else:
            return "remind", {}

    # List reminders intent
    elif "list reminders" in text:
        return "list_reminders", {}

    # Calculation intent (detect arithmetic keywords or symbols)
    elif any(op in text for op in ['+', '-', '*', '/', 'calculate', 'plus', 'minus', 'multiple', 'divided by']):
        expression = None
        calc_match = re.search(r'calculate (.+)', text)
        if calc_match:
            expression = calc_match.group(1)
        else:
            expression = text
        return "calculate", {"expression": expression}
    
    # Date and day intent (detect keywords)
    elif any(word in text for word in ["date", "day", "time", "today"]):
        return "datetime", {}
    

    # Exit intent
    elif "exit" in text or "quit" in text:
        return "exit", {}

    # Fallback
    return None, {}
