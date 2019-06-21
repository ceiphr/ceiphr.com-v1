from django.db import models
from sorl.thumbnail import ImageField
import datetime


class Profile(models.Model):
    slogan = models.CharField(default="", max_length=100)
    desc = models.CharField(default="", max_length=300)
    logo = ImageField(default="", upload_to="img/assets/")
    resume_url = models.CharField(default="", max_length=100)
    favicon = ImageField(default="", upload_to="img/assets/")
