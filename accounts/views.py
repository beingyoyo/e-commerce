from django.shortcuts import render
from accounts.models import Account
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = Account.objects.create_user()
    form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, template_name='accounts/register.html', context=context)

def login(request):
    return render(request, template_name='accounts/login.html')

def logout(request):
    return 