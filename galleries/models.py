import os

from django.db import models
from django.utils.timezone import now
from PIL import Image as PilImage


def image_upload_path(instance, filename):
    """
    Function that returns image upload path.
    :return: /images/offers/{offer.id}/{filename}
    """
    return os.path.join('images', 'galleries', str(instance.gallery.id), filename)


class Gallery(models.Model):
    visible = models.BooleanField(default=True)
    is_new = models.BooleanField(default=0)
    index = models.IntegerField(default=0)
    # 0 - main, displayed on landing; first on menu. 1 - n are next ones.
    title = models.TextField(blank=False)
    desc = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f'Gallery {self.id} - {self.title}'


class Image(models.Model):
    visible = models.BooleanField(default=True)
    index = models.IntegerField(default=0)
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(upload_to=image_upload_path)
    file_small = models.ImageField(blank=True, editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save()
        img = PilImage.open(self.file.path)

        max_height = 3000
        max_width = 4000
        if img.height >= max_height or img.width >= max_width:
            output_size = (max_height, max_width)
            img.thumbnail(output_size)
        img.save(self.file.path)

        # Creating copy of image and resizing it to make it thumbnail.
        img_small = img.copy()
        img_small.thumbnail((1000, 1000))

        # Saving file with added '_sm' to filename.
        ext = self.file.path.split('.')[-1]
        img_small_path = self.file.path.replace('.' + ext, '_sm.' + ext)
        img_small.save(img_small_path)

        # Updating small file model field.
        self.file_small = self.file.name.replace('.' + ext, '_sm.' + ext)
        print(self.file_small.name)
        super().save()

    def __str__(self):
        return f'Gallery {self.gallery.id} - Image {self.id} - {self.title}'
