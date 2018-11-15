# TODO:
# - [x]test task 1
# - test task 2

# FIXME:
# - test fixme 

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Patient, Exp, Result, User

def testview(request):
    context = {"is_ajax":request.is_ajax()}
    return render(request, "nephrosis/test.html", context)


def index(request):
    patient_list = Patient.objects.all()
    # patient_list = get_list_or_404(Patient)
    context = {"patient_list": patient_list}
    return render(request, "nephrosis/index.html", context)

def detail(request, patient_id):
    if request.is_ajax():
        user_is_nephs = request.POST["is_nephs"] == "nephs"
        patient_obj = get_object_or_404(Patient, pk=patient_id)
        user_id = 1
        user_obj = get_object_or_404(User, pk=user_id)
        is_correct = patient_obj.is_nephrosis == user_is_nephs
        defaults = {"user_prediction": user_is_nephs, "is_correct": is_correct}
        result, created = Result.objects.update_or_create(
            patient=patient_obj,
            user=user_obj,
            defaults=defaults,
        )
        return HttpResponse(request.POST["is_nephs"])
    else:
        exp_list = get_list_or_404(Exp, patient=patient_id)
        context = {
            "exp_list": exp_list,
            "patient_id": patient_id,
            "list_15" : range(15),
            "list_12" : range(12),
            }
        return render(request, "nephrosis/exp.html", context)

