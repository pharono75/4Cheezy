from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/80 dark:bg-dark-card backdrop-blur-lg border border-gray-300 dark:border-dark-border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Имя пользователя'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/80 dark:bg-dark-card backdrop-blur-lg border border-gray-300 dark:border-dark-border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/80 dark:bg-dark-card backdrop-blur-lg border border-gray-300 dark:border-dark-border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/80 dark:bg-dark-card backdrop-blur-lg border border-gray-300 dark:border-dark-border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/80 dark:bg-dark-card backdrop-blur-lg border border-gray-300 dark:border-dark-border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Пароль'
    }))

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('news_home')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Ошибка в форме.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан! Можете войти.')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})