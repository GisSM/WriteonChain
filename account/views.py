from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def register(request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

def profilo(request):
    return render(request,'account/profilo.html')

