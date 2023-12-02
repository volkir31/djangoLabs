from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    vk_id = models.IntegerField()


class UserImages(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
