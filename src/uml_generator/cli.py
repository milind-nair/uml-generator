import argparse
from .llm_provider import LLMProvider
from .uml_render import render_plantuml

def main():
    parser = argparse.ArgumentParser(description="Generate a UML diagram from a natural language description.")
    parser.add_argument("prompt", help="The natural language description of the UML diagram.")
    parser.add_argument("-o", "--output", help="The output file path for the generated diagram (e.g., diagram.png).")
    args = parser.parse_args()

    # Generate PlantUML code
    llm_provider = LLMProvider()
    plantuml_code = llm_provider.generate_plantuml(args.prompt)

    # Render the diagram
    if args.output:
        render_plantuml(plantuml_code, args.output)
        print(f"Diagram saved to {args.output}")
    else:
        print("--- PlantUML Code ---")
        print(plantuml_code)
        print("---------------------")
        print("\nTo save the diagram, use the -o/--output flag.")
        print("Example: uml-generator \"a simple class diagram\" -o diagram.png")
