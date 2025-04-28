from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Configura tu API Key de Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("La variable de entorno GEMINI_API_KEY no está configurada.")
genai.configure(api_key=api_key)

# Configuración del chatbot
SYSTEM_PROMPT = "Eres un asistente amigable que responde preguntas de manera clara y concisa."
GEMINI_MODEL = "models/gemini-1.5-pro"  # Modelo de Gemini
TEMPERATURE = 0.7

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").strip()
    print(f"Mensaje recibido: '{mensaje}'")

    try:
        # Generar la respuesta usando el modelo de Gemini
        model = genai.GenerativeModel(model_name=GEMINI_MODEL)
        response = model.generate_content(mensaje)
        respuesta_texto = response.text
    except Exception as e:
        print(f"Error al contactar Gemini: {e}")
        respuesta_texto = "El chatbot está temporalmente no disponible. Por favor, intenta más tarde."

    return jsonify({"respuesta": respuesta_texto})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)