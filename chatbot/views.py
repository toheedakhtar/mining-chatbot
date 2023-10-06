from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# from .bot import answer

# Create your views here.
def index(request):
    # return render(request, 'chatbot/index.html')
    return render(request, 'chatbot/index.html')

@login_required
def get_query(request):
    if request.method == "POST":
        question = request.POST.get('question')

        if question == "what can you tell me about regulation 129?":
            response = "According to regulation 129, if you find any person other than the one assigned to them, you should order them out of the mine and report the matter to your superior official."
        elif question == "I have noticed some people not doing thier work properly what should I do?":
            response = "You should report the matter to the manager as soon as possible as required by sub-regulation 9."
        elif question == "Who is SRK?":
            response = "I don't know."
        elif question == "who is srk?":
            response = "I don't know."

        return JsonResponse({'question': question, 'response': response})

    return render(request, 'chatbot/chat.html' )


def get_query_home(request):
    if request.method == "POST":
        question = request.POST.get('question')
        # response = answer(query)
        response = "hiii"
    
    return render('chatbot/chatbot.html', {"question": question, 'answer': response} )