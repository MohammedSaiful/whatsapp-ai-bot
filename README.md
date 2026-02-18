# WhatsApp AI Bot (FastAPI + Groq + Twilio)

A WhatsApp AI chatbot built using **FastAPI**, **Groq LLM (Llama 3.3 70B)**, and **Twilio WhatsApp Webhook**.

This bot receives WhatsApp messages and replies automatically using an AI model.

---

## Features

- ✅ FastAPI webhook server
- ✅ WhatsApp integration using Twilio
- ✅ AI responses powered by Groq (Llama 3.3 70B)
- ✅ Environment variable configuration
- ✅ Clean and minimal project structure

---

##  Project Structure

📦 whatsapp-ai-bot
┣ 📂 App
┃ ┗ 📜 ai_agent.py
┣ 📜 main.py
┣ 📜 requirements.txt
┗ 📜 README.md


---

## Technologies Used

- FastAPI
- Uvicorn
- Twilio API
- LangChain
- Groq LLM (llama-3.3-70b-versatile)
- Python-dotenv

---

##  How It Works

1. User sends a message to WhatsApp.
2. Twilio forwards the message to the FastAPI webhook.
3. The webhook calls the Groq LLM.
4. The AI generates a reply.
5. Twilio sends the reply back to the user.

---

##  Setup Instructions

### 1️⃣ Clone the Repository


### 2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3️⃣ Install Dependencies
- pip install -r requirements.txt


### 4️⃣ Add Environment Variables
 Create a .env file in root folder:
 GROQ_API_KEY=your_groq_api_key_here

### 5️⃣ Run the Server
 uvicorn main:app --reload

### 6️⃣ Connect with Twilio
1. Start ngrok:
- ngrok http 8000

2. Copy the HTTPS URL.

3. Paste it into Twilio WhatsApp sandbox webhook:
 https://your-ngrok-url/whatsapp