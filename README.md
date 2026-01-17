# 🤖 AI-Chat-Master-Pro

A modern, high-performance AI Chatbot application built with **React**, **FastAPI**, and **Google Gemini 1.5 Flash**.

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=black)
![AI](https://img.shields.io/badge/AI-Gemini_1.5_Flash-8E75B2)

## ✨ Features

* **Real-time AI Chat:** Powered by Google's Gemini 1.5 Flash model for instant responses.
* **Modern UI:** Sleek, dark-mode interface built with React and Tailwind CSS.
* **Secure Architecture:** Backend proxy ensures API keys are never exposed to the client.
* **FastAPI Backend:** High-performance asynchronous API handling.
* **Memory Integration:** (Optional) Context-aware conversations using LangChain.

## 🛠️ Tech Stack

**Frontend:**
* React.js (Vite)
* Tailwind CSS
* Axios
* Lucide React (Icons)

**Backend:**
* Python 3.10+
* FastAPI
* Uvicorn
* LangChain Google GenAI
* Python-Dotenv

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Ai-Chat-Master-Pro.git](https://github.com/YOUR_USERNAME/Ai-Chat-Master-Pro.git)
cd Ai-Chat-Master-Pro
```
### 2. Backend Setup (Python)
Navigate to the backend folder and set up the environment.

cd backend

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

### 3. Configure API Key (Crucial Step)
You need a Google Gemini API Key. Get one here.

Create a file named .env inside the backend folder.

Paste your key inside:
# GOOGLE_API_KEY=AIzaSyYourKeyHere...

Note: This file is ignored by Git for security. Do not share it.

# 4. Run the Backend
python main.py
# OR
uvicorn main:app --reload

The server will start at http://localhost:8000.

5. Frontend Setup (React)
Open a new terminal and navigate to the root (or frontend folder).

Bash

# Install dependencies
npm install

# Start the development server
npm run dev
The app will run at http://localhost:5173.

📡 Deployment
Backend (Render/Vercel)
Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Environment Variables: Add GOOGLE_API_KEY in your hosting dashboard settings.

Frontend (Vercel/Netlify)
Update the API URL in App.js to point to your deployed backend (e.g., https://your-backend.onrender.com/chat).

Deploy using npm run build.

# 🛡️ Troubleshooting
Error: 403 / API Key Leaked

This means you accidentally pushed your key to GitHub.

# Fix: Generate a new key, update your .env file, and ensure .env is listed in your .gitignore file.

# Error: 405 Method Not Allowed

This means your frontend is sending requests to .../ instead of .../chat.

# Fix: Update your Axios request URL to end with /chat.

# 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
