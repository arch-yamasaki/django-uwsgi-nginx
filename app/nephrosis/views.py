# TODO:
# - [x]test task 1
# - test task 2

# FIXME:
# - test fixme 

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Patient, Exp, Result, User, Inspection

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
        patient_obj = get_object_or_404(Patient, pk=patient_id)
        exp_list = get_list_or_404(Exp, patient=patient_id)
        # order_by必要かもしれん
        date_list = Inspection.objects.filter(patient=patient_id).order_by("inspection_date").values_list("inspection_date", flat=True).distinct()
        item_list = ["ALB","BUN","CRE","CRP","Ca","Cl","IP","K","Na","T-CHO","PCR", "TP"]
        inspection_array = [Inspection.objects.filter(patient=patient_id, inspection_item=item).order_by("inspection_item").values_list("inspection_value", flat=True) for item in item_list]
        item_list = item_list = ["ALB","BUN","CRE","CRP","Ca","Cl","IP","K","Na","TCHO","PCR", "TP"]
        context = {
            "exp_list": exp_list,
            "patient_obj": patient_obj,
            "patient_id" : patient_id,
            "inspection_array" : inspection_array,
            "list_15" : range(15),
            "item_list" : item_list,
            "date_list": date_list,
            }
        return render(request, "nephrosis/exp.html", context)

