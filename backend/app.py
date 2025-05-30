import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # To allow requests from the frontend

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY:", GROQ_API_KEY)  # To confirm the key is read correctly

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": "You are a helpful general ai assistant."},
                    {"role": "user", "content": user_input}
                ]
            }
        )
        
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text}")

        if response.ok:
            result = response.json()
            reply = result["choices"][0]["message"]["content"]
            return jsonify({"reply": reply})
        else:
            print("Error status code:", response.status_code)
            print("Error response body:", response.text)
            return jsonify({"error": "Error from Groq API", "details": response.text}), 500

    except Exception as e:
        print("Error in /chat endpoint:", e)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)