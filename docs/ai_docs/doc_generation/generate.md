# Documentation for src/doc_generation/generate.py

**Python Script Documentation**
================================

**Summary**
-----------

This script is designed to generate formal documentation for a Python script based on its source code. It utilizes the Ollama AI model to generate documentation in a specific format.

**Functions and Classes**
-------------------------

### `Client` class

*   **Description:** This class represents a connection to an Ollama AI endpoint.
*   **Parameters:**
    *   `host`: The URL of the Ollama AI endpoint (required)
*   **Return Value:** An instance of the `Client` class, which can be used to send requests to the Ollama API.

### `generate` method

*   **Description:** This method sends a prompt and code snippet to the Ollama AI model for documentation generation.
*   **Parameters:**
    *   `model`: The version of the Ollama model to use (required)
    *   `prompt`: A string containing the prompt for the documentation generation task
    *   `code`: A string containing the code snippet to generate documentation for
*   **Return Value:** A dictionary containing the generated documentation response

**Dependencies**
----------------

This script depends on the following external packages/modules:

*   `os` (built-in Python module)
*   `subprocess` (built-in Python module)
*   `ollama` (external library)

**Code**
------

```python
import os
import subprocess
from ollama import Client

# AI model endpoint (Ollama, Llama.cpp, or API)
AI_ENDPOINT = "http://192.168.86.4:11434"

# Get list of modified files in the last commit
git_diff_cmd = "git diff --name-only HEAD~1"
modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()

print("Modified files:", modified_files)

# Filter files from /src/ that are Python or C++
source_files = [f for f in modified_files if f.startswith("src/") and f.endswith((".py", ".cpp", ".js"))]

print("Source files:", source_files)

if not source_files:
    print("No source files modified. Skipping doc generation.")
    exit(0)

# Initialize the Ollama client
client = Client(
    host=AI_ENDPOINT,
)

for file in source_files:
    print(f"Generating docs for: {file}")

    # Read the source code
    with open(file, "r") as f:
        code = f.read()

    # Send the code to AI for documentation
    prompt = f"""Generate formal documentation for the following Python script. The documentation should include:
                 Summary: Provide a brief overview of what the script does in a concise and clear manner.
                 Functions and Classes: List all functions and classes defined in the script, along with: A short description of what each function/class does. The inputs each function/class takes (parameters). The output (return value) for each function/class.
                 Dependencies: List all external packages/modules that the script depends on.
                 Include the entire code in the documentation, and add comments as nessary, however, don't modify the code in any way.
                 The script to document is as follows:\n\n"""
    
    # Generate documentation using the Ollama API
    documentation = client.generate('llama3.2', prompt + code)['response']

    print('response:', documentation)

    if not documentation:
        print(f"⚠️ No documentation generated for {file}")
        continue

    # Convert file path from /src/ to /docs/
    doc_path = file.replace("src/", "docs/ai_docs/").replace(".py", ".md").replace(".cpp", ".md").replace(".js", ".md")

    # Ensure parent directories exist
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)

    # Write the documentation to the mirrored docs folder
    with open(doc_path, "w") as f:
        f.write(f"# Documentation for {file}\n\n{documentation}")

    print(f"✅ Saved docs: {doc_path}")
```

Note that the script assumes that the `ollama` library is installed and available. If you encounter any issues during execution, please ensure that the library is properly installed and configured.