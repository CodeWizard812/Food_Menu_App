from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        firstName = form.cleaned_data.get('first_name')
        lastName = form.cleaned_data.get('last_name')
        messages.success(request, f'Account created for {firstName} {lastName}!')
        return redirect('food:index')
    return render(request, 'users/register.html', {'form': form})