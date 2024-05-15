from django.db import models


class Dictionary(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.TextField(unique=True, null=False, blank=False)
    value = models.TextField(default="")
