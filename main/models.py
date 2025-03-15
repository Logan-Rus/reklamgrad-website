from django.db import models

class Work(models.Model):
    title2 = models.CharField(max_length=200, verbose_name="")
    tip = models.TextField(verbose_name="", blank=True, null=True)
    description2 = models.TextField(verbose_name="", blank=True, null=True)
    image2 = models.ImageField(upload_to='works/', verbose_name="")


    def __str__(self):
        return self.title2

class Collection(models.Model):
    title = models.CharField(max_length=200, verbose_name="")
    description = models.TextField(verbose_name="", blank=True, null=True)
    image = models.ImageField(upload_to='collections/', verbose_name="")

    def __str__(self):
        return self.title

