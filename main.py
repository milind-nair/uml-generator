from src.llm_provider import LLMProvider
from src.uml_render import render_plantuml

def main():
    print("Enter your description for the UML diagram:")
    user_input = input()
    llm = LLMProvider()
    plantuml_code = llm.generate_plantuml(user_input)
    print("\nGenerated PlantUML code:\n")
    print(plantuml_code)
    render_plantuml(plantuml_code)

if __name__ == "__main__":
    main()
