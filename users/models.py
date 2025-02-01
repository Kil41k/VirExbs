from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import timedelta
from django.utils.timezone import now

class User(AbstractUser):
    image = models.ImageField(upload_to='Exhibition_image', null=True, blank=True)
