from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.testview , name='test'),
    path('<int:patient_id>', views.detail, name="detail")
]