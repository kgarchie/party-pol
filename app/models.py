from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Party(models.Model):
    name = models.CharField(max_length=50)
    banner = models.FileField(upload_to='static/images')

    def __str__(self):
        return self.name


class CustomUser(User):
    party = models.ForeignKey(Party, related_name='associate_party', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
