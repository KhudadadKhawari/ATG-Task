from django.urls import path
from .import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('register/', views.Register.as_view(), name="register"),
    path('login/', views.UserLogin.as_view(), name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('doctor-dashboard/', views.DoctorDash.as_view(), name="doctor-dashboard"),
    path('patient-dashboard/', views.PatientDash.as_view(), name="patient-dashboard"),
]
