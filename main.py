from flask import Flask, request, jsonify, render_template
from intelligent_ai import IntelligentAI

app = Flask(__name__)
ai = IntelligentAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.get_json().get("message", "")
    reply = ai.generate_response(message, user_id=0)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
