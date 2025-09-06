# You can import submodules here for easier access.
from .voice import listen, speak
from .api import get_weather, google_search
from .nlp import parse_intent
from .tasks import add_task, list_tasks, set_reminder, list_reminders

# Optional: Initialization code if needed for package setup.
from dotenv import load_dotenv
import os