from django.shortcuts import render
from django.http import HttpResponse
# from .models import User
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'diagerda/index.html')
