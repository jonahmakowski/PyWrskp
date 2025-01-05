#!/bin/bash
#set -e  # Exit on error

cd ./app

echo "Starting ollama"
nohup ollama serve > ollama.log 2>&1 &

echo "Waiting for ollama to start..."
until curl -s http://localhost:11434 > /dev/null; do
    sleep 1
done
echo "Ollama is ready!"

echo "Starting get_news_data.py"
python get_news_data.py

echo "Starting ai_summary.py"
python ai_summary.py

echo "Starting main.py"
python main.py

echo "All scripts completed successfully."
