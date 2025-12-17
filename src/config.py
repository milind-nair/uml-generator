import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for the UML generator agent."""
    # Supported models: 'gemini-pro', 'openai-gpt-4', etc.
    MODEL = os.getenv('UML_AGENT_MODEL', 'gemini-pro')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

    @classmethod
    def get_model(cls):
        return cls.MODEL

    @classmethod
    def get_api_key(cls):
        if cls.MODEL == 'gemini-pro':
            return cls.GEMINI_API_KEY
        elif cls.MODEL.startswith('openai'):
            return cls.OPENAI_API_KEY
        return ''
