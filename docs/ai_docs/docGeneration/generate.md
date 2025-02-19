# Documentation for src/docGeneration/generate.py

**Script Documentation**

**Summary**

This script generates formal documentation for a given Python script. It uses an AI model to generate the documentation, which includes a concise summary of what the script does, functions and classes defined in the script, dependencies, and includes the entire code with comments.

**Functions and Classes**

### `Client`

*   **Description**: Represents a client that interacts with the AI model.
*   **Parameters**:
    *   `host`: The endpoint of the AI model (e.g., "http://192.168.86.4:11434").
*   **Return Value**: The generated documentation for the given prompt.

### `generate`

*   **Description**: Sends the source code to the AI model and generates formal documentation.
*   **Parameters**:
    *   `prompt`: A string that provides context for the documentation generation (e.g., a brief summary of what the script does).
    *   `code`: The source code of the Python script.
*   **Return Value**: The generated documentation for the given prompt.

### `subprocess.check_output`

*   **Description**: Runs a subprocess and captures its output.
*   **Parameters**:
    *   A command to run (e.g., "git diff --name-only HEAD~1").
*   **Return Value**: The output of the subprocess as a bytes object.

### `os.path.join`, `os.walk`, `os.makedirs`

*   **Description**: Helper functions for working with file paths and directories.
*   **Parameters**:
    *   Various file path components (e.g., directory paths, filename).

**Dependencies**

This script depends on the following external packages:

*   `os`: For interacting with the operating system and file system.
*   `subprocess`: For running subprocesses and capturing their output.
*   `ollama`: A Python library that interacts with the AI model.

```python
# Importing necessary modules
import os
import subprocess
from ollama import Client

# Defining constants
AI_ENDPOINT = "http://192.168.86.4:11434"

# Defining the command to get the list of modified files in the last commit
git_diff_cmd = "git diff --name-only HEAD~1"

# Getting the list of modified files
modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()

print("Modified files:", modified_files)

# Filtering Python and C++ source files from the list of modified files
source_files = [f for f in modified_files if f.startswith("src/") and f.endswith((".py", ".cpp", ".js"))]

print(f"{len(source_files)}; Source files:", source_files)

# Getting the list of documentation files
documentation_files = [os.path.join(dirpath, f) for (dirpath, dirnames, filenames) in os.walk('docs/ai_docs/') for f in filenames]

print(f"{len(documentation_files)}; Documentation files:", documentation_files)

# Removing old documentation for files that have been deleted
for doc_file in documentation_files:
    corresponding_source_file = doc_file.replace("docs/ai_docs/", "src/").replace(".md", ".py")
    if not os.path.exists(corresponding_source_file):
        print(f"Removing outdated documentation: {doc_file}")
        os.remove(doc_file)

# Generating new documentation
if not source_files:
    print("No source files modified. Skipping doc generation.")
    exit(0)

# Creating a client to interact with the AI model
client = Client(
    host=AI_ENDPOINT,
)

for file_num, file in enumerate(source_files):
    if not os.path.exists(file):
        print(f"{file_num} ⚠️ Source file not found: {file}")
        continue

    # Generating documentation for the current source file
    print(f"{file_num} Generating docs for: {file}")

    # Reading the source code
    with open(file, "r") as f:
        code = f.read()

    # Defining the prompt for generating documentation
    prompt = f"""Generate formal documentation for the following Python script. The documentation should include:
                 Summary: Provide a brief overview of what the script does in a concise and clear manner.
                 Functions and Classes: List all functions and classes defined in the script, along with: A short description of what each function/class does. The inputs each function/class takes (parameters). The output (return value) for each function/class.
                 Dependencies: List all external packages/modules that the script depends on.
                 Include the entire code in the documentation, and add comments, however, don't modify the actual code in any way.
                 The script to document is as follows:\n\n"""
    
    # Generating documentation using the AI model
    documentation = client.generate('llama3.2', prompt + code)['response']

    if not documentation:
        print(f"⚠️ No documentation generated for {file}")
        continue

    # Converting file path from /src/ to /docs/
    doc_path = file.replace("src/", "docs/ai_docs/").replace(".py", ".md").replace(".cpp", ".md").replace(".js", ".md")

    # Ensuring parent directories exist
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)

    # Writing the documentation to the mirrored docs folder
    with open(doc_path, "w") as f:
        f.write(f"# Documentation for {file}\n\n{documentation}")

    print(f"✅ Saved docs: {doc_path}")
```

This script uses an AI model to generate formal documentation for a given Python script. It first identifies the modified files in the last commit and filters out only the Python and C++ source files. Then, it generates new documentation for each of these source files using the AI model. Finally, it removes old documentation for files that have been deleted and saves the new documentation to the mirrored docs folder.