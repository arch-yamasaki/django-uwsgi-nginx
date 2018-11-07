from django.shortcuts import render
from django.http import HttpResponse

from .models import Test


def index(request):
    ans = ""
    # t = Test.objects.get(pk=0)
    # ans += t.test_text
    return HttpResponse("Nephrosis 4")