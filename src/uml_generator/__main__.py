import argparse
from .llm_provider import LLMProvider
from .uml_render import render_plantuml

def main():
    parser = argparse.ArgumentParser(description="Generate UML diagrams from natural language.")
    parser.add_argument("-o", "--output", default="uml_diagram.png", help="Output file path for the UML diagram.")
    parser.add_argument("prompt", nargs="?", default=None, help="The prompt for the UML diagram. If not provided, the tool will prompt for input.")
    args = parser.parse_args()

    if args.prompt:
        user_input = args.prompt
    else:
        print("Enter your description for the UML diagram:")
        user_input = input()

    print("Generating UML diagram...")
    llm = LLMProvider()
    plantuml_code = llm.generate_plantuml(user_input)

    if not plantuml_code.strip().startswith("@startuml"):
        print("Error: The generated text is not valid PlantUML code.")
        print("Generated text:", plantuml_code)
        return

    print("\nGenerated PlantUML code:\n")
    print(plantuml_code)
    
    render_plantuml(plantuml_code, args.output)

if __name__ == "__main__":
    main()

