import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_model(data_path):
    data = pd.read_csv(data_path)
    X = data[['user_id', 'item_id']]
    y = data['rating']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model trained and saved to model.pkl")

if __name__ == "__main__":
    train_model('data/preprocessed_data.csv')