from django.db import models


class Bio(models.Model):
    image = models.ImageField()
    image_height = models.PositiveIntegerField()
    image_width = models.PositiveIntegerField()
    text = models.TextField()
    mail_to = models.EmailField()

    def __str__(self):
        return 'Bio instance'

    class Meta:
        verbose_name_plural = 'Bio'


class Social(models.Model):
    index = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)
    name = models.TextField(blank=False, max_length=50)
    link = models.TextField(blank=False)

    def __str__(self):
        return self.name
