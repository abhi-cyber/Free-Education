from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def resource(request):
        if request.session.has_key('session_done'):
            return render(request, 'resources.html')
        else:
            return render(request, 'resources.html')