from django.db import models
from ToDoApp.accounts.models import CustomUser


# Create your models here.
class ToDoItem(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    date_of_creation = models.DateField(
        auto_now=True,
    )
