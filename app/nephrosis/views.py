from django.shortcuts import render

# Create your views here.
# polls/views.py¶
from django.http import HttpResponse

def index(request):
    return HttpResponse("Nephrosis 4")