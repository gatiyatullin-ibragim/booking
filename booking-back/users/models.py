from django.db import models

# Create your models here.

class User(models.Model):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN'
        GUEST = 'GUEST'
        HOST = 'HOST'

    id = models.IntegerField(primary_key=True)
    email = models.TextField(unique=True, max_length=155)
    password_hash = models.TextField(max_length=155)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.GUEST
    )

    class Meta:
        db_table = "user"