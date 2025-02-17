import uuid
from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import timedelta
from django.utils.timezone import now

class User(AbstractUser):
    image = models.ImageField(upload_to='Exhibition_image', null=True, blank=True)
    is_verificated = models.BooleanField(default=False)


class EmailVerification(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4(), unique=True)

    def __str__(self):
        return f'{self.user.username}'
