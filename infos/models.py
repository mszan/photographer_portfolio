from django.db import models


class Bio(models.Model):
    image = models.ImageField()
    text = models.TextField()
    mail_to = models.EmailField()

    def __str__(self):
        return self.text
