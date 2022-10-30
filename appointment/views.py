from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Apointment
from .forms import AppointmentCreateForm
from account.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class AppointmentView(View):
    template_name = "appointment/appointment.html"
    form = AppointmentCreateForm()
    context = {
        "title": "Appointment",
        "active_nav": "appointment",
    }

    def get(self, request):
        if request.user.user_type == "Patient":
            appointments = Apointment.objects.filter(patient=request.user)
            # doctors list if request is done by patient
            doctors = User.objects.filter(user_type="Doctor")
            self.context["doctors"] = doctors
        else:
            appointments = Apointment.objects.filter(doctor=request.user)
        self.context["form"] = self.form
        self.context["appointments"] = appointments
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = AppointmentCreateForm(request.POST)
        doctor = User.objects.get(id=request.POST.get("doctor_id"))
        patient = request.user
        if form.is_valid():
            form.save(doctor, patient)
            return redirect("appointment")
        self.context["form"] = form
        return render(request, self.template_name, self.context)
