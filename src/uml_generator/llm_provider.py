import os
from .config import Config
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage

class LLMProvider:
    def __init__(self):
        if os.getenv("UML_GENERATOR_MODE") == "test":
            self.llm = None
            self.model_name = "test"
            return

        self.model_name = Config.get_model()
        self.llm = self._get_llm()

    def _get_llm(self):
        if self.model_name.startswith('openai'):
            return ChatOpenAI(model=self.model_name, temperature=0)
        elif self.model_name == 'gemini-pro':
            return ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True, temperature=0)
        else:
            raise NotImplementedError(f"Model {self.model_name} not supported.")

    def generate_plantuml(self, prompt: str) -> str:
        if os.getenv("UML_GENERATOR_MODE") == "test":
            return "@startuml\nclass Car\n@enduml"

        system_prompt = (
            "You are an expert UML generator. "
            "Convert the following user request into PlantUML code. "
            "Respond ONLY with PlantUML code, nothing else."
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=prompt),
        ]
        try:
            response = self.llm.invoke(messages)
            return response.content.strip()
        except Exception as e:
            return f"@startuml\n' Error: {e}\n@enduml"

