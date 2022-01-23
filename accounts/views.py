from django.shortcuts import render

from .forms import RegistrationForm

# Create your views here.
def register(request):
    form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, template_name='accounts/register.html', context=context)

def login(request):
    return render(request, template_name='accounts/login.html')

def logout(request):
    return 