# Git Command Executor

This is a Python script that allows you to execute Git commands based on voice recognition.

## How to Use

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- [Spacy](https://spacy.io/): You can install it via `pip install spacy`
- [SpeechRecognition](https://github.com/Uberi/speech_recognition): You can install it via `pip install SpeechRecognition`

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.

### Usage

1. Run the `Main.py` script.
2. The script will prompt you to speak.
3. Speak your command (e.g., "commit this change").
4. The script will recognize your command and execute the corresponding Git action.

## Components

### `Main.py`

This is the main script that orchestrates the entire process. It listens to your voice command, processes it, and executes the appropriate Git action.

### `git_commit.py`

Contains functions related to committing changes using Git. It utilizes subprocess to execute Git commands and SpaCy for natural language processing to extract commit messages.

### `git_log.py`

Contains functions related to retrieving Git log. It uses subprocess to execute Git commands to retrieve the log.

### `process_command.py`

Handles the processing of voice commands. It uses SpaCy for natural language processing to extract verbs from the recognized text.

### `recognizeVoice.py`

This module handles voice recognition using the SpeechRecognition library. It listens to your voice command and converts it into text.
