import google.generativeai as genai
import os

# Configura la API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def test_gemini():
    try:
        # Usa uno de los modelos listados
        model = genai.GenerativeModel(model_name='models/gemini-1.5-pro')
        response = model.generate_content("¿Quién ganó la Copa del Mundo 2022?")
        
        print("Respuesta de Gemini:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_gemini()
