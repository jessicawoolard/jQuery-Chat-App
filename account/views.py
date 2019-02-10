from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from account.forms import SignUpUserCreationForm


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


# class SignupView(TemplateView):
#     template_name = 'signup.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('chat:home')
