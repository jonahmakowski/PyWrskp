# Documentation for src/docGeneration/generate.py

**Python Script Documentation**
=============================

### Program Overview

The provided Python script is designed to generate documentation for source code files. It uses the Ollama API to analyze the code and produce high-quality documentation.

### Table of Contents

*   [Function 1](#function-1): `load_from_file`
    *   Description: Loads a prompt from a file.
    *   Parameters:
        *   `file_path` (str): The path to the file containing the prompt.
    *   Returns: The loaded prompt.

*   [Class 1](#class-1): `Client`
    *   Description: A client class for interacting with the Ollama API.
    *   [Method 1](##method-1): `generate`
        *   Description: Generates documentation for a given source code file.
        *   Parameters:
            *   `model_name` (str): The name of the AI model to use.
            *   `prompt` (str): The prompt for the AI model to generate documentation from.
            *   `source_code` (str): The source code to be analyzed and documented.

### Detailed Function Descriptions

#### Function 1: `load_from_file`

**Description**: Loads a prompt from a file.

**Parameters**

*   `file_path` (str, required): The path to the file containing the prompt.

**Returns**: The loaded prompt.

```python
def load_from_file(file_path):
    """
    Loads a prompt from a file.

    Args:
        file_path (str): The path to the file containing the prompt.

    Returns:
        str: The loaded prompt.
    """
    with open(file_path, "r") as f:
        return f.read()
```

#### Function 1: `generate`

**Description**: Generates documentation for a given source code file.

**Parameters**

*   `model_name` (str, required): The name of the AI model to use.
*   `prompt` (str, required): The prompt for the AI model to generate documentation from.
*   `source_code` (str, required): The source code to be analyzed and documented.

**Returns**: The generated documentation.

```python
class Client:
    def __init__(self, host):
        """
        Initializes a client object for interacting with the Ollama API.

        Args:
            host (str): The endpoint URL of the Ollama API.
        """
        self.host = host

    def generate(self, model_name, prompt, source_code):
        """
        Generates documentation for a given source code file.

        Args:
            model_name (str): The name of the AI model to use.
            prompt (str): The prompt for the AI model to generate documentation from.
            source_code (str): The source code to be analyzed and documented.

        Returns:
            str: The generated documentation.
        """
        # Construct API request payload
        payload = {
            "prompt": prompt + source_code,
            "model_name": model_name
        }

        # Send API request
        response = requests.post(self.host, json=payload)

        # Extract and return generated documentation
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception(f"Failed to generate documentation: {response.text}")
```

### Example Usage

```python
# Load prompt from file
prompt = load_from_file("src/docGeneration/prompt.md")

# Create client object for Ollama API
client = Client("http://192.168.86.4:11434")

# Generate documentation for source code file
generated_docs = client.generate("llama3.2", prompt, open("source_code.py").read())

# Save generated documentation to file
with open("documentation.md", "w") as f:
    f.write(generated_docs)
```