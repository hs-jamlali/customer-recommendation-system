# Customer Recommendation System

This project is a simple customer recommendation system built with Python(use linear regression). It preprocesses data, trains a machine learning model, and serves predictions via a Flask API.

## Setup

1. Install dependencies:
   ```
   pip install pandas scikit-learn flask
   ```

2. Preprocess the data:
   ```
   python preprocess.py
   ```

3. Train the model:
   ```
   python train_model.py
   ```

4. Run the Flask app:
   ```
   python app.py
   ```

## Usage

Send a POST request to `/predict` with JSON data:
   ```
   python post.py
   ```
   
```json
{
  "user_id": 0,
  "item_id": 1
}
```