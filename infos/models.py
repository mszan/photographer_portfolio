from django.db import models


class About(models.Model):
    photo = models.ImageField()
    text = models.TextField()

class Contact (models.Model):
    text = models.TextField()
    phone = models.PositiveIntegerField()
    mail = models.EmailField()
