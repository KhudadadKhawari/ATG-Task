from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .models import User, Address
from django.contrib import messages
from .forms import UserForm, AddressForm


# Create your views here.
class Home(View):
    context = {
        'title': 'Home',
        'active_nav': 'home',
    }

    def get(self, request):
        return render(request, 'account/home.html', self.context)


class Register(View):
    template_name = 'account/register.html'
    context = {
        'title': 'Register',
        'active_nav': 'register',
        'user_form': UserForm(),
        'address_form': AddressForm(),
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        user_form = UserForm(request.POST, request.FILES)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            user = user_form.save(commit=False)
            user.address = address
            user.set_password(user.password)
            user.save()
            messages.success(request, "User created successfully", "alert-success")
            return redirect('home')
        return render(request, self.template_name, self.context)


class UserLogin(View):
    template_name = 'account/login.html'
    context = {
        'title': 'Login',
        'active_nav': 'login',
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'Patient':
                return redirect('patient-dashboard')
            elif user.user_type == 'Doctor':
                return redirect('doctor-dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid credentials", "alert-danger")
            return render(request, self.template_name, self.context)

def user_logout(request):
    logout(request)
    return redirect('home')

class DoctorDash(View):
    template_name = 'account/doctor-dashboard.html'
    context = {
        'title': 'Doctor Dashboard',
        'active_nav': 'dashboard',
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

class PatientDash(View):
    template_name = 'account/patient-dashboard.html'
    context = {
        'title': 'Patient Dashboard',
        'active_nav': 'dashboard',
    }

    def get(self, request):
        return render(request, self.template_name, self.context)