from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    return render(request, template_name='register.html', context={'form': form})
