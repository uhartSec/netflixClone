from django.db import models
from django.utils import timezone
# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} :  {}".format(self.username, self.password)


