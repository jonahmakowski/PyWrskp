ollama

nohup ollama serve &

ollama ps

ollama pull llama3.2

cat > Modelfile << EOF
# Use the 3B parameter, 2 GB base model file
FROM llama3.2
# Larger context window for page summaries
PARAMETER num_ctx 32768
# Lower temperature for more conservative sampling / less creative summaries
PARAMETER temperature 0.25
EOF

ollama create -f Modelfile llama3.2:ctx32k-t0.25
