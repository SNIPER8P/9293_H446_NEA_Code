🐿️ Study Squirrel
Programming Language
Python
Requirements

Before running the program, install the following:

1. Python
Python 3.10 or above
Download from: https://www.python.org/downloads/

Make sure you tick “Add Python to PATH” during installation
2. Python Libraries

Open Command Prompt and run:

pip install customtkinter pillow ollama

These libraries handle the interface, images, and AI connection.

3. Local AI Service

This project uses a local AI model through:

Ollama

Steps to set it up:

Download and install Ollama:
https://ollama.com
Open Command Prompt and run:
ollama pull llama3
Leave Ollama running in the background before starting the app

After setup, no internet connection is needed.

How to Run
Download or extract the project folder
Open Command Prompt in the folder
Run:
python Main.py
External Services
Ollama is required to generate AI flashcards
It runs locally on your computer
No external servers or online APIs are used
Additional Hardware
No extra hardware is required
A standard computer with enough RAM to run the Ollama model is needed
8GB RAM is recommended for smooth performance
Notes
First run may be slower due to the AI model loading
If AI generation does not work, check that Ollama is running
All user data is stored locally in users.json
