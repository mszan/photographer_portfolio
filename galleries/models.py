import os

from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from PIL import Image as PilImage


def image_upload_path(instance, filename):
    """
    Function that returns image upload path.
    :return: /images/offers/{offer.id}/{filename}
    """
    return os.path.join('images', 'galleries', str(instance.gallery.id), filename)


class Category(models.Model):
    visible = models.BooleanField(default=True)
    index = models.IntegerField(default=0)
    title = models.TextField(blank=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    visible = models.BooleanField(default=True)
    main = models.BooleanField(default=False)
    index = models.IntegerField(default=0)
    title = models.TextField(blank=False)
    category = models.ForeignKey(Category, related_name='galleries', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # MAIN FIELD
        if self.main:
            try:
                temp_objs = Gallery.objects.filter(main=True)
                for temo_obj in temp_objs:
                    temo_obj.main = False
                    temo_obj.save()
            except Gallery.DoesNotExist:
                pass
        super().save()


class Image(models.Model):
    visible = models.BooleanField(default=True)
    index = models.IntegerField(default=0)
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(upload_to=image_upload_path)
    file_small = models.ImageField(blank=True)

    def save(self, *args, **kwargs):
        super().save()
        # IMAGE FIELD
        img = PilImage.open(self.file.path)

        max_height = 1400
        max_width = 1400
        if img.height >= max_height or img.width >= max_width:
            output_size = (max_height, max_width)
            img.thumbnail(output_size)
        img.save(self.file.path)

        # Creating copy of image and resizing it to make it thumbnail.
        img_small = img.copy()
        img_small.thumbnail((700, 700))

        # Saving file with added '_sm' to filename.
        ext = self.file.path.split('.')[-1]
        img_small_path = self.file.path.replace('.' + ext, '_sm.' + ext)
        img_small.save(img_small_path)

        # Updating small file model field.
        self.file_small = self.file.name.replace('.' + ext, '_sm.' + ext)
        print(self.file_small.name)
        super().save()

    def __str__(self):
        return f'image_{self.id}'
