from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import Usersignupform
# Create your views here.

# def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("login"))
#     else:
#         return render(request, 'users/user.html')


def signup(request):
    if request.method == 'POST':
        form = Usersignupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can Log in now!')
            return redirect('login')
    else:
        form = Usersignupform()
    return render(request, 'users/signup.html', {'form': form})
