from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1, password=password1)
        if user is None:
            return redirect('login')
        else:
            request.session['session_done']='All ok'
            return redirect('/')
    return render(request, 'login.html')