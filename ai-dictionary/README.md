# AI Dictionary

This project is an AI-powered dictionary that allows users to query definitions and synonyms of words using a machine learning model. The application is designed to provide quick and accurate responses based on a dataset of words, their meanings, and related terms.

## Features

- Retrieve definitions of words
- Get synonyms for words
- User-friendly interface for querying

## Project Structure

```
ai-dictionary
├── src
│   ├── main.py          # Entry point of the application
│   ├── models
│   │   └── model.py     # Contains the AIDictionaryModel class
│   ├── data
│   │   └── dataset.csv   # Dataset containing words, definitions, and synonyms
│   └── utils
│       └── helpers.py    # Utility functions for data processing
├── requirements.txt      # Project dependencies
├── .gitignore            # Files and directories to ignore by Git
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd ai-dictionary
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the prompts to enter a word and retrieve its definition or synonyms. 

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.