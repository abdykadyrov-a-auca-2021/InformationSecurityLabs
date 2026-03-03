from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def receive_logs():
    data = request.get_json()
    logs = data.get('logs', '')
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("received_logs.txt", "a") as f:
        f.write(f"\n=== {timestamp} ===\n")
        f.write(logs + "\n")
    
    print(f"[{timestamp}] Received: {logs}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    print("Server running on http://localhost:9000")
    app.run(port=9000)
