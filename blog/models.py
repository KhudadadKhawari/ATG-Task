from email.policy import default
from django.db import models
from account.models import User


CATEGORIES = ('Mental Health', 'Heart Disease', 'Covid19', 'Immunization')

CATEGORY_CHOICES = (
    ('Mental Health', CATEGORIES[0]),
    ('Heart Disease', CATEGORIES[1]),
    ('Covid19', CATEGORIES[2]),
    ('Immunization', CATEGORIES[3]),
)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    
    def blog_image_url(self, instance):
        return f"static/blog_images/{self.author.username}/{instance}"

    image = models.ImageField(upload_to=blog_image_url, default="static/blog_images/default.jpg")

    def __str__(self):
        return self.title

    # only doctors can create blog
    def save(self, *args, **kwargs):
        if self.author.user_type == "Doctor":
            super().save(*args, **kwargs)
        else:
            raise Exception("Only Doctors can create blog")



