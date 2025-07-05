from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask app on Render is working!'

@app.route('/test-vps')
def test_vps():
    try:
        payload = {
            "test": "connection from Render",
            "timestamp": "2025-07-05T12:00:00"
        }
        res = requests.post("http://82.208.20.218:5000/test-connection", json=payload, timeout=5)
        return jsonify({
            "status": "success",
            "response_text": res.text,
            "status_code": res.status_code
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        })
