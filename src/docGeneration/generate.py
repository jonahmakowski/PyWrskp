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
    if not os.path.exists(file):
        print(f"⚠️ Source file not found: {file}")
        continue

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
