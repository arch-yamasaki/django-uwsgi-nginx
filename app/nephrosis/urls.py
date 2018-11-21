from django.urls import path
from . import views

app_name = "nephrosis"

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.testview , name='test'),
    path('<int:patient_id>', views.detail, name="detail"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]