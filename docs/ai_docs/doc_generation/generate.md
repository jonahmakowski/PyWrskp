# Documentation for src/doc_generation/generate.py

**Script Overview**

This Python script generates formal documentation for a given Python script. It uses an AI model to generate the documentation and then converts the file paths accordingly.

**Functions and Classes**

### Functions

*   `generate_docs(file)`: Generates formal documentation for a given Python script.
    *   Parameters:
        *   `file`: The path to the Python script.
    *   Output: A string containing the generated documentation.

### Classes

*   `Client(host)`: Establishes a connection with an AI model endpoint.
    *   Parameters:
        *   `host`: The URL of the AI model endpoint.
    *   Output: A client object used to send requests to the AI model.

**Dependencies**

The script depends on the following external packages/modules:

*   `os` and `subprocess` for system-related tasks
*   `ollama` for interacting with the AI model

**Script Documentation**

```python
"""
Generates formal documentation for a given Python script using an AI model.
"""

import os
import subprocess
from ollama import Client

# AI model endpoint (Ollama, Llama.cpp, or API)
AI_ENDPOINT = "http://192.168.86.4:11434"

def get_modified_files():
    """
    Gets the list of modified files in the last commit.

    Returns:
        A list of file paths that have been modified.
    """
    git_diff_cmd = "git diff --name-only HEAD~1"
    return subprocess.check_output(git_diff_cmd.split()).decode().splitlines()

def filter_source_files(modified_files):
    """
    Filters files from /src/ that are Python or C++.

    Args:
        modified_files (list): A list of file paths that have been modified.

    Returns:
        A list of file paths that are Python or C++ source files.
    """
    return [f for f in modified_files if f.startswith("src/") and f.endswith((".py", ".cpp", ".js"))]

def generate_docs(client, file):
    """
    Generates formal documentation for a given Python script.

    Args:
        client (Client): The client object used to send requests to the AI model.
        file (str): The path to the Python script.

    Returns:
        A string containing the generated documentation.
    """
    # Read the source code
    with open(file, "r") as f:
        code = f.read()

    # Send the code to AI for documentation
    prompt = f"""Generate formal documentation for the following Python script. The documentation should include:
                 Summary: Provide a brief overview of what the script does in a concise and clear manner.
                 Functions and Classes: List all functions and classes defined in the script, along with: A short description of what each function/class does. The inputs each function/class takes (parameters). The output (return value) for each function/class.
                 Dependencies: List all external packages/modules that the script depends on.
                 The script to document is as follows:\n\n"""
    
    documentation = client.generate('llama3.2', prompt + code)['response']

    return documentation

def save_docs(file, documentation):
    """
    Saves the generated documentation to a file.

    Args:
        file (str): The path to the Python script.
        documentation (str): The generated documentation.
    """
    # Convert file path from /src/ to /docs/
    doc_path = file.replace("src/", "docs/").replace(".py", ".md").replace(".cpp", ".md").replace(".js", ".md")

    # Ensure parent directories exist
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)

    # Write the documentation to the mirrored docs folder
    with open(doc_path, "w") as f:
        f.write(f"# Documentation for {file}\n\n{documentation}")

def main():
    """
    The main function that generates formal documentation for a given Python script.
    """
    modified_files = get_modified_files()
    source_files = filter_source_files(modified_files)

    if not source_files:
        print("No source files modified. Skipping doc generation.")
        return

    client = Client(host=AI_ENDPOINT)

    for file in source_files:
        print(f"Generating docs for: {file}")

        documentation = generate_docs(client, file)
        save_docs(file, documentation)
        print('response:', documentation)

        if not documentation:
            print(f"⚠️ No documentation generated for {file}")
            continue

if __name__ == "__main__":
    main()
```

This script provides a clear and concise overview of how to generate formal documentation for a given Python script using an AI model.