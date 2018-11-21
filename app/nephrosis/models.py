from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


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


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Result(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_prediction = models.BooleanField()
    is_correct = models.BooleanField()
    
    def __str__(self):
        return "patient:{} | user:{}".format(
            self.patient, self.user
        )


class Inspection(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    inspection_date = models.DateField()
    inspection_item = models.CharField(max_length=10)
    inspection_value = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return "name:{} | date:{} | item:{}".format(
        self.patient, str(self.inspection_date), self.inspection_item
        )
