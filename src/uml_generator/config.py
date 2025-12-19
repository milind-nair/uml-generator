import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for the UML generator agent."""
    
    MODEL = os.getenv('UML_AGENT_MODEL', 'gemini-pro')

    @classmethod
    def get_model(cls):
        return cls.MODEL
