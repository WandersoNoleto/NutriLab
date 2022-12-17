from django.contrib.auth.models import User
from django.db import models


class ActiveUser(models.Model):
    token  = models.CharField(max_length=64)
    user   = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
