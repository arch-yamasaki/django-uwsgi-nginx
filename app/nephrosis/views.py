from django.shortcuts import render
from django.http import HttpResponse

from .models import Test


def index(request):
    ans = "Nephrosis 7! : "
    t = Test.objects.get(pk=2)
    ans += t.test_text
    return HttpResponse(ans)