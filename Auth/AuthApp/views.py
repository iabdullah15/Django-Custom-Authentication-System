from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse_lazy
from .models import CustomUser
from django.http import HttpRequest, HttpResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib.auth import login, authenticate



def index(request:HttpRequest):

    return render(request, 'index.html')


def register(request:HttpRequest):

    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))
    
    else:

        form = CustomUserCreationForm()

        if request.method == 'POST':

            form = CustomUserCreationForm(request.POST)

            if form.is_valid():

                form.save()
                return redirect(reverse_lazy('login'))


        return render(request, 'register.html', {'form':form})



def login_view(request):


    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))

    else:

        form = CustomAuthenticationForm()

        if request.method == 'POST':

            form = CustomAuthenticationForm(request, data=request.POST)

            if form.is_valid():

                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, email=email, password=password)

                if user is not None:

                    login(request, user)
                    return redirect(reverse_lazy('home'))

                else:
                    return render(request, 'login.html', {'form': form})  

                
        return render(request, 'login.html', {'form': form})