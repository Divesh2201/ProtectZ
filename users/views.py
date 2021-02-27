from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm


def register(request):
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created! You can now Login {username}!')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})