from django.urls import path, re_path
from . import views

app_name = "nephrosis"

urlpatterns = [
    path('', views.index, name='index'),
    path('test<str:test_id>', views.patients, name="patients"),
    path('test<str:test_id>/detail/<int:patient_id>/', views.detail, name="detail"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('sample', views.testview , name='test'),
]