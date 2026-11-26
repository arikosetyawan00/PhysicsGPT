import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120"

TEMPERATURE = 0.4

MAX_COMPLETION_TOKENS = 4096
