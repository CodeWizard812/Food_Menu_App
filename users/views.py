from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        firstName = form.cleaned_data.get('first_name')
        lastName = form.cleaned_data.get('last_name')
        messages.success(request, f'You are logged in {firstName} {lastName}!')
        return redirect('login')
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')