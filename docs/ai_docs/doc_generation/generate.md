# Documentation for src/doc_generation/generate.py

**Formal Documentation**

**Summary**

This Python script generates formal documentation for a given Python script. It uses an AI model to provide a concise and clear overview of the script's functionality, including descriptions of functions and classes, dependencies, and code comments. The generated documentation is written in Markdown format.

**Functions and Classes**

*   `Client(host=AI_ENDPOINT)`: Constructs a new instance of the Ollama client, connecting to the specified AI model endpoint.
*   `subprocess.check_output(git_diff_cmd.split())`: Runs the specified Git diff command and returns its output as a bytes object, decoded into a string.
*   `os.makedirs(os.path.dirname(doc_path), exist_ok=True)`: Creates the parent directories for the documentation folder if they do not already exist.

**Dependencies**

The script depends on the following external packages/modules:

*   `os`
*   `subprocess`
*   `ollama` (AI model library)

**Code with Comments**

```python
import os  # Import the os module for file system operations
import subprocess  # Import the subprocess module for running shell commands
from ollama import Client  # Import the Ollama client class

# AI model endpoint (Ollama, Llama.cpp, or API)
AI_ENDPOINT = "http://192.168.86.4:11434"  # Specify the AI model endpoint URL

# Get list of modified files in the last commit using Git diff
git_diff_cmd = "git diff --name-only HEAD~1"  # Define the Git diff command
modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()  # Run the Git diff command and get its output

print("Modified files:", modified_files)  # Print the list of modified files

# Filter files from /src/ that are Python or C++
source_files = [f for f in modified_files if f.startswith("src/") and f.endswith((".py", ".cpp", ".js"))]  # Filter modified files based on file extensions

print("Source files:", source_files)  # Print the list of filtered source files

if not source_files:
    print("No source files modified. Skipping doc generation.")  # If no source files are found, exit without generating documentation
    exit(0)

# Create an instance of the Ollama client connected to the specified AI model endpoint
client = Client(
    host=AI_ENDPOINT,
)

for file in source_files:
    print(f"Generating docs for: {file}")  # Print a message indicating that documentation generation has started

    # Read the contents of the source code file
    with open(file, "r") as f:
        code = f.read()  # Read the source code into a variable

    # Construct a prompt to pass to the AI model for documentation generation
    prompt = f"""Generate formal documentation for the following Python script. The documentation should include:
                 Summary: Provide a brief overview of what the script does in a concise and clear manner.
                 Functions and Classes: List all functions and classes defined in the script, along with: A short description of what each function/class does. The inputs each function/class takes (parameters). The output (return value) for each function/class.
                 Dependencies: List all external packages/modules that the script depends on.
                 Include the entire code in the documentation, and add comments, however, don't modify the actual code in any way.
                 The script to document is as follows:\n\n"""
    
    # Use the Ollama client to generate documentation for the source code
    documentation = client.generate('llama3.2', prompt + code)['response']  # Generate documentation using the AI model

    print('response:', documentation)  # Print the generated documentation response

    if not documentation:
        print(f"⚠️ No documentation generated for {file}")  # If no documentation is found, print a warning message
        continue

    # Convert file path from /src/ to /docs/
    doc_path = file.replace("src/", "docs/ai_docs/").replace(".py", ".md").replace(".cpp", ".md").replace(".js", ".md")  # Construct the documentation file path

    # Ensure parent directories exist for the documentation folder
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)  # Create parent directories using the os module

    # Write the generated documentation to the mirrored docs folder
    with open(doc_path, "w") as f:
        f.write(f"# Documentation for {file}\n\n{documentation}")  # Write the documentation content to a file

    print(f"✅ Saved docs: {doc_path}")  # Print a message indicating that documentation has been saved successfully
```

This formal documentation provides an overview of the script's functionality, dependencies, and code structure. It also includes comments explaining each section of the code, making it easier for users to understand and maintain the script.