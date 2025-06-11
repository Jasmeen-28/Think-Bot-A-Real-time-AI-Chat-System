# 🤖 Think-Bot-A-Real-time-AI-Chat-System

A powerful real-time AI chatbot built using **Django**, **WebSockets**, **OpenAI GPT-4.1**, and web technologies. The chatbot can respond via text, support voice chat (speech-to-text and text-to-speech), and even generate images on request!

![Screenshot 2025-06-11 120059](https://github.com/user-attachments/assets/503920d2-cbcc-4819-b2e5-bafe39e482a3)
![Screenshot 2025-06-11 123224](https://github.com/user-attachments/assets/08083ebf-d691-42da-9422-f83cc3d4fd77)



## 🌟 Features

- 💬 **Text-based Chat** powered by OpenAI GPT-4.1
- 🗣️ **Voice Chatting** using Speech-to-Text (Whisper) & Text-to-Speech (TTS)
- 🖼️ **Image Generation** using DALL·E (via OpenAI API)
- 🔌 Real-time communication via WebSockets
- 🧩 Multiple chat rooms with user separation
- 🎨 Clean and responsive frontend (HTML/CSS/JS)

## 🧠 Technologies Used

| Component        | Technology                         |
|------------------|-------------------------------------|
| Frontend         | HTML, CSS, JavaScript               |
| Backend          | Python, Django                      |
| Real-Time Comm.  | Django Channels (WebSocket support) |
| AI Engine        | OpenAI GPT-4.1                      |
| Voice Chat       | Whisper (STT), OpenAI TTS           |
| Image Generator  | DALL·E / OpenAI image API           |
| Deployment       | Localhost        |

## Set Environment Variables
Create a .env file:
OPENAI_API_KEY=your_openai_key_here

- Note :
   🔑 Get Your Own OpenAI API Key
To use this chatbot's AI features (text, voice, image generation), you must have your own OpenAI API key.

- 📌 Steps to Get an API Key:
1. Go to the OpenAI Platform and sign up or log in.

2. Visit your API Keys page.

3. Click “Create new secret key” and copy the key.

4. Paste this key into your .env file:

     OPENAI_API_KEY=your_api_key_here
⚠️ Keep your API key secure. Never share it publicly or commit it to version control (e.g., GitHub).

- Run Server :
  daphne gs4.asgi:application
  
- Open in Browser
   Visit: http://127.0.0.1:8000/chat/room1/

## 🧪 How It Works
- 📝 Text Chat
   Send text input, and GPT-4.1 generates intelligent replies in real-time.

- 🗣️ Voice Chat
   Uses Whisper API to convert your speech into text

- GPT-4.1 replies

  Text response is then converted back to speech using OpenAI's TTS

- 🖼️ Image Generator
    Ask for images (e.g., “Generate a futuristic cityscape”) and get AI-generated visuals using DALL·E.

  # 🙏 Acknowledgements
 - OpenAI GPT-4.1

- Whisper

- DALL·E

- Django

- Django Channels
