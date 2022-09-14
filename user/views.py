from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm


# Create your views here.


def index(request):
    return render(request, 'user/main.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)
            return redirect('board:index')
        else:
            return render(request, 'user/register_form.html', {'form': form})

    elif request.method == 'GET':
        form = UserForm()
        return render(request, 'user/register_form.html', {'form': form})
