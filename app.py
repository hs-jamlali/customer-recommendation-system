from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_id = data['user_id']
    item_id = data['item_id']
    prediction = model.predict([[user_id, item_id]])
    return jsonify({'rating': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
