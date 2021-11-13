from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
        if request.session.has_key('session_done'):
            return render(request, 'index.html')
        else:
            return render(request, 'index.html')