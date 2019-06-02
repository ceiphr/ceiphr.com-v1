from django.db import models
from sorl.thumbnail import ImageField
import datetime

class Profile(models.Model):
    slogan = models.CharField(default="", max_length=100)
    desc = models.CharField(default="", max_length=300)
    logo = ImageField(default="", upload_to='img/assets/')
    resume_url = models.CharField(default="", max_length=100)
    favicon = ImageField(default="", upload_to='img/assets/')

class Project(models.Model):
    title = models.CharField(default="", max_length=50)
    summary = models.CharField(default="", max_length=200)

    image = ImageField(default="", upload_to='img/projects/')

    badges = models.TextField(default="", max_length=200)
    link = models.CharField(default="", max_length=50)

    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-active', '-end_date']

    def __str__(self):
        return self.title