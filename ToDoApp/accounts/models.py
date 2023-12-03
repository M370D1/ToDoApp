from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators


# Create your models here.
class CustomUser(AbstractUser):

    first_name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(2, message='Name should be at least 2 characters long'),
        ],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(2, message='Name should be at least 2 characters long'),
        ],
    )
    email = models.EmailField(
        unique=True,
    )
    photo = models.URLField()

    @property
    def get_user_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.first_name or self.last_name

    def __str__(self):
        return self.get_user_name or self.username
