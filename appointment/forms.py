from django import forms
from .models import Apointment
import datetime

class AppointmentCreateForm(forms.Form):
    specialtity = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"class": "form-control", "type": "time"}))

    def save(self, doctor, patient):
        data = self.cleaned_data
        # endtime should be 45 minutes form start time
        time_delta = datetime.timedelta(minutes=45)
        temp = datetime.datetime.combine(data["date"], data["start_time"])
        end_time = (temp + time_delta).time()

        Apointment.objects.create(
            doctor=doctor,
            patient=patient,
            speciality=data.get("specialtity"),
            date=data.get("date"),
            start_time=data.get("start_time"),
            end_time=end_time,
        )


