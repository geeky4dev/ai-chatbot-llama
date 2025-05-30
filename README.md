# 💬 AI Chatbot Groq-Llama(Flask + React)

A lightweight AI-powered chatbot using **Groq API (model Llama3-8b-8192)**, with a beautiful frontend built in **React + Bootstrap** and a **Flask** backend. 
---

## 📸 Preview

![Chatbot Screenshot](screenshot.png) <!-- Optional: Replace with actual image if available -->

---

## 🧠 Features

- ✨ Chat with Groq available LLM models (e.g. Llama)
- 🎨 Beautiful and responsive UI (React + Bootstrap)
- ♻️ Full-stack architecture (Flask API + React Frontend)
- 🚀 Deployable to Render, Vercel, or local server

---

## 🚀 Project Structure

ai-chatbot-llama/
├── backend/ # Flask API using Groq-Llama
│ ├── app.py
│ └── ...
├── frontend/ # React + Vite + Bootstrap UI
│ ├── src/
│ └── ...
├── .gitignore
└── README.md

---

## ⚙️ Requirements
- Python 3.9+
- Node.js 18+
- Groq API Key
- Git + GitHub account

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```
git clone git@github.com:yourusername/ai-chatbot-llama.git
cd ai-chatbot-llama
2️⃣ Backend Setup (Flask + Groq API-llama)
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Create a .env file or export manually:

export GROQ_API_KEY="your_groq_api_key"
Start the backend:
python app.py
🟢 Running on: http://localhost:5001

3️⃣ Frontend Setup (React + Vite + Bootstrap)
In another terminal:
cd frontend
npm install
npm run dev
🟢 Running on: http://localhost:5173

🛠️ How to Use
Enter a message in the chatbox

Submit and get your AI-powered response

🔐 GitHub SSH Setup (Optional)
If you're using SSH with GitHub, update your remote:

git remote set-url origin git@github.com:yourusername/ai-chatbot-llama.git
Then push:

git push -u origin main
☁️ Deployment
You can deploy this project to platforms like:

🟣 Render
🟢 Vercel
🔵 Railway

🤝 Credits
Groq API

React
Flask

📄 License
MIT License — use freely, with attribution. Contributions welcome!
Created by geeky4dev – feel free to fork, contribute, or star 🌟 the project!

