from django.shortcuts import render, HttpResponse
# from .bot import answer

# Create your views here.
def index(request):
    # return render(request, 'chatbot/index.html')
    return render(request, 'chatbot/index.html')

def get_query(request):
    if request.method == "POST":
        query = request.POST.get('query')
        # response = answer(query)
        response = query
        context = {
            "question": query,
            "answer": response,
        }
        return render(request, "chatbot/chat.html", context)

    return render(request, 'chatbot/index.html')


