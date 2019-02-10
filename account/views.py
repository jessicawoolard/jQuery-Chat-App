from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from account.forms import SignUpUserCreationForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('chat:chat/index')


    else:
        form = SignUpUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
        logout(request)
        return redirect('chat:chat/index')


# class SignupView(TemplateView):
#     template_name = 'signup.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('chat:home')
