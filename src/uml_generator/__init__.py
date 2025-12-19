from .llm_provider import LLMProvider
from .uml_render import render_plantuml

__all__ = ['generate']

def generate(prompt: str, output_path: str = None) -> str:
    """
    Generates a UML diagram from a natural language prompt.

    Args:
        prompt: The natural language description of the UML diagram.
        output_path: Optional. The file path to save the generated diagram.
                     If not provided, the diagram is not saved.

    Returns:
        The generated PlantUML code as a string.
    """
    llm_provider = LLMProvider()
    plantuml_code = llm_provider.generate_plantuml(prompt)

    if output_path:
        render_plantuml(plantuml_code, output_path)
        print(f"Diagram saved to {output_path}")

    return plantuml_code
