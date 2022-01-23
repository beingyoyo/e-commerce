from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, template_name='accounts/register.html')

def login(request):
    return render(request, template_name='accounts/login.html')

def logout(request):
    return 