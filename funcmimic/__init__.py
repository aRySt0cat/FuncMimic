import os
from dotenv import load_dotenv
import openai

from .decorators import mimic

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

__all__ = ["mimic"]