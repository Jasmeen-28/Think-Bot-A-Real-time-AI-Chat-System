# Project Overview :

This project is an AI-powered chatbot built with Django, Django Channels, and WebSockets. It enables real-time, intelligent, and interactive conversations between users and the chatbot. The chatbot leverages OpenAI's GPT models for providing context-aware responses, making the interaction engaging and dynamic.

# Technologies Used:

Frontend: HTML, CSS, JavaScript

Backend: Python, Django

WebSockets: Django Channels

AI: OpenAI API (GPT-4, GPT-3.5)

# Folder Structure:

D_channels > gs4

# How to Run:

In Terminal:-
....d_channels\gs4> python manage.py runserver [for Django]
....d_channels\gs4> daphne gs4.asgi:application[ for websockets connections]

In browers:-
http://127.0.0.1:8000/indexi/chat1/

indexi = url path
chat1 = chatroom name

