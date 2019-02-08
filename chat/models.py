from django.db import models


class Message(models.Model):
    user = models.ForeignKey(pk=user)
    text = models.CharField(max_length=300)
    created = models.DateTimeField()


