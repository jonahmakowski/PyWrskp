# Documentation for src/doc_generation/generate.py

**Documentation**

### Summary

This script generates formal documentation for a given Python script using the Ollama AI model. It identifies modified files in the last commit, filters out source files that are not Python or C++, and then uses Ollama to generate documentation for each source file.

### Functions and Classes

#### `Client`

*   **Description:** A class representing a connection to an Ollama AI model.
*   **Inputs:**
    *   `host`: The endpoint of the AI model (e.g., "http://192.168.86.4:11434").
*   **Output:** The response from the AI model, which is a dictionary containing the generated documentation.

#### `generate`

*   **Description:** A function that sends the source code to the Ollama AI model for documentation generation.
*   **Inputs:**
    *   `prompt`: The prompt provided to the AI model (required).
    *   `code`: The source code of the Python script (required).
*   **Output:** The response from the AI model, which is a dictionary containing the generated documentation.

#### `Client.generate`

*   **Description:** A function that generates documentation for a given Python script using Ollama.
*   **Inputs:**
    *   `prompt`: The prompt provided to the AI model (required).
    *   `code`: The source code of the Python script (required).
*   **Output:** The response from the AI model, which is a dictionary containing the generated documentation.

### Dependencies

The script depends on the following external packages/modules:

*   `os` : For interacting with the operating system and file system.
*   `subprocess` : For running shell commands and executing external processes.
*   `ollama` : For connecting to the Ollama AI model and generating documentation.

### Code

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

documentation_files = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk('docs/ai_docs/') for f in filenames]

print('Documentation files:', documentation_files)

# Remove old documentation for files that have been deleted
for doc_file in documentation_files:
    corresponding_source_file = doc_file.replace("docs/ai_docs/", "src/").replace(".md", ".py")
    if not os.path.exists(corresponding_source_file):
        print(f"Removing outdated documentation: {doc_file}")
        os.remove(doc_file)

# Generate New Documentation
if not source_files:
    print("No source files modified. Skipping doc generation.")
    exit(0)

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
                 Include the entire code in the documentation, and add comments, however, don't modify the actual code in any way.
                 The script to document is as follows:\n\n"""
    
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