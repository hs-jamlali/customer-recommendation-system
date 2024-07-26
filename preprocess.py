import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['user_id'] = df['user_id'].astype('category').cat.codes
    df['item_id'] = df['item_id'].astype('category').cat.codes
    return df

if __name__ == "__main__":
    data = preprocess_data('data/sample_data.csv')
    data.to_csv('data/preprocessed_data.csv', index=False)
    print("Data preprocessed and saved to data/preprocessed_data.csv")