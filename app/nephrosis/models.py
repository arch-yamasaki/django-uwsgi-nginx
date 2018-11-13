from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_text = models.CharField(max_length=200)
    is_nephrosis = models.BooleanField()
    predict_is_nephrosis = models.BooleanField()
    nonnephs_proba = models.FloatField()
    nephs_proba = models.FloatField()

    def __str__(self):
        return self.patient_text


class Exp(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
    cond_exp = models.CharField(max_length=20)
    contribution = models.FloatField()

    # def __str__(self):
    #     return self.pk


class User(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class Result(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    user_prediction = models.BooleanField()
    is_correct = models.BooleanField()
    
    def __str__(self):
        return "patient:{} | user:{}".format(
            self.patient, self.user
        )


class Inspection(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    inspection_time = models.DateField()
    inspection_item = models.CharField(max_length=10)
    inspecgtion_value = models.FloatField()
    
    def __str__(self):
        return "name:{} | time:{} | item:{}".format(
        self.patient, str(self.inspection_time), self.inspection_item
        )
