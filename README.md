# UML Generator AI Agent

A Python-based AI agent that converts natural language descriptions into UML diagrams using a configurable LLM (default: Gemini Pro). The output is PlantUML code, which is rendered as an image.

## Features

- Configurable LLM backend (Gemini Pro, OpenAI, etc.)
- Converts human input to PlantUML code
- Renders PlantUML code to PNG image

## Project Structure

```
.
├── src/
│   ├── config.py
│   ├── llm_provider.py
│   ├── uml_render.py
│   └── main.py
├── requirements.txt
├── .env (optional, for API keys)
└── README.md
```

## Setup

1. Clone the repository and navigate to the project directory.
2. (Optional) Create a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your API keys in a `.env` file:
   ```env
   UML_AGENT_MODEL=gemini-pro
   GEMINI_API_KEY=your_gemini_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the main script and follow the prompt:

```sh
python src/main.py
```

## Configuration

- Change the model by editing `UML_AGENT_MODEL` in `.env` or `config.py`.
- Supported models: `gemini-pro`, `openai-gpt-4`, etc.

## License

MIT
