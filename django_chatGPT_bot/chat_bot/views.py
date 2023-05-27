from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key


def ask_openai(message):
    reponse = openai.Completion.create(
        model='text-davinci-003',
        promt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = reponse.choices[0].text.strip()
    return answer


# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'Hi this is my response'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat_bot.html')
