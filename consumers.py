import json
import re
import os
import tempfile
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

connected_users = {}

class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.username = self.user.username
        connected_users[self.username] = self.channel_name
        await self.accept()

    async def disconnect(self, close_code):
        try:
            connected_users.pop(self.username, None)
            print(f"{self.username} disconnected gracefully.")
        except Exception as e:
            print(f"Disconnect error: {str(e)}")

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            await self.handle_voice_message(bytes_data)
        elif text_data:
            await self.handle_text_message(text_data)

    async def handle_text_message(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = data['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'type': 'text'
        }))

        try:
            lowered = message.lower()

            if lowered.startswith("generate image of") or lowered.startswith("show me an image of") or lowered.startswith("create an image of"):
                prompt = re.sub(r'^(generate|show me|create) (an |a )?image of', '', lowered).strip()

                try:
                    image_response = await asyncio.wait_for(
                        client.images.generate(
                            prompt=prompt,
                            n=1,
                            size="256x256"
                        ),
                        timeout=20
                    )
                    image_url = image_response.data[0].url

                    await self.send(text_data=json.dumps({
                        'message': image_url,
                        'sender': "Thinkbot",
                        'type': 'image'
                    }))

                except asyncio.TimeoutError:
                    await self.send(text_data=json.dumps({
                        'message': "Image generation timed out.",
                        'sender': "System",
                        'type': 'text'
                    }))

            else:
                try:
                    response = await asyncio.wait_for(
                        client.chat.completions.create(
                            model='gpt-4.1',
                            messages=[
                                {'role': 'system', 'content': "Your name is Jass. You are friendly and helpful."},
                                {'role': 'user', 'content': message}
                            ],
                            temperature=0.7
                        ),
                        timeout=20
                    )
                    content = response.choices[0].message.content

                    await self.send(text_data=json.dumps({
                        'message': content,
                        'sender': "Thinkbot",
                        'type': 'text'
                    }))

                except asyncio.TimeoutError:
                    await self.send(text_data=json.dumps({
                        'message': "Response timed out. Please try again.",
                        'sender': "System",
                        'type': 'text'
                    }))

        except Exception as e:
            await self.send(text_data=json.dumps({
                'message': f"Error: {str(e)}",
                'sender': "System",
                'type': 'text'
            }))

    async def handle_voice_message(self, audio_data):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_audio.write(audio_data)
                audio_path = temp_audio.name

            with open(audio_path, "rb") as audio_file:
                try:
                    transcription = await asyncio.wait_for(
                        client.audio.transcriptions.create(
                            model="whisper-1",
                            file=audio_file
                        ),
                        timeout=20
                    )
                except Exception as e:
                    print("Transcription error:", str(e))
                    await self.send(text_data=json.dumps({
                        'message': f"Transcription failed: {str(e)}",
                        'sender': "System",
                        'type': 'text'
                    }))
                    return

            user_input = transcription.text

            await self.send(text_data=json.dumps({
                'message': user_input,
                'sender': self.username,
                'type': 'text'
            }))

            try:
                response = await asyncio.wait_for(
                    client.chat.completions.create(
                        model='gpt-4.1',
                        messages=[
                            {"role": "system", "content": "Your name is Jass. You are friendly and helpful."},
                            {"role": "user", "content": user_input}
                        ]
                    ),
                    timeout=20
                )

                response_text = response.choices[0].message.content

                speech_response = await asyncio.wait_for(
                    client.audio.speech.create(
                        model="tts-1",
                        voice="nova",
                        input=response_text
                    ),
                    timeout=20
                )

                audio_bytes = speech_response.content

                await self.send(text_data=json.dumps({
                    'message': response_text,
                    'sender': "Thinkbot",
                    'type': 'text'
                }))

                await self.send(bytes_data=audio_bytes)

            except asyncio.TimeoutError:
                await self.send(text_data=json.dumps({
                    'message': "Voice processing timed out.",
                    'sender': "System",
                    'type': 'text'
                }))

        except Exception as e:
            await self.send(text_data=json.dumps({
                'message': f"Voice error: {str(e)}",
                'sender': "System",
                'type': 'text'
            }))
