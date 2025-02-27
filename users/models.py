from django.contrib.auth.models import AbstractUser
from django.db import models


# to specify custom user fields for to create CustomUser model.
class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    employee_cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
