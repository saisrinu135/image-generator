from django.shortcuts import render
import openai
from dotenv import load_dotenv
import os
# Create your views here.

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
def get_compeletion(promt, model="gpt-3.5-turbo-0301",temperature=0):
    messages = [{"role": "user", "content":promt}]
    response = openai.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature,
        )
    return response.choices[0].message.content
def index(request):
    
    text = ""

    if request.method == "POST":
        try:
            prompt = request.POST.get("prompt")

            text = get_compeletion(prompt)
        except Exception as e:
            print(e)

    return  render(request, 'index.html', context={'text':text, 'title':'Generate Text'})

def generateImage(request):

    images = ""

    if request.method == 'POST':
        try:
            prompt = request.POST.get('prompt')
            
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.images.generate(
                model="dall-e-2",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=2
            )
            images = [image.url for image in response.data]
            
        except Exception as e:
            print(e)

    return render(request, 'image-generator.html', context={'images':images, 'title':'Generate Image'})