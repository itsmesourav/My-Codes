import pandas as pd
from models.model import AIDictionaryModel
from utils.helpers import load_data

def main():
    # Load the dataset
    dataset = load_data('data/dataset.csv')
    
    # Initialize the AI dictionary model
    dictionary_model = AIDictionaryModel(dataset)
    
    print("Welcome to the AI-Powered Dictionary!")
    
    while True:
        word = input("Enter a word to get its definition and synonyms (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        
        definition = dictionary_model.get_definition(word)
        synonyms = dictionary_model.get_synonyms(word)
        
        if definition:
            print(f"Definition of '{word}': {definition}")
        else:
            print(f"No definition found for '{word}'.")
        
        if synonyms:
            print(f"Synonyms of '{word}': {', '.join(synonyms)}")
        else:
            print(f"No synonyms found for '{word}'.")

if __name__ == "__main__":
    main()