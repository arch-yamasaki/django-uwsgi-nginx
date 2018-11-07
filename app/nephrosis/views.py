from django.shortcuts import render
from django.http import HttpResponse

from .models import Test

def testview(request):
    ans = "Nephrosis test! : "
    t = Test.objects.get(pk=2)
    ans += t.test_text
    block_body = "block"
    end_body = "end"
    context = {}
    return render(request, "nephrosis/sample.html", context)
    # return HttpResponse(ans)

def index(request):
    test_list = Test.objects.all()
    context = {"test_list": test_list}
    return render(request, "nephrosis/index.html", context)