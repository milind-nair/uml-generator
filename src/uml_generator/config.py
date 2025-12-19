import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for the UML generator agent."""

    MODEL = os.getenv('UML_AGENT_MODEL', 'gemini-pro')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    @classmethod
    def get_model(cls):
        return cls.MODEL

    @classmethod
    def get_openai_api_key(cls):
        return cls.OPENAI_API_KEY

    @classmethod
    def get_gemini_api_key(cls):
        return cls.GEMINI_API_KEY