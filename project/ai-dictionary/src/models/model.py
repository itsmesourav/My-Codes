class AIDictionaryModel:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = self.load_data()
        self.word_definitions = self.process_data()

    def load_data(self):
        import pandas as pd
        return pd.read_csv(self.dataset_path)

    def process_data(self):
        word_definitions = {}
        for index, row in self.data.iterrows():
            word = row['word']
            definition = row['definition']
            synonyms = row['synonyms'].split(';') if 'synonyms' in row else []
            word_definitions[word] = {'definition': definition, 'synonyms': synonyms}
        return word_definitions

    def get_definition(self, word):
        return self.word_definitions.get(word, {}).get('definition', 'Definition not found.')

    def get_synonyms(self, word):
        return self.word_definitions.get(word, {}).get('synonyms', 'No synonyms found.')