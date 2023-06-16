import random
import os
from django.db import models
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from user.models import User


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "images/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )


class SomeModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    thumbnail = ImageSpecField(
        source="logo",
        processors=[ResizeToFill(400, 400)],
        format="jpeg",
        options={"quality": 70},
    )
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
