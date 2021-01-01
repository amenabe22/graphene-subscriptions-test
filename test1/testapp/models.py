from django.db import models
# from test1.schema import MySubscription
# from .utils import tSaveHandler
# Create your models here.


class Testmodel(models.Model):
    xtt = models.CharField(max_length=200)

