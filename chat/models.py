from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)

    # def to_data(self):
    #     out = {}
    #     out['id'] = self.id
    #     out['from'] = self.user
    #     out['date'] = self.date.isoformat()
    #     out['text'] = self.text
    #     return out



