from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.state}, {self.pincode}"

USER_TYPE = (
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
)

class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def profile_picture_url(self, instance):
        return f"static/profile_images/{instance}"
    
    profile_picture = models.ImageField(upload_to=profile_picture_url, null=True, default="static/profile_images/default.png")

    def __str__(self):
        return self.username
