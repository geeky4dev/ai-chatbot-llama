# list_models.py
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def listar_modelos():
    try:
        models = genai.list_models()
        for model in models:
            print(model.name)
    except Exception as e:
        print("Error al listar modelos:", e)

if __name__ == "__main__":
    listar_modelos()