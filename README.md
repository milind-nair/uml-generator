# UML Generator AI Agent

A Python-based AI agent that converts natural language descriptions into UML diagrams using a configurable LLM (default: Gemini Pro). The output is PlantUML code, which is rendered as an image.

## Features

- Configurable LLM backend (Gemini Pro, OpenAI, etc.)
- Converts human input to PlantUML code
- Renders PlantUML code to PNG image

## Installation

1.  Install the package from PyPI:
    ```sh
    pip install uml-generator
    ```

2.  Set up your API keys in a `.env` file in your project directory:
    ```env
    # Set the model to 'gemini-pro' or an OpenAI model like 'gpt-4'
    UML_AGENT_MODEL=gemini-pro

    # Add your API keys
    GEMINI_API_KEY=your_gemini_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

## CLI Usage

Run the `uml-generator` command with your prompt.

To print the PlantUML code to the console:
```sh
uml-generator "A simple class diagram for a Dog"
```

To save the generated diagram to a file:
```sh
uml-generator "A simple class diagram for a Dog" -o dog_diagram.png
```

## Library Usage

You can also use `uml-generator` as a library in your own Python code:

```python
import uml_generator

# Generate PlantUML code and save the diagram to a file
prompt = "A class diagram for a simple shopping cart"
plantuml_code = uml_generator.generate(prompt, "shopping_cart.png")

print("--- Generated PlantUML Code ---")
print(plantuml_code)

# Or, generate the code without saving a file
prompt2 = "An activity diagram for making coffee"
plantuml_code_only = uml_generator.generate(prompt2)
print(plantuml_code_only)
```

## Developer Setup

If you want to contribute to the project, follow these steps:

1.  Clone the repository:
    ```sh
    git clone https://github.com/milind-nair/uml-generator.git
    cd uml-generator
    ```

2.  Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  Install the package in editable mode:
    ```sh
    pip install -e .
    ```

4.  Run the tests:
    ```sh
    python -m unittest discover -s tests
    ```

## Configuration

- Change the model by editing `UML_AGENT_MODEL` in your `.env` file.
- Supported models: `gemini-pro`, `openai/gpt-4`, etc.

## License

MIT
