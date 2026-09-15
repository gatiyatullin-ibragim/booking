from django.db import models
# Create your models here.
from users.models import User


class Profile(models.Model):
    User = models.OneToOneField(
        User,
        id,
        on_delete=models.CASCADE
    )

    first_name = models.TextField(max_length=155)
    last_name = models.TextField(max_length=155)
    phone = models.TextField(max_length=155)
    avatar = models.URLField(blank=True)

    class Meta:
        db_table = "profile"