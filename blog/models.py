from email.policy import default
from django.db import models
from account.models import User


# blog with 4 categories mental health, Heart Disease, Covid19, Immunization

CATEGORIES = (
    ('Mental Health', 'Mental Health'),
    ('Heart Disease', 'Heart Disease'),
    ('Covid19', 'Covid19'),
    ('Immunization', 'Immunization'),
)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORIES)
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



