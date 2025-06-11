import openai

openai.api_key = "Your-open-api-secret-key....."

def get_gpt4_response(query):
    response = openai.ChatCompletion.create(
        model='gpt-4.1',
        messages=[
            {'role': 'user', 'content': query}
        ],
        temperature=0.4,
        stream=True
    )
    return response['choices'][0]['message']['content']


def generate_image(prompt):
    response = openai.images.generate(
        model="dall-e-3", 
        prompt=prompt,
        size="512x512",
        n=1,
    )
    return response.data[0].url

