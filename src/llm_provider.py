from src.config import Config

class LLMProvider:
    def __init__(self):
        self.model = Config.get_model()
        self.api_key = Config.get_api_key()

    def generate_plantuml(self, prompt: str) -> str:
        if self.model == 'gemini-pro':
            return self._call_gemini(prompt)
        elif self.model.startswith('openai'):
            return self._call_openai(prompt)
        else:
            raise NotImplementedError(f"Model {self.model} not supported.")

    def _call_gemini(self, prompt: str) -> str:
        # Gemini Pro API call for PlantUML generation
        import requests
        import json
        api_key = self.api_key
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in environment or config.")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key
        headers = {"Content-Type": "application/json"}
        system_prompt = (
            "You are an expert UML generator. "
            "Convert the following user request into PlantUML code. "
            "Respond ONLY with PlantUML code, nothing else."
        )
        data = {
            "contents": [
                {"role": "user", "parts": [
                    {"text": f"{system_prompt}\nRequest: {prompt}"}
                ]}
            ]
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
            response.raise_for_status()
            result = response.json()
            # Gemini returns candidates, get the first candidate's content
            plantuml_code = result["candidates"][0]["content"]["parts"][0]["text"]
            return plantuml_code.strip()
        except Exception as e:
            return f"@startuml\n' Error: {e}\n@enduml"

    def _call_openai(self, prompt: str) -> str:
        # Placeholder for OpenAI API call
        # Replace with actual OpenAI API integration
        return "@startuml\n' OpenAI output here\n@enduml"
