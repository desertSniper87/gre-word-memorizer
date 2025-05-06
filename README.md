# GRE Word Memorizer

A simple tool to help memorize GRE vocabulary words by fetching definitions and opening Google Images for visual association.

## Features

- Look up word definitions from a dictionary API
- Open a browser window with Google Images search for visual association
- Save word information to a local SQLite database
- View word definitions and examples

## Installation

1. Clone this repository
2. Install required dependencies:

```
pip install -r requirements.txt
```

## Usage

### Command Line Mode

Process a specific word:
```
python main.py ubiquitous
```

List all saved words:
```
python main.py list
```

### Interactive Mode

Start the application without arguments to enter interactive mode:
```
python main.py
```

In interactive mode, you can:
- Enter a word to process it
- Type `list` to see all saved words
- Type `exit` to quit the application

### How It Works

When you enter a word:
1. The app checks if the word already exists in the database
2. If not, it fetches the definition from the Dictionary API
3. It opens your default web browser with a Google Images search for the word
4. You can manually select and save any image that helps you remember the word
5. The word information is stored in the SQLite database

## API Credits

- Definitions: [Free Dictionary API](https://dictionaryapi.dev/)