from django.shortcuts import render

# Create your views here.
from importlib.metadata import files

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password, email=email)
        x.save()
        return redirect('/')
    return render(request, 'signup.html')