# LangChain AI Project

A Python project demonstrating the use of **LangChain** with Large Language Models (LLMs) to extract summaries and insights from textual information.

## Overview

This project leverages LangChain to create an AI-powered pipeline that:
- Accepts company information or text data as input
- Uses prompt templates to structure LLM requests
- Generates intelligent summaries and interesting facts from the provided information
- Supports multiple LLM backends (OpenAI's GPT or Local Ollama models)

## Features

- 🤖 **LLM Integration**: Support for both OpenAI's ChatOpenAI and local Ollama models
- 📝 **Prompt Templates**: Structured prompt engineering using LangChain's PromptTemplate
- ⚙️ **Flexible Configuration**: Easy switching between different LLM providers
- 🔄 **Chain Architecture**: Sequential processing using LangChain's chain operations
- 🔒 **Secure Environment**: Environment variable management with python-dotenv

## Requirements

- Python 3.11 or higher
- Dependencies as specified in `pyproject.toml`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LangChain-AI-Project
```

2. Install dependencies using pip:
```bash
pip install -r requirements.txt
```

Or with Poetry (if using pyproject.toml):
```bash
poetry install
```

### Dependencies

- `langchain>=1.3.6` - LangChain framework
- `langchain-openai>=1.3.0` - OpenAI integration
- `langchain-ollama>=1.1.0` - Ollama integration
- `python-dotenv>=1.2.2` - Environment variable management
- `black>=26.5.1` - Code formatter
- `isort>=8.0.1` - Import sorter

## Configuration

### Environment Variables

1. Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` and add your configuration:

```env
# For OpenAI
OPENAI_API_KEY=your_openai_api_key_here
### Quick Start

Run the main script to generate a summary and facts about a company:

```bash
python main.py
```

The script processes company information and returns:
1. A short summary of the company
2. Two interesting facts about the company

### Sample Examples

For comprehensive examples of different use cases, run:

```bash
python sample.py
```

This demonstrates:
- **Example 1**: Basic company summary with facts
- **Example 2**: Detailed company analysis
- **Example 3**: Industry impact and competitive analysis
- **Example 4**: Batch processing multiple companies
- **Example 5**: Temperature settings comparison (for creative vs deterministic outputs)
- **Example 6**: Error handling and provider fallbacks

### Customization

#### Using main.py
1. Edit the `information` variable with your desired text
2. Modify the `summary_template` to change what the LLM extracts
3. Switch LLM providers:

```python
# For OpenAI
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# For Local Ollama
llm = ChatOllama(temperature=0, model="gemma3:270m")
```

#### Using sample.py
The `sample.py` file includes a helper function to easily switch providers:

```python
# Use local Ollama
llm = get_llm("ollama")

# Use OpenAI
llm = get_llm("openai
The script processes company information and returns:
1. A short summary of the company
2. Two interesting facts about the company

### Customization

To analyze different companies or information:

1. Edit the `information` variable in `main.py` with your desired text
2. Modify the `summary_template` to change what the LLM should extract
3. Ssample.py            # Sample examples and use cases
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
├── .env.example         # Example environment variables template
└── .env                 # Environment variables (create from .env.example
# For OpenAI (uncomment and add API key)
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# For Local Ollama (default)
llm = ChatOllama(temperature=0, model="gemma3:270m")
```

## LLM Models

### OpenAI Models
- `gpt-3.5-turbo` - Fast and cost-effective
- `gpt-4` - More advanced reasoning

### Ollama Models
- `gemma3:270m` - Lightweight local model (default)
- `llama2` - General-purpose model
- Other available models in your Ollama installation

## Project Structure

```
LangChain-AI-Project/
├── main.py              # Main application script
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
└── .env                 # Environment variables (create as needed)
```

## How It Works

1. **Prompt Template**: Defines the structure of the request to the LLM
2. **LLM Chain**: Connects the prompt template to the language model
3. **Invocation**: Passes company information through the chain
4. **Output**: Returns AI-generated summary and facts

## Temperature Parameter

The `temperature=0` setting means the LLM produces deterministic, focused responses. Adjust this value:
- `0` - Deterministic responses (recommended for summaries)
- `0.5-0.7` - Balanced creativity and consistency
- `1.0+` - More creative and random responses
Examples Included

### main.py
Basic example demonstrating:
- Loading environment variables
- Creating prompt templates
- Using ChatOllama or ChatOpenAI
- Chaining prompts with LLMs
- Processing company information

### sample.py
Advanced examples including:
- Multiple analysis approaches
- Batch processing workflows
- Temperature comparison (creativity levels)
- Error handling and provider fallbacks
- Helper functions for LLM management

## Future Enhancements

- [ ] Support for multiple input file formats (JSON, CSV, PDF)
- [ ] Advanced prompt engineering techniques (few-shot, chain-of-thought)
- [ ] Web interface for easy interaction
- [ ] API endpoint for remote access
- [ ] Configuration file for LLM settings
- [ ] Unit tests and integration tests
- [ ] CLI interface with argument parsing
- [ ] Support for additional LLM providers (HuggingFace, Anthropic)
- [ ] Caching and prompt optimization
- [ ] Multi-step reasoning chains`
- Ensure the model is available: `ollama list`
- Pull model if needed: `ollama pull gemma3:270m`

### Import errors
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
- Verify Python version is 3.11 or higher: `python --version`

## Code Quality

The project uses:
- **Black** - Code formatting
- **isort** - Import organization

Format your code:
```bash
black main.py
isort main.py
```

## Future Enhancements

- [ ] Support for multiple input file formats
- [ ] Advanced prompt engineering techniques
- [ ] Batch processing capabilities
- [ ] API endpoint for remote access
- [ ] Configuration file for LLM settings
- [ ] Unit tests and integration tests
- [ ] CLI interface with argument parsing

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please follow the code quality standards and submit pull requests.

## Support

For issues or questions, please open an issue in the repository or contact the project maintainers.
