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
            api_key = Config.get_openai_api_key()
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables.")
            return ChatOpenAI(model=self.model_name, api_key=api_key, temperature=0)
        elif self.model_name == 'gemini-pro':
            api_key = Config.get_gemini_api_key()
            if not api_key:
                raise ValueError("GEMINI_API_KEY not found in environment variables.")
            return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, convert_system_message_to_human=True, temperature=0)
        else:
            raise NotImplementedError(f"Model {self.model_name} not supported.")

    def generate_plantuml(self, prompt: str) -> str:
        if os.getenv("UML_GENERATOR_MODE") == "test":
            return """
@startuml
title Complex System UML Example

package "User Management" {
  class User {
    +id: int
    +name: string
    +email: string
    +login()
    +logout()
  }

  class Admin {
    +roleLevel: int
    +banUser(u: User)
  }

  User <|-- Admin
}

package "Product Catalog" {
  class Product {
    +id: int
    +title: string
    +price: float
    +getPriceWithTax()
  }

  class Category {
    +id: int
    +name: string
  }

  Category "1" -- "*" Product
}

package "Order System" {
  class Order {
    +id: int
    +total: float
    +checkout()
  }

  class OrderItem {
    +id: int
    +unitPrice: float
    +quantity: int
  }

  Order "1" -- "*" OrderItem
  Product "1" -- "*" OrderItem
}

package "Payment Service" {
  interface PaymentGateway {
    +makePayment(amount: float)
  }

  class RazorpayGateway {
    +makePayment(amount: float)
  }

  class PaypalGateway {
    +makePayment(amount: float)
  }

  PaymentGateway <|.. RazorpayGateway
  PaymentGateway <|.. PaypalGateway
}

User "1" -- "*" Order
Order "1" --> "1" PaymentGateway

@enduml
"""



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

