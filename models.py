from django.db import models
from .validators import validate_file_extension

# Create your models here.
class Slider_image(models.Model):
    Id = models.AutoField(primary_key=True)
    sliderimage = models.FileField(upload_to='slider_image/', validators=[validate_file_extension], null=True, blank=True)
    class Meta:
        ordering = ["Id"]
class Slider_image_App(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    sliderimage_App = models.FileField(upload_to='slider_image/',validators=[validate_file_extension], null=True, blank=True)
    keyword = models.CharField(max_length=25,null=True, blank=True)

    class Meta:
        ordering = ["Id"]
