from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Patient, Exp

def testview(request):
    context = {}
    return render(request, "nephrosis/sample.html", context)
    # return HttpResponse(ans)[]


def index(request):
    patient_list = Patient.objects.all()
    # patient_list = get_list_or_404(Patient)
    context = {"patient_list": patient_list}
    return render(request, "nephrosis/index.html", context)

def detail(request, patient_id):
    # exp_list = get_object_or_404(Exp, pk=patient_id)
    exp_list = get_list_or_404(Exp, patient=patient_id)
    context = {
        "exp_list": exp_list,
        "patient_id": patient_id
        }
    return render(request, "nephrosis/exp.html", context)


