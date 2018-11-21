from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Patient, User, Result, Inspection, Exp

admin.site.register(Patient)
admin.site.register(User, UserAdmin)
admin.site.register(Result)
admin.site.register(Inspection)
admin.site.register(Exp)