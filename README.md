# LLM ChatBot Function

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/simonpierreboucher/llm-chatbot-function)](https://github.com/simonpierreboucher/llm-chatbot-function/issues)
[![GitHub Forks](https://img.shields.io/github/forks/simonpierreboucher/llm-chatbot-function)](https://github.com/simonpierreboucher/llm-chatbot-function/network)
[![GitHub Stars](https://img.shields.io/github/stars/simonpierreboucher/llm-chatbot-function)](https://github.com/simonpierreboucher/llm-chatbot-function/stargazers)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Models Supported](#models-supported)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Using the `ChatBot` Class](#using-the-chatbot-class)
  - [Running the Jupyter Notebook](#running-the-jupyter-notebook)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

In the rapidly evolving landscape of artificial intelligence, **Language Learning Models (LLMs)** have become indispensable tools for a myriad of applications, ranging from natural language understanding to advanced content generation. This repository provides a **modular and extensible framework** to generate and compare responses from a diverse set of LLMs provided by **OpenAI**, **Anthropic**, and **Mistral**.

At the heart of this project is the `ChatBot` class, a versatile Python class designed to interact seamlessly with multiple LLM providers. Whether you're conducting research, benchmarking model performance, or integrating LLMs into larger projects, the `ChatBot` class offers a unified interface to streamline your workflow.

## Features

- **Multi-Provider Support**: Interact with OpenAI, Anthropic, and Mistral models using a single class.
- **Flexible Configuration**: Customize parameters such as temperature, max tokens, and top_p for tailored responses.
- **Markdown Formatting**: Responses are formatted in Markdown for easy readability within Jupyter Notebooks.
- **Secure API Key Management**: Utilize environment variables to manage API keys securely.
- **Extensible Design**: Easily add support for additional LLM providers or models as needed.
- **Comprehensive Documentation**: Detailed instructions and examples to get you started quickly.

## Models Supported

### **OpenAI**
- `gpt-4o`
- `gpt-4o-mini`
- `gpt-4-turbo`
- `gpt-4`
- `gpt-3.5-turbo`

### **Anthropic**
- `claude-3-5-sonnet-20241022`
- `claude-3-opus-20240229`
- `claude-3-sonnet-20240229`
- `claude-3-haiku-20240307`

### **Mistral**
- `mistral-small-latest`
- `mistral-medium-latest`
- `mistral-large-latest`
- `open-mistral-7b`
- `open-mixtral-8x7b`
- `open-mixtral-8x22b`

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/simonpierreboucher/llm-chatbot-function.git
cd llm-chatbot-function
```

### Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv env
# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Setting Up API Keys

The project requires API keys from **OpenAI**, **Anthropic**, and **Mistral** to interact with their respective models. These keys should be stored securely in a `.env` file.

1. **Create a `.env` File**

   In the root directory of the project, create a file named `.env`:

   ```bash
   touch .env
   ```

2. **Add Your API Keys**

   Open the `.env` file in a text editor and add your API keys in the following format:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

   **Important**: Ensure that the `.env` file is **never** committed to version control. The provided `.gitignore` already excludes it, but double-check to prevent accidental exposure.

## Usage

### Using the `ChatBot` Class

The `ChatBot` class is the core component of this project, providing a unified interface to interact with multiple LLM providers. Below is a step-by-step guide on how to use the `ChatBot` class in your Python scripts.

#### 1. Import Necessary Modules

```python
import os
from IPython.display import display, Markdown
from llm_utils import ChatBot
```

#### 2. Initialize the `ChatBot` Class

Create instances of the `ChatBot` class for each provider and model you wish to interact with.

##### **Example for OpenAI**

```python
# Initialize ChatBot with OpenAI
bot_openai = ChatBot(
    provider="openai",
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1500,
    top_p=0.9
)
```

##### **Example for Anthropic**

```python
# Initialize ChatBot with Anthropic
bot_anthropic = ChatBot(
    provider="anthropic",
    model="claude-3-5-sonnet-20240620",
    temperature=0.7,
    max_tokens=1500,
    top_p=0.9
)
```

##### **Example for Mistral**

```python
# Initialize ChatBot with Mistral
bot_mistral = ChatBot(
    provider="mistral",
    model="mistral-small-latest",
    temperature=0.7,
    max_tokens=1500,
    top_p=0.9
)
```

#### 3. Generate Responses

Use the `get_response` method to send user inputs and receive formatted responses.

##### **Example Usage**

```python
# Get a response from OpenAI
user_input_openai = "Can you suggest 5 dinner ideas for this week?"
response_openai = bot_openai.get_response(user_input_openai)
display(Markdown(response_openai))

# Get a response from Anthropic
user_input_anthropic = "Explain the concept of quantum entanglement and its implications for understanding causality."
response_anthropic = bot_anthropic.get_response(user_input_anthropic)
display(Markdown(response_anthropic))

# Get a response from Mistral
user_input_mistral = "Explain the concept of quantum entanglement and how it challenges classical notions of locality and realism. What are the implications of entanglement for our understanding of causality and information transfer?"
response_mistral = bot_mistral.get_response(user_input_mistral)
display(Markdown(response_mistral))
```

### Running the Jupyter Notebook

An example Jupyter Notebook (`example.ipynb`) is provided to demonstrate how to use the `ChatBot` class with all supported models. Follow the steps below to run the notebook and interact with the models.

1. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

2. **Open `example.ipynb`**

   Navigate to the `example.ipynb` file in the Jupyter interface and run the cells sequentially to generate and view responses from each model.

## Examples

Below is an example of how to use the `ChatBot` class with multiple models, performing **three exchanges** with each provider: **OpenAI**, **Anthropic**, and **Mistral**.

```python
import os
from IPython.display import display, Markdown
from llm_utils import ChatBot

# Initialize ChatBot instances for each provider and model
bot_openai = ChatBot(
    provider="openai",
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1500,
    top_p=0.9
)

bot_anthropic = ChatBot(
    provider="anthropic",
    model="claude-3-5-sonnet-20240620",
    temperature=0.7,
    max_tokens=1500,
    top_p=0.9
)

bot_mistral = ChatBot(
    provider="mistral",
    model="mistral-small-latest",
    temperature=0.7,
    max_tokens=1500,
    top_p=0.9
)

# Define user inputs for each provider
user_inputs_openai = [
    "Can you suggest 5 dinner ideas for this week?",
    "What are the key differences between supervised and unsupervised learning?",
    "Explain the theory of relativity in simple terms."
]

user_inputs_anthropic = [
    "Explain the concept of quantum entanglement and its implications for understanding causality.",
    "What are the ethical considerations of artificial intelligence in healthcare?",
    "Describe the process of photosynthesis in plants."
]

user_inputs_mistral = [
    "Explain the concept of quantum entanglement and how it challenges classical notions of locality and realism. What are the implications of entanglement for our understanding of causality and information transfer?",
    "What advancements have been made in renewable energy technologies in the past decade?",
    "Describe the main causes and effects of the Great Depression."
]

# Perform three exchanges with OpenAI
for idx, user_input in enumerate(user_inputs_openai, 1):
    response = bot_openai.get_response(user_input)
    display(Markdown(f"### OpenAI Exchange {idx}"))
    display(Markdown(response))
    display(Markdown("---"))  # Separator for readability

# Perform three exchanges with Anthropic
for idx, user_input in enumerate(user_inputs_anthropic, 1):
    response = bot_anthropic.get_response(user_input)
    display(Markdown(f"### Anthropic Exchange {idx}"))
    display(Markdown(response))
    display(Markdown("---"))  # Separator for readability

# Perform three exchanges with Mistral
for idx, user_input in enumerate(user_inputs_mistral, 1):
    response = bot_mistral.get_response(user_input)
    display(Markdown(f"### Mistral Exchange {idx}"))
    display(Markdown(response))
    display(Markdown("---"))  # Separator for readability
```

### Explanation of the Example

1. **Initialization**:
   - Instances of the `ChatBot` class are created for each provider (**OpenAI**, **Anthropic**, **Mistral**) with their respective models and configurations.

2. **Defining User Inputs**:
   - Three distinct user inputs are defined for each provider to initiate meaningful conversations.

3. **Generating and Displaying Responses**:
   - For each user input, the `get_response` method is called to generate a response from the corresponding model.
   - The responses are displayed in a formatted Markdown style for easy readability.
   - Separators (`---`) are used to distinguish between different exchanges and providers.

## Contributing

Contributions are welcome! Whether you're reporting a bug, suggesting a feature, or improving the documentation, your input is valuable.

### Steps to Contribute

1. **Fork the Repository**

   Click the "Fork" button at the top right of the repository page to create your own fork.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your_username/llm-chatbot-function.git
   cd llm-chatbot-function
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes**

   Implement your feature, fix bugs, or update documentation.

5. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Add detailed explanation for quantum entanglement"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request**

   Navigate to the original repository and click "Compare & pull request". Provide a clear description of your changes.

### Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions within the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions, suggestions, or feedback, please open an issue on [GitHub Issues](https://github.com/simonpierreboucher/llm-chatbot-function/issues) or contact [Simon Pierre Boucher](mailto:simon.pierre.boucher@example.com).

