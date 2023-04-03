from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
from django.conf import settings


class CustomUser(AbstractUser):
    id          = models.AutoField(primary_key=True)
    is_working = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

class CheckinCheckout(models.Model):
    id          = models.AutoField(primary_key=True)

    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    
    checkin_time = models.DateTimeField(default=timezone.now)
    checkout_time = models.DateTimeField(null=True, blank=True)



