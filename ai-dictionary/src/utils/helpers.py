def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Example preprocessing: remove any rows with missing values
    cleaned_data = data.dropna()
    return cleaned_data